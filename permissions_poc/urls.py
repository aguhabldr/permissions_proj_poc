from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('', include('projects.urls'))
]   

urlpatterns += router.urls