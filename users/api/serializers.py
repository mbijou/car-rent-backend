from django.db.transaction import atomic
from rest_framework import serializers
from users.models import NotRegisteredUser, Address, NotRegisteredProfile


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("street", "house_number", "location", "postal_code", )

    def validate(self, attrs):
        print("OH I AM CALLED!")
        return super().validate(attrs)


class NotRegisteredProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = NotRegisteredProfile
        fields = ("address", )


class NotRegisteredUserSerializer(serializers.ModelSerializer):
    profile = NotRegisteredProfileSerializer()

    class Meta:
        model = NotRegisteredUser
        fields = ("first_name", "last_name", "email", "profile", )

    @atomic
    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        address_data = profile_data.pop("address")

        address = Address(address_data)
        address.save()

        not_registered_user = NotRegisteredUser(**validated_data, address=address)

        not_registered_user.save()

        return not_registered_user
