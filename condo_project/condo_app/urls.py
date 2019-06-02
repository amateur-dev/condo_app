from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.index, name='mainLandingPage'),
    path('app/signup', views.signup, name='signup'),
    path('app/<str:facility>',
         views.facility, name='facility_booking'),
    path('app/', include(
        'django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
