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
    path("admin_dash/",views.admin_dash,name="admin_dash"),
    path("admin_contacts/",views.admin_contacts,name="admin_contacts"),
    path("quotations/",views.quotations,name="quotations"),
    path("delete_contacts/<int:id>",views.delete_contacts,name="delete_contacts"),
    path("delete_quotations/<int:id>",views.delete_quotations,name="delete_quotations"),
    path("services/",views.services,name="services"),
    path("view_services/",views.watch_services,name="watch_services"),
    path("delete_view_service/<int:id>",views.delete_view_service,name="delete_view_service"),
    path("updateservice/<int:id>",views.updateservice,name="updateservice"),
    path("add_portfolio/",views.add_portfolio,name="add_portfolio"),
    path("view_portfolio/",views.view_portfolio,name="view_portfolio"),
    path("updateportfolio/<int:id>",views.updateportfolio,name="updateportfolio"),
    path("delete_portfolio/<int:id>",views.delete_portfolio,name="delete_portfolio")

    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


