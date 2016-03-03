from django.contrib import admin

# Register your models here.
from work.models import wy_user, homework, newhomework, design
class WorkAdmin(admin.ModelAdmin):
	list_display = ('owner','desc','link','comment','create_time',)
	search_fields = ('owner',)
class UserAdmin(admin.ModelAdmin):
	list_display = ('user_name','phonenumber',)
	search_fields = ('user_name','phonenumber',)
    # list_display = homework._meta.get_all_field_names()
admin.site.register(wy_user,UserAdmin)
admin.site.register(homework,WorkAdmin)
admin.site.register(newhomework)
admin.site.register(design,WorkAdmin)
