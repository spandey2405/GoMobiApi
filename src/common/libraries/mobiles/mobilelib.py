import time
from collections import OrderedDict
from src.common.models.mobiles import Mobiles
from src.common.libraries.constants import *
from src.api.v1.serializers.mobileserializer import MobileSerializer
class MobileLib():

    def get_mobiles(self, mobilename):
        try:
            name = mobilename['u'].lower()
            try:
                total = int(mobilename['total'])
                mobiles = Mobiles.objects.all().filter(name__contains=name).order_by('-launched')[:total]
            except:
                mobiles = Mobiles.objects.all().filter(name__contains=name).order_by('-launched')

        except:

            try:
                total = int(mobilename['total'])
                mobiles = Mobiles.objects.all().order_by('-launched')[:total]
            except:
                mobiles = Mobiles.objects.all().order_by('-launched')

        response = OrderedDict()
        count = 0
        response["data"] = OrderedDict()

        for mobile in mobiles:
            count += 1
            selected = MobileSerializer(mobile).data
            selected[KEY_LAUNCHED] = self.getdate(selected[KEY_LAUNCHED])
            response["data"][count] = selected

        response["No Of Mobiles"] = count
        return response

    def add_mobiles(self, mobilelist):

        try:
            for mobile in mobilelist:
                selected = mobilelist[mobile]
                selected[KEY_ADEEDON] = time.time()
                selected[KEY_MOBILE_NAME] = selected[KEY_MOBILE_NAME].lower()
                Mobiles.objects.create(**selected)

        except Exception as e:
            print e

        return "Mobiles Added"

    def getdate(self, date):
        m = {
            1:'Jan',
            2:'Feb',
            3:'Mar',
            4:'Apr',
            5:'May',
            6:'Jun',
            7:'Jul',
            8:'Aug',
            9:'Sep',
            10:'Oct',
            11:'Nov',
            12:'Dec'
        }
        date = str(date).split('.')
        year = date[0]
        month = int(date[1])
        if month > 0:
            month = m[month]
            return "{0}, {1}".format(str(year), str(month))
        else:
            return "{0}".format(str(year))

        return None