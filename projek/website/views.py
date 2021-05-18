from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = {
            'judul': 'Home',
            'isi': 'Mulai Deteksi',
        }
        return context
