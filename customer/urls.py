
from django.urls import path
from. import views

app_name = 'customer'

urlpatterns = [
    # path('data/', views.customer_data,name="customer_data"),
    path('application_form/', views.application_form, name='application_form'),
    path('get_branches/<int:district_id>/', views.get_branches, name='get_branches'),
]