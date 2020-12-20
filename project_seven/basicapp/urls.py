from django.urls import path,include
from basicapp import views

# Template urls
app_name = 'basicapp'

urlpatterns=[
    path('register/$',views.register,name='register'),
    path('user_login/$',views.user_login,name='user_login'),
]
