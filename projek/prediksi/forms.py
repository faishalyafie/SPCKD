from django import forms
from .models import DataModel


class PostForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = [
            'id_pasien',
            'nama',
            'jenis',
            'umur',
            'sg',
            'al',
            'hemo',
            'htn',
            'dm',
            'appet',
        ]
        widgets = {
            'id_pasien': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukan ID Pasien',
            }),
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukan Nama',
            }),
            'jenis': forms.Select(attrs={
                'class': 'form-control',
            }),
            'umur': forms.TextInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Masukan Umur',
            }),
            'sg': forms.Select(attrs={
                'class': 'form-control ',
            }),
            'al': forms.Select(attrs={
                'class': 'form-control ',
            }),
            'hemo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'g/dL',
            }),
            'htn': forms.Select(attrs={
                'class': 'form-control ',
            }),
            'dm': forms.Select(attrs={
                'class': 'form-control ',
            }),
            'appet': forms.Select(attrs={
                'class': 'form-control ',
            }),
        }
        labels = {
            'id_pasien': 'ID Pasien',
            'nama': 'Nama Lengkap',
            'jenis': 'Jenis Kelamin',
            'umur': 'Umur',
            'sg': 'Specific Gravity',
            'al': 'Albumin',
            'hemo': 'Hemoglobin',
            'htn': 'Hypertension',
            'dm': 'Diabetes Mellitus',
            'appet': 'Appetite',
        }
