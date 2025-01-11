from rest_framework.serializers import ModelSerializer, CharField
from .models import User, Address, Progress


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ["id"]


class ProgressSerializer(ModelSerializer):
    class Meta:
        model = Progress
        fields = ["level", "experience"]


class UserListSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "phone_number",
            "role",
            "address",
            "progress",
        ]


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "phone_number",
            "role",
        ]
