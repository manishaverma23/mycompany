from django.contrib import admin
from .models import Contact,Quote


class ContactAdmin(admin.ModelAdmin):
    list_display= ('email','name','message')
admin.site.register(Contact,ContactAdmin)

class QuoteAdmin(admin.ModelAdmin):
    list_display= ('email', 'name', 'mobile')
admin.site.register(Quote,QuoteAdmin)
