from django.urls import path
from product.views import *


app_name = "product"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

]
