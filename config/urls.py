from django.contrib import admin
from django.urls import path, include  
from django.views.generic import RedirectView  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('register/', include('users.urls')),    
    path('login/', include('users.urls')),  
    path('logout/', include('users.urls')),  
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # Redirect to login by default  
] 