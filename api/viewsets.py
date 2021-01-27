from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . import serializers
from .models import DoctorProfile as Doc, PatientProfile as Patient


class DoctorViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.DocSerializer
    queryset = Doc.objects.all()
    def list(self, req):
        qset = Doc.objects.all()
        serializer = serializers.DocSerializer(qset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, req, pk=None):
        qset = Doc.objects.all()
        profile = get_object_or_404(qset, pk=pk)
        serializer = serializers.DocSerializer(profile)
        return Response(serializer.data)

class PatientViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.PatientSerializer
    queryset = Patient.objects.all()
    def list(self, req):
        qset = Patient.objects.all()
        serializer = serializers.PatientSerializer(qset, many=True)
        return Response(serializer.data)

    def retrieve(self, req, pk=None):
        qset = Patient.objects.all()
        profile = get_object_or_404(qset, pk=pk)
        serializer = serializers.PatientSerializer(profile)
        return Response(serializer.data)
