<<<<<<< HEAD
from django.shortcuts import render
=======

#La fonction render est utilisée pour générer et renvoyer des pages HTML en combinant un modèle HTML avec des données.
#Dans ce cas précis, elle n'est pas utilisée car tu envoies une réponse JSON


from django.shortcuts import render
#La classe JsonResponse permet de renvoyer une réponse JSON à un client. C'est très utile pour les API ou les projets avec des interfaces React ou Vue.js.


>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User
<<<<<<< HEAD
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

=======

from base.serializers import  UserSerializer, UserSerializerWithToken
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
from django.contrib.auth.hashers import make_password
from rest_framework import status


<<<<<<< HEAD
=======

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
<<<<<<< HEAD
    serializer_class = MyTokenObtainPairSerializer

=======
    serializer_class = MyTokenObtainPairSerializer        
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610

@api_view(['POST'])
def registerUser(request):
    data = request.data
<<<<<<< HEAD
    try:
=======

    try:
        # Création de l'utilisateur
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
<<<<<<< HEAD
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
=======
            password=make_password(data['password'])  # Hash le mot de passe
        )

        # Sérialisation et retour des données
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)

    except:
        # Gestion des erreurs, par ex. utilisateur existant
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


<<<<<<< HEAD
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

=======



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
   user = request.user
   serializer = UserSerializer(user, many=False)
   return Response(serializer.data)
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
<<<<<<< HEAD
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')
=======
   users = User.objects.all()
   serializer = UserSerializer(users, many=True)
   return Response(serializer.data) 
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
