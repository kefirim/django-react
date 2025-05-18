<<<<<<< HEAD
from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name="products"),

    path('create/', views.createProduct, name="product-create"),
    path('upload/', views.uploadImage, name="image-upload"),
    path('top/', views.getTopProducts, name='top-products'),

    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),

    # Doit être en dernier
    path('<str:pk>/', views.getProduct, name="product"),
]
=======


#path est une fonction qui sert à définir des URL spécifiques. 
#Chaque URL correspond à une vue.

from django.urls import path

#Cela importe le fichier views.py de ton application actuelle (base ici). 
#Ainsi, tu peux appeler les fonctions définies dans views.py.
from base.views import product_views as views


#Cette liste contient toutes les routes (ou chemins d'accès) définies pour ton application.
urlpatterns = [
    #'' : Définit l'URL de base, c'est-à-dire http://127.0.0.1:8000/.
    #views.getRoutes : Associe cette URL à la vue getRoutes.
    #name='routes' : Donne un nom à cette route (utile pour la référencer ailleurs dans ton projet).
   
    path('', views.getProducts, name='products'),
    path('<str:pk>/', views.getProduct, name='product'),



]
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
