from django.urls import path
from . import views
from . import api
app_name='job'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add',views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    
    # api
    path('api/list',api.job_list_api, name='joblistapi'),
    path('api/detail/<int:id>',api.job_detail_api, name='jobdetailapi'),
    
    
    ## class based views
    path('api/v2/list',api.JobListApi.as_view() , name='job_list_api'),
    path('api/v2/detail/<int:id>',api.JobDetail.as_view() , name='job_detail_api'),

  
]