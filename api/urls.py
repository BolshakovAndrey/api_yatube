from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import PostViewSet
from rest_framework.authtoken import views
# from rest_framework.authtoken.models import Token

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path(r'api/v1/posts/', PostViewSet.as_view({'get': 'list'})),
    path(r'api/v1/api-token-auth/', views.obtain_auth_token),
]