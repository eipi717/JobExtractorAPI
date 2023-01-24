from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('listjobs/', views.listAllJob,),
    path('listjob/<str:id>/', views.listJobByID),
    path('createjob/', views.createJob),
    path('updatejob/<str:id>/', views.updateJob),
    path('deletejob/<str:id>/', views.deleteJobByID),
]