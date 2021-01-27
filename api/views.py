from django.shortcuts import render, get_object_or_404
from django.core import exceptions
from datetime import date as dt, datetime
from django.utils import datetime_safe
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
import json
from .models import DoctorProfile, PatientProfile

class PlaceAppointMent(APIView):

    def post(self, req, appointment_pk=None):
        try:
            data = json.loads(req.body)  
            date = data["appointment_date"]
            id = data["doc_id"]
            doc_profile = get_object_or_404(DoctorProfile, pk=id)
            # validate for dates from the past 
            if datetime.strptime(date, "%Y-%m-%d").date() < dt.today():
                return Response({'detail': 'an appointment cannot be scheduled at this date'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                doc_profile.appointment_set.get(date=date)
            except exceptions.ObjectDoesNotExist:
                patient_profile = get_object_or_404(PatientProfile, pk=appointment_pk)
                patient_profile.appointment = date
                patient_profile.save()
                return Response({'detail': 'appointment has been successfully scheduled'}, status=status.HTTP_201_CREATED)
            return Response({'detail': 'an appointment cannot be scheduled at this date'}, status=status.HTTP_400_BAD_REQUEST)
            
        except json.decoder.JSONDecodeError as err:
            return Response({'detail': 'unable to process payload body'},
            status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'detail': 'internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlockAppointMentDate(APIView):

    def post(self, req, doc_pk=None):
        try:
            data = json.loads(req.body)
            date = data["cancel_date"]
            if datetime.strptime(date, "%Y-%m-%d").date() < dt.today():
                return Response({'detail': 'please provide a valid date'}, status=status.HTTP_400_BAD_REQUEST)

            doc_profile = get_object_or_404(DoctorProfile, pk=doc_pk)
            doc_profile.appointment_set.create(date=date)
            return Response({'detail': 'date has be successfully blocked for future appoinments'}, status=status.HTTP_200_OK)
        except json.decoder.JSONDecodeError as err:
            return Response({'detail': 'unable to process payload body'},
            status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)
            return Response({'detail': 'internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UnBlockAppointMentDate(APIView):

    def post(self, req, doc_pk=None):
        try:
            data = json.loads(req.body)
            date = data["canceled_date"]
            doc_profile = get_object_or_404(DoctorProfile, pk=doc_pk)
            appointment = doc_profile.appointment_set.get(date=date)
            appointment.delete()
            return Response({'detail': 'date has be successfully unblocked to allow future appoinments'}, status=status.HTTP_200_OK)
        except json.decoder.JSONDecodeError as err:
            return Response({'detail': 'unable to process payload body'},
            status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)
            return Response({'detail': 'internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
