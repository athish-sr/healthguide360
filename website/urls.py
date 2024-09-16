from django.urls import path
from . import views
urlpatterns=[
  path("contact/",views.contact_view,name="contact"),
  path("home/",views.index_view,name="index"),
  path("about/",views.about_view,name="about"),
  path("diagnoser/",views.diagnoser_view,name="diagnoser"),
  path("hospitals-nearby/",views.hospitals_nearby_view,name="hospitals-nearby"),
  path("login/",views.login_view,name="login"),
  path("sign_up/",views.sign_up_view,name="sign_up"),
  path("logout/",views.logout_view,name="logout"),
  path("disease/",views.disease_view,name="disease"),
  path("mental/",views.mental_view,name="mental"),
  path('medicine/', views.medicine_list, name='medicine_list'),
  path('search/', views.search_medicine, name='search_medicine'),
  path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
  
] 