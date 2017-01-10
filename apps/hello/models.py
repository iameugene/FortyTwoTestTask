from django.db import models


class ContactDetail(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_day = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=32)
    skype = models.CharField(max_length=128)
    jabber = models.CharField(max_length=128)
    other_contacts = models.TextField()

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
