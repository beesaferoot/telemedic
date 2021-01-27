from django.test import TestCase
from api.models import User, DoctorProfile, PatientProfile

class ModelsTestCase(TestCase):
    # load test data
    fixtures = ["user.json", "patient.json", "doctor.json"]
    def test_user_is_active(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.is_active, True)
    
    def test_doctor_profile_has_valid_user(self):
        doc_profile = DoctorProfile.objects.get(pk=1)
        self.assertNotEquals(doc_profile.user, None)
        
    def test_patient_profile_has_valid_user(self):
        patient_profile = PatientProfile.objects.get(pk=1)
        self.assertNotEquals(patient_profile.user, None)

