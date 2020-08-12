# -*- coding: utf-8 -*-

from .models import Review_data
from import_export import resources

class ReviewDataResource(resources.ModelResource):
        class Meta:
            model = Review_data