from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from OverSkilledApp import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'about', views.AboutViewSet)
router.register(r'howto', views.HowToViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bonnet/', admin.site.urls),

    path('viewprojects', views.ProjectView.as_view()), # view list of projects
    path('projectdetails/<project_id>/', views.ProjectDetailsView.as_view()), # view detail of projects
    path('projectapply/<project_id>/', views.ProjectDetailsView.as_view()), # apply for project

    path('viewcompetitions', views.CompetitionView.as_view()), # view list of competitions
    path('competitionapply/<competition_id>/', views.ProjectDetailsView.as_view()), # apply for competition

    path('subscribe', views.SubscribersView.as_view()),
    path('contactus', views.ContactUsView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)