import time
from src.common.models.mobiles import Mobiles
from src.common.libraries.constants import *
from src.api.v1.serializers.mobileserializer import MobileSerializer
class MobileLib():

    def get_mobiles(self, mobilename):
        print mobilename
        try:
            mobile = mobilename['u']
            mobiles = Mobiles.objects.filter('mobile_name')
        except Exception as e:
            mobiles = Mobiles.objects.all()

        response = dict()
        count = 0

        for mobile in mobiles:
            count += 1
            response[count] = MobileSerializer(mobile).data
            if count > 101:
                return response


    def add_mobiles(self, mobilelist):

        try:
            for mobile in mobilelist:
                selected = mobilelist[mobile]
                selected[KEY_ADEEDON] = time.time()
                selected[KEY_LINK] = selected[KEY_LINK].replace('.php','.json')
                Mobiles.objects.create(**selected)

        except Exception as e:
            print e

        return "Mobiles Added"