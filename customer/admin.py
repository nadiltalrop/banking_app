from django.contrib import admin

from customer.models import AccountType, Application, Branch, District, Material

# Register your models here.

admin.site.register(District)


admin.site.register(Branch)


admin.site.register(AccountType)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
admin.site.register(Material, MaterialAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display =(
    "id",
    "name",
    'dob', 
    'age',
    'gender',
    'phone_number',
    'email',
    'address',
    "branch",
    )
admin.site.register(Application, ApplicationAdmin)