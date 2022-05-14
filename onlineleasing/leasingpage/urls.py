from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage),
    path('adminlogin/', views.adminlogin),
    path('register/', views.registers),
    path('login/', views.lessorlogin),
    path('lesselogin/',views.lesselogin),
    path('lesseregister/',views.lesseregister),
    path('lessordatas/', views.lessordatas),
    path('pending/', views.pending),
    path('approved/', views.approved),
    path('approve/<int:id>', views.update),
    path('lessepending/', views.lessepending),
    path('lesseapproved/', views.lesseapproved),
    path('lesseapprove/<int:id>', views.lesseupdate),
    path('lesseview/', views.lesseview),
    path('orderlesse/',views.orderlesse),
    path('approveorder/',views.approveorder)



]
