from src.common.libraries.constants import *
from src.common.models.brands import Brands
import time
class BrandLib():

    def get_grands(self):

        return None

    def add_brand(self, brandlist):

        try:
            for brand in brandlist:
                selected = brandlist[brand]
                image_name = brandlist[brand][KEY_BRAND_IMAGE].split('/')[-1].replace('lg_','mobi_brand_')
                selected[KEY_ADEEDON] = time.time()
                selected[KEY_BRAND_IMAGE] = image_name
                Brands.objects.create(**selected)
            return "Brands Added"
        except Exception as e:
            print e
            return "Some Error Occured"

    def update_brand(self):

        return None

    def del_brand(self):

        return None