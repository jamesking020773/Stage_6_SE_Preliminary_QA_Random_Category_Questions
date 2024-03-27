from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
]