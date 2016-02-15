from src.api.v1.serializers.dynamicfieldmodelserializer import DynamicFieldsModelSerializer
from src.common.libraries.constants import *
from src.common.models import Mobiles

class MobileSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Mobiles
        fields = (
            KEY_MOBILE_ID,
            KEY_BRAND_NAME,
            KEY_MOBILE_NAME,
            KEY_LINK,
            KEY_IMAGE,
            KEY_SHORT_DES,
            KEY_ADEEDON
            )

