"""
URL configuration for djpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
# from myapp.views import ObjectView
from myapp.views import StudentInfoDetailView,StudentInfoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/credentials/', views.get_credentials, name='get_credentials'),
    # path('api/object/', ObjectView.as_view(), name='object'),
    path('api/student_info/', StudentInfoView.as_view(), name='student_info'),
    path('api/student_info/<str:name>/', StudentInfoDetailView.as_view(), name='student_info_detail'),

]
