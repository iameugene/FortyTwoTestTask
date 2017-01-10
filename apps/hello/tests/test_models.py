from django.test import TestCase

from apps.hello.models import ContactDetail


class ContactDetailTest(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        self.contact_detail = {
            "first_name": "Yauhen",
            "last_name": "Alkhouski",
            "birth_day": "1976-11-20",
            "bio": "some bio information",
            "email": "zzreklama@gmail.com",
            "skype": "i.eugene",
            "jabber": "iameugene@42cc.co",
            "other_contacts": "some other contact"
        }

    def test_save_contact(self):
        """
        model should save contact detail into DB
        """
        cd = ContactDetail.objects.last()
        self.assertTrue(isinstance(cd, ContactDetail))
        self.assertEqual(ContactDetail.objects.count(), 1)
        self.assertEqual(cd.email.encode(),
                         self.contact_detail['email'])
