from __future__ import unicode_literals
from django.db import models


class ProfileManager(models.Manager):
    def get_by_google_id(self, search):
        return self.filter(google_id=search).first()

    def get_by_email(self, email):
        return self.filter(user__email=email).first()