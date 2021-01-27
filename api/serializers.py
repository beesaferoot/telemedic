from rest_framework import serializers
from .models import DoctorProfile, PatientProfile, AppointMent, User

class DocSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorProfile
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PatientProfile
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class AppointMentSerializer(serializers.ModelSerializer):

    class Meta:
        AppointMent
        fields = '__all__'