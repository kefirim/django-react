from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
<<<<<<< HEAD
from .models import Product, Order, OrderItem, ShippingAddress, Review


class UserSerializer(serializers.ModelSerializer):
=======
from .models import Product, Order, OrderItem, ShippingAddress

class UserSerializer(serializers.ModelSerializer):
    # Ajout du champ personnalisé "name"
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
<<<<<<< HEAD
        return obj.is_staff

    def get_name(self, obj):
=======
        return obj.is_staff    

    def get_name(self, obj):
        # Si le champ "first_name" est vide, utiliser l'email
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        name = obj.first_name
        if name == '':
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
<<<<<<< HEAD
=======
   # Modèle utilisé pour le serializer : User (utilisateur intégré de Django)
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
<<<<<<< HEAD
=======
      # Génération d'un token d'accès (access token) pour l'utilisateur
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


<<<<<<< HEAD
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # utilise related_name='reviews'

=======
class ProductSerializer(serializers.ModelSerializer):
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
    class Meta:
        model = Product
        fields = '__all__'

<<<<<<< HEAD

=======
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
<<<<<<< HEAD
            address = ShippingAddressSerializer(obj.shippingaddress, many=False).data
=======
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
        except:
            address = False
        return address

    def get_user(self, obj):
<<<<<<< HEAD
        serializer = UserSerializer(obj.user, many=False)
        return serializer.data
=======
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data
>>>>>>> 2d0e5b5859a900e9b7dc8af44d1896a5e9f4b610
