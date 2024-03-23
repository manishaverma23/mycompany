from django.contrib import admin
from .models import Contact,Quote,Service,Portfolio


class ContactAdmin(admin.ModelAdmin):
    list_display= ('email','name','message')
admin.site.register(Contact,ContactAdmin)

class QuoteAdmin(admin.ModelAdmin):
    list_display= ('email', 'name', 'mobile')
admin.site.register(Quote,QuoteAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display= ('file','title','description')
admin.site.register(Service,ServiceAdmin)

# class PortfolioAdmin(admin.ModelAdmin):
    # list_display=('file','text')
admin.site.register(Portfolio)