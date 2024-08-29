from django.contrib import admin
from .models import User,Note,FamilyDetails,Brother,Sister
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class BrotherInline(admin.TabularInline):
    model = Brother
    extra = 1

class SisterInline(admin.TabularInline):
    model = Sister
    extra = 1


class FamilyDetailsInline(admin.StackedInline):
    model = FamilyDetails
    can_delete = False
    extra =1
    verbose_name_plural = 'Family Details'
    inlines = [BrotherInline, SisterInline]

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email',"first_name", "last_name", 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email',"first_name", "last_name",)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    inlines = [FamilyDetailsInline]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'mobile', 'address', 'pin_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(Note)
admin.site.register(FamilyDetails)
admin.site.register(Brother)
admin.site.register(Sister)
admin.site.register(User, UserAdmin)

