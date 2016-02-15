from django.db import models
from src.common.libraries.constants import *
import uuid

class MobilesManager(models.Manager):
    def generate_mobileid(self):
        return str(uuid.uuid4())

class Mobiles(models.Model):
    mobile_id          = models.CharField(max_length=UID_LENGTH, primary_key=True, editable=False)
    brand_name         = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    mobile_name        = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    image              = models.CharField(max_length=MAX_URL_LENGTH)
    link               = models.CharField(max_length=MAX_URL_LENGTH)
    short_des          = models.CharField(max_length=MAX_DES_LENGTH, default="Not Available")
    launch_date        = models.CharField(max_length=200, default='NA')
    addedon            = models.DecimalField(max_digits=20, decimal_places=6)
    objects            = MobilesManager()

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        if not self.mobile_id:
            self.mobile_id = Mobiles.objects.generate_brandid()

        return super(Mobiles, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.mobile_id

    class Meta:
        db_table = 'mobi_mobiles'
        app_label = 'common'