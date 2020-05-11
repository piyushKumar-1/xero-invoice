from django.urls import path, include

urlpatterns = [
    path('', include('Oauth.urls')),
]
