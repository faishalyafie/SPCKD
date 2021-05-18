from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from .models import DataModel
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from.forms import PostForm

# Create your views here.


class IndexListview(ListView):
    template_name = 'prediksi/index.html'
    model = DataModel
    extra_context = {
        'judul': 'List',
        'nama': 'Nama',
        'id': 'ID Pasien',
        'class': 'Classifications',
        'tombol': 'Actions'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


def pdf_view(request, *args, **kwargs):

    slug = kwargs.get('slug')
    data = get_object_or_404(DataModel, slug=slug)

    # pk = kwargs.get('pk')
    # data = get_object_or_404(DataModel, pk=pk)
    template_path = 'prediksi/pdf2.html'
    context = {'data': data}
    # Create a Django response object, and specify content_type as pdf note attachment dihilangkan
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class PostView(CreateView):
    model = DataModel
    template_name = 'prediksi/create.html'
    form_class = PostForm
    extra_context = {
        'judul': 'Deteksi',
        'body': 'Form Pemeriksaan'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class HapusView(DeleteView):
    model = DataModel
    template_name = 'prediksi/delete.html'
    success_url = reverse_lazy('prediksi:create')

    extra_context = {
        'judul': 'Detail',
        'body': 'Detail Pemeriksaan',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
