import time
from src.common.models.mobiles import Mobiles
from src.common.libraries.constants import *

class MobileLib():


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