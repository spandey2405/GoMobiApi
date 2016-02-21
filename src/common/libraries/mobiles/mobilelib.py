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

            startlist = (32 * (page - 1 ))

            if "u" in queryobj:
                print "Object Present"
                searchfor = "%" + queryobj['u'].lower() + "%"
                total = Mobiles.objects.filter(name__like = searchfor).count()
                Query = "SELECT * FROM `gomobi_mobiles` WHERE `name` LIKE '{0}' ORDER BY `gomobi_mobiles`.`mobile_id` DESC LIMIT {1} , 32".format(str(searchfor),str(startlist))
                mobiles = Mobiles.objects.raw(Query)

            else :
                total = Mobiles.objects.all().count()
                Query = "SELECT * FROM `gomobi_mobiles` ORDER BY `gomobi_mobiles`.`mobile_id` DESC LIMIT {0} , 32".format(str(startlist))
                mobiles = Mobiles.objects.raw(Query)

            response = OrderedDict()
            response['total'] = total
            response['data'] = OrderedDict()

            for mobile in mobiles:
                selected = MobileSerializer(mobile).data
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