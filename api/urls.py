from django.urls import path,include
from rest_framework import routers
from . import viewsets as vs
from .views import BlockAppointMentDate, UnBlockAppointMentDate, PlaceAppointMent

router = routers.SimpleRouter()

router.register("doctor_profile", vs.DoctorViewSet, basename="doctor-profile")
router.register("patient_profile", vs.PatientViewSet, basename="patient-profile")

urlpatterns = [
    path("create_appointment/<int:appointment_pk>/", PlaceAppointMent.as_view(), name="create-appointment"),
    path("block_appointment/<int:doc_pk>/", BlockAppointMentDate.as_view(), name="block-appointment-date"),
    path("unblock_appointment/<int:doc_pk>/", UnBlockAppointMentDate.as_view(), name="unblock-appointment-date"),
    path("", include(router.urls)),
]