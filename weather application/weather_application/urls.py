from django.contrib import admin
from django.urls import path
from weather_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('delete/<CName>',views.delete_city,name="DCity"),
]
