from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from OverSkilledApp import views

router = routers.DefaultRouter()
router.register(r'about', views.AboutViewSet)
router.register(r'howto', views.HowToViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('viewprojects', views.ProjectView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
