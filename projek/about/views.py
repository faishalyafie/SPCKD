from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self):
        context = {
            'judul': 'About',
            'isi': 'About Website',
        }
        return context
