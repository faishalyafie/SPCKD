from .views import IndexListview, pdf_view, PostView, HapusView
from django.urls import path


app_name = 'prediksi'
urlpatterns = [
    path('', IndexListview.as_view(), name='index'),
    path('pdf/<slug:slug>/', pdf_view, name='pdf'),
    path('create/', PostView.as_view(), name='create'),
    path('detail/<slug:slug>/', HapusView.as_view(), name='delete'),
]
