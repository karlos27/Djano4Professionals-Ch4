from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Per la creació d'usuaris
    add_form = CustomUserCreationForm
    # Per l'edició d'usuaris
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "username", "is_superuser")

    # Configuració per la vista d'edició (no inclou password1, password2)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Afegir un form per la creació
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email")
        }),
    )

    # Opcions de filtres i recerca
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "username")

admin.site.register(CustomUser, CustomUserAdmin)
