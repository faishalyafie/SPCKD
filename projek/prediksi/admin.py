from django.contrib import admin
from .models import DataModel
# Register your models here.


class DBadmin (admin.ModelAdmin):
    readonly_fields = (
        'prediksi',
        'publish',
        'slug',
    )


admin.site.register(DataModel, DBadmin)
