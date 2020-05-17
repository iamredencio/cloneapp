from django.urls import path, include
from my_app import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
#    path('css/', include('my_app.urls')),
    path('admin/', admin.site.urls),
#    path('new-search/', views.new_search, name="new_Search"),
]