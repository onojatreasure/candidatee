from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.candidate_form,name='candidate_insert'), # get and post req. for insert operation
    path('<int:id>/', views.candidate_form,name='candidate_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.candidate_delete,name='candidate_delete'),
    path('list/',views.candidate_list,name='candidate_list') # get req. to retrieve and display all records
]