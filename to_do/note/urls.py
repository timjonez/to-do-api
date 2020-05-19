from django.urls import path, include
from rest_framework.routers import DefaultRouter
from note import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet),
router.register(r'lists', views.ListViewSet),
router.register(r'notes', views.NoteViewSet),

urlpatterns = [
    path('',include(router.urls)),
]
