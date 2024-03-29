from django.urls import path

from accountapp.views import hello_peter

app_name= "accountapp"

urlpatterns = [
    path('hello_peter/', hello_peter, name = 'hello_peter')
]