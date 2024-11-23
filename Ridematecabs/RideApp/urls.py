from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("", views.home, name='home'),
    path('packages-list/', views.packages_list, name='packages-list'),
  
    path('sedan/', views.sedans, name='sedan'),
    path('suvs/', views.suvs, name='suvs'),
    path('travaller/', views.travaller, name='tembo'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)