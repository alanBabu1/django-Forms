from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.StudentDetails.as_view(), name="add-student"),
    path('list/', views.StudentListDetails.as_view(), name="list-student"),
    path('update/<id>/', views.StudentUpdateDetails.as_view(), name="update-student"),
]