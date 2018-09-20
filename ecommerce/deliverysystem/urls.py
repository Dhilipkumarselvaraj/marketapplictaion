from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test', views.test, name='test'),
    url(r'home',views.home,name='home'),
    url(r'addcustomer', views.add_customers, name='addcustomer'),
]
