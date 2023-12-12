from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Import Django's built-in login views

app_name= 'user'# namespace for URL patterns
'''urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),  # User registration URL
    path('accounts/login/',  views.user_login, name='login'),# User login URL
    path('logout/', views.user_logout, name='logout'),   # User logout URL 
    path('register/create-vehicle-damage-assessment/', views.create_vehicle_damage_assessment, name='create-vehicle-damage-assessment'),# vehicle damage assesment form URL
    
]'''
urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('accounts/login/',  views.login_view, name='login'),# User login URL
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('profile/', views.profile, name='profile'),  # User profile
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('submit_report/', views.submit_report, name='submit_report'),  # Assessment submission
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # URL pattern for the about view
    path('contact/', views.contact, name='contact'),  # URL pattern for the contact view
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serving media files in development

# The `+ static(...)` part is necessary for Django to serve uploaded media files in development.
# Do not use this in a production setting.