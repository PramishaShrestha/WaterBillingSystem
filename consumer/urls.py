from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from consumer.views import customer_login_view, consumer_dashboardview, consumer_registration_formview, \
    consumer_adminview, consumer_signupview,  SignedOutView, billView
from home import views
from home.views import homeview

app_name = "consumer"

urlpatterns = [
    path('customer_login', customer_login_view, name='customer_login'),
    path('consumer_dashboard', consumer_dashboardview, name='consumer_dashboard'),
    path('consumer_registration_form', consumer_registration_formview, name='consumer_registration_form'),
    path('consumer_admin', consumer_adminview, name='consumer_admin'),
    path('consumer_signup', consumer_signupview, name='consumer_signup'),
    # path('consumerlogout', consumerlogoutview, name='consumerlogout'),
    path("signed_out", SignedOutView.as_view(), name="sign_out"),
    path('billView/<str:id>', billView, name='billview'),

    # path('consumer_dashboard', consumer_dashboardview, name='consumer_dashboard'),
    # path('consumer_update/<int:phone>', consumer_updateview, name='consumer_update'),
    # path('delete/<int:id>/', consumer_delete, name='consumer_delete'),

]