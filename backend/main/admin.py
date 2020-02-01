from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserAddForm ,CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserAddForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email' , 'is_staff')
    list_filter = ('email',)
    ordering = ('email',)
    search_fields = ('first_name',)
    fieldsets = (
        (None , {
            'fields' : (
                'first_name' , 'last_name' , 'email' , 'password'
            )
        }),
        ('Permissions' , {
            'fields':(
                'is_staff' , 'is_superuser', 'is_active'
            )
        })
    )
    add_fieldsets = (
        (None , {
            'classes' : 'wide',
            'fields' : (
                'first_name' , 'last_name' , 'email' , 'password1' , 'password2', 'is_staff' , 'is_active'
            )
        }),
    )