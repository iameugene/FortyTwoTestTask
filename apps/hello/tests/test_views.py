from django.test import TestCase
from django.core.urlresolvers import reverse


class ContactDetailTest(TestCase):
    def setUp(self):
        self.contact_detail = {
            "first_name": "Yauhen",
            "last_name": "Alkhouski",
            "birth_day": "1976-11-20",
            "bio": "some bio information",
            "email": "zzreklama@gmail.com",
            "skype": "i.eugene",
            "jabber": "iameugene@42cc.co",
            "other_contacts": "some other contact",
        }

    def test_returns_correct_template(self):
        """
        The view should return correct template
        """
        response = self.client.get(reverse('hello:contact_detail'))
        self.assertTemplateUsed(response, 'hello/contact_detail.html')

    def test_returns_correct_data(self):
        """
        Context should contain correct data passed by view
        """
        response = self.client.get(reverse('hello:contact_detail'))
        self.assertEqual(response.context['cd_data'], self.contact_detail)

    def test_template_render_correct(self):
        """
        Template should correct use context

        """
        response = self.client.get(reverse('hello:contact_detail'))
        self.assertContains(response, 'zzreklama@gmail.com', count=1)
