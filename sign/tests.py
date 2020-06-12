from django.test import TestCase
from sign.models import Event,Guest

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,
                             address='shenzhen',start_time='2020-6-15 15:00:00')

        Guest.objects.create(id=1,event_id=1,realname='马化腾',phone='15300015522',
                             email='mahuat@mail.com',sign=False)


    def test_event_models(self):
        result = Event.objects.get(name)
