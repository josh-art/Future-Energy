from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index1, name='index'),
    path('projects', views.projects, name='projects'),
    path('partners', views.partners, name='partners'),
    path('mission/', views.mission, name='mission'),
    path('feedback/', views.contactForm, name='feedback'),
    path('about/', views.about, name='about'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
