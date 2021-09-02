
from django.contrib import admin
from django.urls import path, include
from order_pizza.views import pizza_choiceList
from pizza_api.views import index
from django.views.generic import TemplateView
from order_pizza import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/',include('integrate.api.urls')),
    path('products/', views.pizza_choiceList),
    path('pizza-post/', views.pizza_post),
    path('api/pizza/<int:pk>',views.pizza_detail)
]
