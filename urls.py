from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoanUserViewSet
from .apps import ProjectApisConfig


app_name = ProjectApisConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'loan-users', LoanUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
