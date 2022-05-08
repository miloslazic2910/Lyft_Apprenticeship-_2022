from django.urls import re_path as url
from django.contrib import admin
from MyApp import views

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^test/',views.test)
]
