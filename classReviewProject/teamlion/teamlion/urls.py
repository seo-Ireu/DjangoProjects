
from django.contrib import admin
from django.urls import path
import teamlionapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',teamlionapp.views.index,name='index'),
    path('new', teamlionapp.views.new, name='new'),
    path('blog/edit/<int:blog_id>',teamlionapp.views.edit, name='edit'),
    path('blog/delete/<int:blog_id>',teamlionapp.views.delete,name='delete'),
    path('<int:blog_id>', teamlionapp.views.detail, name='detail'),
    path('search',teamlionapp.views.search,name='search')
    
]
