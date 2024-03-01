from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns= [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("admin_registration/",views.admin_regi,name="admin_registration"),
    path("admin_dash/",views.admin_dash,name="admin_dash")
    
]

