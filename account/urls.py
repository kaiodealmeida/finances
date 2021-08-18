from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='index_login'),
    path('cadastro', views.login, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
