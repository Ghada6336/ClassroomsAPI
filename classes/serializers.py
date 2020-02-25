from rest_framework import serializers
from django.contrib.auth.models import User

#from .models
from .models import Classroom

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","password"]

    # To encrypt password... dis
    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User(username=username)
        user.set_password(password)
        user.save()
        return validated_data

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id","subject","name","year","teacher"]



class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id","subject","name","year","teacher"]

class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ["subject","year","name"]

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["subject","year","name","teacher"]
