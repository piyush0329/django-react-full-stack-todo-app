# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note,User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "username",
#             "email",
#         ]
#         extra_kwargs = {
#             "password":{"write_only":True}
#         }
#     def create(self,validated_data):
#         user  = User.objects.create_user(**validated_data)   
#         return user 

class UserSerializer(serializers.ModelSerializer):
   
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    pin_code = serializers.CharField(required=False, allow_blank=True)
    
    mobile = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile",
            "address",
            "pin_code",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        print("Validated data:", validated_data)  # Print validated data for debugging
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "author"
        ]
        extra_kwargs = {"author":{"read_only":True}}