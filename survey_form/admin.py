from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from datetime import datetime
from django.utils.http import urlencode
from django.shortcuts import redirect


class ServayEntryResource(resources.ModelResource):

    class Meta:
        model = ServayEntry
        fields = ('sessionId', 'name', 'area__area_name', 'show__show_name', 'gender', 'created_at')


@admin.register(ServayEntry) 
class ServayEntryImportExport(ImportExportModelAdmin):
    resource_class = ServayEntryResource
    list_display = ('name', 'area', 'show', 'gender')
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False


    def changelist_view(self, request, extra_context=None):
        if request.GET:
            return super().changelist_view(request, extra_context=extra_context)

        date = datetime.now()
        params = ['day', 'month', 'year']
        field_keys = ['{}__{}'.format(self.date_hierarchy, i) for i in params]
        field_values = [getattr(date, i) for i in params]
        query_params = dict(zip(field_keys, field_values))
        url = '{}?{}'.format(request.path, urlencode(query_params))
        return redirect(url)


# Register your models here.
admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(Shows)
admin.site.register(Area)

admin.site.site_header = "Survey administration" 