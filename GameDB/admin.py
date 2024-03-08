from django.contrib import admin
from GameDB.models import UserProfile, Category, Page, Game, Review

class GameAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only superusers (admins) can add games
        return request.user.is_superuser

class CategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only superusers (admins) can add categories
        return request.user.is_superuser

class ReviewAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # Only superusers (admins) can delete reviews
        return request.user.is_superuser

class UserProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Only superusers (admins) can view user profiles
        if request.user.is_superuser:
            return UserProfile.objects.all()
        else:
            return UserProfile.objects.none()

admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Page)
