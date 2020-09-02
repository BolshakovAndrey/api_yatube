from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentView, PostView

router = DefaultRouter()
router.register(r'api/v1/posts', PostView)
router.register(r'api/v1/posts/(?P<id>[0-9]+)/comments', CommentView)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
