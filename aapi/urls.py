from django.urls import include, path
from rest_framework import routers
from . import views
from aapi.views import RecebedorViewSet

router = routers.DefaultRouter()

router.register(r'recebedors', RecebedorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/<int:pk>/', views.RecebedorViewSet.as_view({'get':'__all__'}), name='pics')
]