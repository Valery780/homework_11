from django.contrib import admin
from django.urls import path
from django.urls import include
from post.views import post
from editor.views import editor
from tag.views import tag


urlpatterns = [
    path('admin/', admin.site.urls),
    path("app/post/", post),
    path('post/', include('post.urls')),
    path('app/editor/', editor),
    path('editor/', include('editor.urls')),
    path('app/tag/', tag),
    path('tag/', include('tag.urls')),
]
    
