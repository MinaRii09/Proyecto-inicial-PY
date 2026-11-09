import io, zipfile
from datetime import datetime
from django.utils import timezone
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()

    categoria = request.GET.get('categoria')
    orden = request.GET.get('orden')

    if categoria:
        posts = posts.filter(categoria=categoria)

    if orden == 'antiguos':
        posts = posts.order_by('date')
    else:
        posts = posts.order_by('-date')

    return render(request, 'posts/posts_list.html', {
        'posts': posts
    })


def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_page.html', {'post' : post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

@login_required(login_url="/users/login/")
def export_reports(request):
    reports = Post.objects.all()
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        wb = Workbook()
        ws = wb.active
        ws.title = "Reportes"

        summary = wb.create_sheet("Resumen")
        summary.append(["Estadística", "Valor"])
        summary.append([
            "Total de reportes",
            reports.count()
        ])
        summary.append([])
        summary.append(["Reportes por categoría", "Cantidad"])
        for codigo, nombre in Post.CATEGORIAS:
            cantidad = Post.objects.filter(
                categoria=codigo
            ).count()
            summary.append([
                nombre,
                cantidad
            ])
        con_imagen = Post.objects.exclude(
            banner=''
        ).count()
        
        summary.append([])

        summary.append([
            "Exportado por",
            request.user.username
        ])
        summary.append([
            "Fecha de exportación",
            datetime.now().strftime("%d/%m/%Y %H:%M")
        ])

        summary.append([
            "Reportes con imagen",
            con_imagen
        ])
        header_fill = PatternFill(
            fill_type="solid",
            start_color="1F4E78"
        )
        for cell in summary[1]:
            cell.font = Font(
            bold=True,
            color="FFFFFF"
            )
            cell.fill = header_fill
        
        for column in summary.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                if cell.value:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            summary.column_dimensions[
                column_letter
            ].width = max_length + 5

        headers = [
            'ID',
            'Título',
            'Descripción',
            'Categoría',
            'Usuario',
            'Fecha de reporte',
            'Imagen Adjunta',
            'Latitud',
            'Longitud',
            'Google Maps'
        ]
        
        ws.append(headers)

        for report in reports:
            lat = round(report.latitude, 6) if report.latitude else ""
            lng = round(report.longitude, 6) if report.longitude else ""
            maps_link = (
                f"https://www.google.com/maps?q={lat},{lng}"
                if lat and lng
                else ""
            )

            ws.append([
                report.id,
                report.title,
                report.body,
                report.get_categoria_display(),
                report.author.username,
                timezone.localtime(report.date).strftime("%d/%m/%Y %H:%M"),
                report.banner.name if report.banner else '',
                lat,
                lng,
                maps_link,
            ])
            current_row = ws.max_row
            maps_cell = ws.cell(row=current_row, column=10)
            maps_cell.hyperlink = maps_link
            maps_cell.style = "Hyperlink"
            maps_cell.value = "Abrir ubicación"

            if report.banner:
                zip_file.write(
                    report.banner.path,
                    f"images/{report.id:04d}_{report.banner.name.split('/')[-1]}"
                )
        for cell in ws[1]:
            cell.font = Font(
                bold=True,
                color="FFFFFF"
            )
            cell.fill = header_fill

        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                try:
                    if cell.value:
                        max_length = max(
                            max_length,
                            len(str(cell.value))
                        )
                except Exception:
                    pass

            ws.column_dimensions[column_letter].width = min(max_length + 2, 50)
            ws.column_dimensions["C"].width = 50
            for row in ws.iter_rows():
                for cell in row:
                    cell.alignment = Alignment(
                        wrap_text=True, vertical="top"
                    )

        ws.freeze_panes = 'B2'
        ws.auto_filter.ref = ws.dimensions
        excel_buffer = io.BytesIO()
        wb.save(excel_buffer)
        excel_buffer.seek(0)
        zip_file.writestr(
            'reports.xlsx',
            excel_buffer.getvalue()
        )
    zip_buffer.seek(0)
    response = HttpResponse(
        zip_buffer.getvalue(),
        content_type='application/zip'
    )
    response["Content-Disposition"] = (
        'attachment; filename="reports_export.zip"'
    )
    return response