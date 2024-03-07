from django.contrib import admin

# Register your models here.



#CODE RIPPED FROM TANGO_WITH_DJANGO - J

from django.contrib import admin
from GameDB.models import UserProfile

# Register your models here.

from django.contrib import admin
from GameDB.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
    
...
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # Update the registration to include this customised interface




admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)