from django.db import models
from src.common.libraries.constants import *

class Mobiles(models.Model):
    mobile_id       = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    image           = models.CharField(max_length=MAX_URL_LENGTH)
    filejson        = models.CharField(max_length=MAX_URL_LENGTH)
    des             = models.CharField(max_length=MAX_DES_LENGTH, default="Not Available")
    launched        = models.DecimalField(max_digits=6, decimal_places=2)
    addedon         = models.DecimalField(max_digits=20, decimal_places=6)

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        return super(Mobiles, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.mobile_id

    class Meta:
        db_table = 'gomobi_mobiles'
        app_label = 'common'