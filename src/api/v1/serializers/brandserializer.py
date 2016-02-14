from src.api.v1.serializers.dynamicfieldmodelserializer import DynamicFieldsModelSerializer
from src.common.libraries.constants import *
from src.common.models import Brands

class BrandSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Brands
        fields = (
            KEY_BRAND_ID,
            KEY_BRAND_NAME,
            KEY_BRAND_IMAGE,
            KEY_BRAND_URL,
            KEY_BRAND_DES,
            KEY_ADEEDON
            )

