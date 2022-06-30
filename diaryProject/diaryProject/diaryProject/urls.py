from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import diaryApp.views
urlpatterns = [
     path('admin/', admin.site.urls),
    path('',diaryApp.views.index,name='index'),
    path('new',diaryApp.views.new,name='new'),
    path('<int:diary_id>',diaryApp.views.detail,name='detail'),
    path('diary/edit/<int:diary_id>',diaryApp.views.edit,name='edit'),
    path('diary/delete/<int:diary_id>',diaryApp.views.delete,name='delete'),
 path('accounts/',include('allauth.urls')),
]

urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

