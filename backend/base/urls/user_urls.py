<<<<<<< HEAD
from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),
    
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),

    # Routes spécifiques avec paramètres (à placer AVANT la route générique <str:pk>)
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),

    # Route générique pour un utilisateur par ID (à mettre après les autres)
    path('<str:pk>/', views.getUserById, name='user'),

    # Liste des utilisateurs (mettre en dernier si on veut garder la logique REST claire)
    path('', views.getUsers, name='users'),
]
=======


#path est une fonction qui sert à définir des URL spécifiques. 
#Chaque URL correspond à une vue.

from django.urls import path

#Cela importe le fichier views.py de ton application actuelle (base ici). 
#Ainsi, tu peux appeler les fonctions définies dans views.py.
from base.views import user_views as views


#Cette liste contient toutes les routes (ou chemins d'accès) définies pour ton application.
urlpatterns = [
    #'' : Définit l'URL de base, c'est-à-dire http://127.0.0.1:8000/.
    #views.getRoutes : Associe cette URL à la vue getRoutes.
    #name='routes' : Donne un nom à cette route (utile pour la référencer ailleurs dans ton projet).
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='users-profile'),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('register/', views.registerUser, name='register'),
    path('', views.getUsers, name='users'),
    
]
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
