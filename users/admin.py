from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_help_text = "You can search for bookmarks' id, author's username, book's isbn or title"
    fields = ('user', 'book', 'type')
    list_display = ('id', 'user', 'book', 'type', 'date')
    list_filter = ['type', 'date']
    search_fields = ['id', 'user__username', 'book__isbn', 'book__title']


class CustomUserAdmin(UserAdmin):
    ADDITIONAL_USER_FIELDS = (
        (None, {'fields': ('profile_pic', 'bio',)}),
    )
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = ADDITIONAL_USER_FIELDS + UserAdmin.fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
