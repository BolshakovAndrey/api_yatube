from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentView, PostView

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostView)
router_v1.register(r'posts/(?P<id>[0-9]+)/comments', CommentView)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
