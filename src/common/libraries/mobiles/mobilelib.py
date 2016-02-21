import time
from collections import OrderedDict
from src.common.models.mobiles import Mobiles
from src.common.libraries.constants import *
from src.api.v1.serializers.mobileserializer import MobileSerializer

class MobileLib():

    def get_mobiles(self, queryobj):
        try:
            print queryobj
            page = 1
            if "page" in queryobj:
                page = int(queryobj['page'])

            endlist = page * 20
            startlist = endlist - 19


            if "u" in queryobj:
                searchfor = "%" + queryobj['u'].lower() + "%"
                total = Mobiles.objects.filter(name__like = searchfor).count()
                mobiles = Mobiles.objects.filter(name__like = searchfor).order_by('-launched')

            else :
                total = Mobiles.objects.all().count()
                mobiles = Mobiles.objects.all().order_by('-mobile_id')

            response = OrderedDict()
            response['total'] = total
            response['data'] = OrderedDict()
            count = 0
            for mobile in mobiles:
                count += 1
                if count >= startlist and count <=endlist:
                    selected = MobileSerializer(mobile).data
                    selected[KEY_SHORT_DES] = selected[KEY_SHORT_DES][0:80] + "....."
                    response['data'][selected[KEY_MOBILE_ID]] = selected

            return response

        except Exception as e:
            print e

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

    def get_mobile(self, mobilename):
        try:
            file = mobilename['u'].lower().replace('[[plus]]','+')+'.json'
            print file
            mobiles = Mobiles.objects.all().filter(filejson=file)
            print mobiles[0]
        except Exception as e:
            print e
            return None
        response = dict()
        selected = MobileSerializer(mobiles[0]).data
        selected[KEY_LAUNCHED] = self.getdate(selected[KEY_LAUNCHED])
        response = selected
        return response

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