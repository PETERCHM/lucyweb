from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('payment/<int:website_id>/', views.payment, name='payment'),
    path('website/<int:website_id>/', views.website_access, name='website_access'),
]
