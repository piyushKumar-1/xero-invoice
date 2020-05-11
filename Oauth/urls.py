from django.urls import path
from . import views

app_name = "Oauth"

urlpatterns = [
    path('', views.index, name='index'),
    path("auth/", views.auth, name="auth"),
    path("add/", views.add_invoice, name="add"),
    path("addline/", views.add_line, name="addl"),
    path("addcontact/<str:conID>", views.add_conID, name="addcID"),
    path("done/", views.submit, name="submit"),

]
