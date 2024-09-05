# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note,User,FamilyDetails,Brother,Sister

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
    
   
    first_name = serializers.CharField( required=False, allow_blank=True)
    last_name = serializers.CharField( required=False, allow_blank=True)
    pin_code = serializers.CharField( required=False, allow_blank=True)
    pan_card = serializers.CharField( required=False, allow_blank=True)
    aadhar_card = serializers.CharField( required=False, allow_blank=True)
    
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
            "pan_card",
            "aadhar_card",
            "profile_pic"
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

class BrotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brother
        fields = ['id', 'name']

class SisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sister
        fields = ['id', 'name']

class FamilyDetailsSerializer(serializers.ModelSerializer):
    brothers = BrotherSerializer(many=True)
    sisters = SisterSerializer(many=True)
    class Meta:
        model = FamilyDetails
        fields = [
            "id",
            "total_members",
            "father_name",
            "mother_name",
            "brothers",
            "sisters",
            "grandfather_name",
            "grandmother_name",
            "created_at",
            "user"
        ]   
        extra_kwargs = { "user":{"read_only":True} }   


    def create(self, validated_data):
        brothers_data = validated_data.pop('brothers')
        sisters_data = validated_data.pop('sisters')
        family_details = FamilyDetails.objects.create(**validated_data)
        for brother_data in brothers_data:
            Brother.objects.create(family_details=family_details, **brother_data)
        for sister_data in sisters_data:
            Sister.objects.create(family_details=family_details, **sister_data)
        return family_details
    
    def update(self, instance, validated_data):
        brothers_data = validated_data.pop('brothers', None)
        sisters_data = validated_data.pop('sisters', None)
        
        instance.total_members = validated_data.get('total_members', instance.total_members)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.mother_name = validated_data.get('mother_name', instance.mother_name)
        instance.grandfather_name = validated_data.get('grandfather_name', instance.grandfather_name)
        instance.grandmother_name = validated_data.get('grandmother_name', instance.grandmother_name)
        instance.save()

        if brothers_data is not None:
            instance.brothers.all().delete()  # Delete existing brothers
        for brother_data in brothers_data:
            Brother.objects.create(family_details=instance, **brother_data)

        # Handle sisters update
        if sisters_data is not None:
            instance.sisters.all().delete()  # Delete existing sisters
        for sister_data in sisters_data:
            Sister.objects.create(family_details=instance, **sister_data)
        return instance

