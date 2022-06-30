from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from post import views

router=DefaultRouter()
router.register('essay/',views.PostViewSet)
router.register('album/',views.ImgViewSet)
router.register('files/',views.FileViewSet)
urlpatterns = [
    path('',include(router.urls)),
   
]
