from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='index_dashboard'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('acoes/', views.acoes, name='acoes'),
    path('covariancia/', views.covariancia, name='covariancia'),
    path('correlacao/', views.correlacao, name='correlação'),
]
