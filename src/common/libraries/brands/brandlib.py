from src.common.libraries.constants import *
from src.common.models.brands import Brands
from src.api.v1.serializers.brandserializer import BrandSerializer
import time
class BrandLib():

    def get_grands(self):

        response = dict()
        brands = Brands.objects.all()
        for brand in brands:
            selected = BrandSerializer(brand).data
            response[selected[KEY_BRAND_ID]] = selected

        return response

    def add_brand(self, brandlist):

        try:
            for brand in brandlist:
                selected = brandlist[brand]
                image_name = brandlist[brand][KEY_BRAND_IMAGE].split('/')[-1].replace('lg_','mobi_brand_')
                selected[KEY_ADEEDON] = time.time()
                selected[KEY_BRAND_URL] = 'brand-' + selected[KEY_BRAND_NAME].replace(' ','-').replace('&','-and-').replace(';','').replace('_','-')
                selected[KEY_BRAND_URL] = selected[KEY_BRAND_URL].lower()[:-1]
                selected[KEY_BRAND_URL] = selected[KEY_BRAND_URL] + '.php'
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