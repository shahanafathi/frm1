"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from appz import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('regstrpage',views.regstrpage,name='regstrpage'),
    path('registerpg',views.registerpg,name='registerpg'),
    path('search',views.search,name='search'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edits/<int:id>',views.edits,name='edits'),
    path('page1',views.page1,name='page1'),
    path('form',views.formpage,name='form'),
    path('form1',views.form,name='form1'),
    path('form3',views.hosp,name='form3'),
    path('mdlform',views.mdlform,name='mdlform'),
    path('tblmdl',views.tblmdl,name='tblmdl'),
    path('del_tbl/<int:id>',views.del_tbl,name='del_tbl'),
    path('edit/<int:id>',views.edit,name='edit'),
]
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
