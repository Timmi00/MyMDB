
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, FilmViewSet, StaffViewSet,  expired_obtain_auth_token


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'films', FilmViewSet)
router.register(r'staffs', StaffViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
