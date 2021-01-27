from datetime import date
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from api.models import User, DoctorProfile, PatientProfile


class APIViewsTestCase(APITestCase):

    fixtures = ["user.json", "patient.json", "doctor.json"]
    
    def test_book_appointment_with_past_dates(self):
        payload = {
            "appointment_date": date(2020, 2, 7).strftime("%Y-%m-%d"),
            "doc_id": 1 
        } 
        res = self.client.post("/api/create_appointment/1/", data=payload, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertContains(res, "an appointment cannot be scheduled at this date", status_code=400)

    def test_book_appointment_with_available_date(self):
        payload = {
            "appointment_date": date(2021, 2, 7).strftime("%Y-%m-%d"),
            "doc_id": 1 
        } 
        res = self.client.post("/api/create_appointment/1/", data=payload, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertContains(res, "appointment has been successfully scheduled", status_code=201)
       
    def test_book_appointment_with_unavailable_date(self):
        patient_profile = PatientProfile.objects.get(pk=1)
        patient_profile.appointment = None
        patient_profile.save()
        doc_profile = DoctorProfile.objects.get(pk=1)
        blocked_appointment_dt = doc_profile.appointment_set.create(date=date(2021, 5, 10))
        payload = {
            "appointment_date": date(2021, 5, 10).strftime("%Y-%m-%d"),
            "doc_id": 1 
        } 
        res = self.client.post("/api/create_appointment/1/", data=payload, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertContains(res, "an appointment cannot be scheduled at this date", status_code=400)
        
    def test_block_appointment_date(self):
        """
            Test for operation that lets a doctor cancel a specific date for any appoinment
        """
        payload = {
            "cancel_date": date(2021, 10, 10).strftime("%Y-%m-%d")
        }
        res = self.client.post("/api/block_appointment/1/", data=payload, format="json")
        self.assertEqual(res.status_code, 200)

    def test_unblock_appointment_date(self):
        """
            Test for operation that lets a doctor unblock a previously canceled specific date for future appoinment
        """
        doc_profile = DoctorProfile.objects.get(pk=1)
        blocked_appointment_dt = doc_profile.appointment_set.create(date=date(2021, 12, 12))
        payload = {
            "canceled_date": date(2021, 12, 12).strftime("%Y-%m-%d")
        }
        res = self.client.post("/api/unblock_appointment/1/", data=payload, format="json")
        self.assertEqual(res.status_code, 200)