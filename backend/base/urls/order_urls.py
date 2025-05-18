from django.urls import path
from base.views import order_views as views

<<<<<<< HEAD
urlpatterns = [
    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),

    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
]
=======

urlpatterns = [
 path('add/', views.addOrderItems, name='orders-add'),
 path('myorders/', views.getMyOrders, name='myorders'),
 path('<str:pk>/', views.getOrderById, name='user-order'),
 path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),

    
]
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
