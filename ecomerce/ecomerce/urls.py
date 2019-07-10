from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usuario/', include('usuario.urls')),
   # path('', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_then_login, name='loguot'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# personalización de los títulos del administrador
admin.site.site_header = "Administración de la ecomerce"
admin.site.index_title = "Ecomerce"
admin.site.site_title = "Administración ecomerce"
