from . import views
from django.urls import path


urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('api/englistings/', views.engtaskList, name="englistings"),
 	path('api/bdlistings/', views.bdtaskList, name="bdlistings"),
  	path('api/videolistings/', views.videotaskList, name="videolistings"),
 
   
    

]



