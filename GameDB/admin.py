from django.contrib import admin
from django.contrib.auth.models import User
from GameDB.models import UserProfile, Category, Page, Game, Review

class GameAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

class CategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

class ReviewAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'  # Sets column header in admin interface.
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email' 
    
    def is_staff(self, obj):
        return obj.user.is_staff
    is_staff.short_description = 'Staff Status'
    
    def is_active(self, obj):
        return obj.user.is_active
    is_active.short_description = 'Active Status' 


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Page)
