from django.db import models
from src.common.libraries.constants import *
import uuid

class BrandsManager(models.Manager):
    def generate_brandid(self):
        return str(uuid.uuid4())

class Brands(models.Model):
    brand_id        = models.CharField(max_length=UID_LENGTH, primary_key=True, editable=False)
    brand_name      = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    brand_image     = models.CharField(max_length=MAX_URL_LENGTH)
    brand_url       = models.CharField(max_length=MAX_URL_LENGTH)
    brand_des       = models.CharField(max_length=MAX_DES_LENGTH, default="Not Available")
    total_mobiles   = models.IntegerField()
    addedon         = models.DecimalField(max_digits=20, decimal_places=6)
    objects         = BrandsManager()

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        if not self.brand_id:
            self.brand_id = Brands.objects.generate_brandid()

        return super(Brands, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.brand_id

    class Meta:
        db_table = 'mobi_brands'
        app_label = 'common'