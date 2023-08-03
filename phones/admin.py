from django.contrib import admin

# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
