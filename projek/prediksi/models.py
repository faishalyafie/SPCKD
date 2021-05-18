from django.db import models
from django.utils.text import slugify
from .algo import model_knn
from django.urls import reverse

# Create your models here.


class DataModel(models.Model):
    id_pasien = models.CharField(max_length=200)
    nama = nama = models.CharField(max_length=200)
    umur = models.CharField(max_length=200)
    gender = (
        ('', '-Pilih-'),
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    )
    jenis = models.CharField(max_length=200, choices=gender, default='-Pilih-')
    sg_c = (
        ('', '-Pilih-'),
        (1.005, '1.005'),
        (1.010, '1.010'),
        (1.015, '1.015'),
        (1.020, '1.020'),
        (1.025, '1.025'),
        (1.020, 'Lainya'),
    )
    sg = models.FloatField(null=False, choices=sg_c, default='-Pilih-')
    al_c = (
        ('', '-Pilih-'),
        (0.0, '0'),
        (1.0, '1'),
        (2.0, '2'),
        (3.0, '3'),
        (4.0, '4'),
        (5.0, '5'),
        (0.0, 'Lainya'),
    )
    al = models.FloatField(choices=al_c, default='-Pilih-')

    hemo = models.FloatField()

    htn_c = (
        ('', '-Pilih-'),
        (1.0, 'Yes'),
        (0.0, 'No'),
        (0.0, 'Lainya'),
    )
    htn = models.FloatField(choices=htn_c, default='-Pilih-')

    dm_c = (
        ('', '-Pilih-'),
        (1.0, 'Yes'),
        (0.0, 'No'),
        (0.0, 'Lainya'),
    )
    dm = models.FloatField(choices=dm_c, default='-Pilih-')

    appet_c = (
        ('', '-Pilih-'),
        (1.0, 'Good'),
        (0.0, 'Poor'),
        (1.0, 'Lainya'),
    )
    appet = models.FloatField(choices=appet_c, default='-Pilih-')

    prediksi = models.CharField(blank=True, max_length=200, editable=False)
    publish = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        sg = self.sg
        al = self.al
        hemo = self.hemo
        htn = self.htn
        dm = self.dm
        appet = self.appet
        hasil = model_knn(sg, al, hemo, htn, dm, appet,)
        self.prediksi = slugify(hasil)
        self.slug = slugify(self.id_pasien)
        super(DataModel, self).save()

    def get_absolute_url(self):
        urls_slug = {
            'slug': self.slug,
        }
        return reverse('prediksi:delete', kwargs=urls_slug)

    def __str__(self):
        return self.id_pasien + " | " + self.nama
