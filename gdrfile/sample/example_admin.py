from django.contrib import admin
from {{path_to_app}}.models import {{MainClass}}


@admin.register({{MainClass}})
class {{MainClass}}Admin(admin.ModelAdmin[{{MainClass}}]):
    """{{docs}}"""

    list_filter = {{list_main_fields}}
    search_fields = {{list_main_fields}}
    list_display = {{list_main_fields}}
