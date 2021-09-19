from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('acoes', views.AcoesView)

urlpatterns = [
    path('', views.dashboard, name='index_dashboard'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('acoes/', views.acoes, name='acoes'),

    path('covariancia/', views.covariancia, name='covariancia'),
    path('correlacao/', views.correlacao, name='correlação'),
    path('api/', include(router.urls), name='api'),


]
