from django.contrib import admin
from .models import Review_data, Review_Classfiy
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .resources import ReviewDataResource
# Register your models here.

@admin.register(Review_data)


class ReviewDataAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Review_Classfiy)
