from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
#    path('css/', include('my_app.urls')),
    path('admin/', admin.site.urls),
    path('new_search.html', views.new_search, name="new_search"),
]