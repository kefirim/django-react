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
