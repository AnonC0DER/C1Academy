from django.urls import path
from API import views


urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='create')
]
