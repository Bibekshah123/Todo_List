"""
URL configuration for todo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views
from todo.views import delete_file, upload_document, delete_task, document_list, download_file
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    #home page
    path('', views.index, name='todo'),
    path('del/<int:item_id>', delete_task, name="del"),
    path('admin/', admin.site.urls),
    path('documents/', document_list, name='document_list'),
    path('document_list/', upload_document, name='upload_document'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
    path('download/<int:file_id>/', download_file, name='download_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
