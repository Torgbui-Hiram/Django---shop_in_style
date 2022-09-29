from django.contrib import admin
from . models import NewUser

# Register your models here.


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'username', 'email', 'birth_date',)
    search_fields = ('first_name', 'last_name', 'username',)
    list_filter = ('first_name', 'last_name', 'username',)
