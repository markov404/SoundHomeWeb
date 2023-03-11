
from django.test import TestCase

from utils.abstractions.data_structures.service_response import ServiceResponse
from utils.abstractions.types.error_type import Error

from users.models import SoundHomeUsersAdditionalInfo

from users.components.registration import Registration
from users.components import database_requests as dbq
from users.services.user_data_service import UserBasicDataService

# Create your tests here.

""" Cases """

class VirginUser(TestCase):
    def setUp(self) -> None:

        self.TEST_DATA = {
            'email': 'UsamaBenLaden@yandex.ru',
            'password': 'btufn262osn8F'   
        }

        def _make_user():
            component = Registration()
            self.test_user = component.create_user(
                email=self.TEST_DATA['email'], 
                password=self.TEST_DATA['password'])
        self.make_user = _make_user
        self.make_user()
    
    def tearDown(self) -> None:
        del self.test_user
        self.make_user()


class VirginUser(TestCase):
    def setUp(self) -> None:

        self.TEST_DATA = {
            'email': 'UsamaBenLaden@yandex.ru',
            'password': 'btufn262osn8F'   
        }

        def _make_user():
            component = Registration()
            self.test_user = component.create_user(
                email=self.TEST_DATA['email'], 
                password=self.TEST_DATA['password'])
        self.make_user = _make_user
        self.make_user()
    
    def tearDown(self) -> None:
        del self.test_user
        self.make_user()  


"""Testing module 'database_requests.py'"""

class DataBaseRequestsModuleCase(VirginUser):
    def test_check_active_posititve(self, _result_status: bool = False) -> None:
        pk = self.test_user.pk
        status = dbq.get_user_additional_active_status(pk)
        
        self.assertEqual(status, _result_status)
    
    def test_check_active_negative(self) -> None:
        pk = self.test_user.pk
        status = dbq.get_user_additional_active_status(666)
        
        self.assertIsInstance(status, Error)

    def test_user_email_positive(self) -> None:
        pk = self.test_user.pk
        email = dbq.get_user_email_by_pk(pk)
        
        self.assertEqual(email, self.TEST_DATA['email'])

    def test_user_email_negative(self) -> None:
        pk = self.test_user.pk
        email = dbq.get_user_email_by_pk(666)
        
        self.assertIsInstance(email, Error)

    def test_change_user_active_positive(self) -> None:
        pk = self.test_user.pk
        
        respone = dbq.change_user_active(pk=pk, active=True)
        self.assertIsInstance(respone, SoundHomeUsersAdditionalInfo)
        self.test_check_active_posititve(_result_status=True)
        self.test_change_user_active_negative()

    def test_change_user_active_negative(self) -> None:
        pk = self.test_user.pk
        
        respone = dbq.change_user_active(pk=666, active=True)
        self.assertIsInstance(respone, Error)


"""Testing module 'user_data_service.py'"""

class UserDataServiceTestCase(TestCase):
    def setUp(self):
        email = 'UsamaBenLaden@yandex.ru'
        password = 'btufn262osn8F'

        self.helpful_component = Registration()
        self.test_user = self.helpful_component.create_user(email=email, password=password)

    def tearDown(self) -> None:
        super().tearDown()
        del self.test_service

    def test_positive_getting_basic_user_data(self):
        self.test_service = UserBasicDataService()
        
        pk = self.test_user.pk
        self.test_service._extract_basic_user_data(_id=pk)
        self.assertEqual(
            self.test_service.response.as_one_dictionary(),
            {'email': self.test_user.email})
    
    def test_negative_getting_basic_user_data(self):
        self.test_service = UserBasicDataService()

        self.test_service._extract_basic_user_data(_id=666)
        self.assertEqual(
            self.test_service.response.as_one_dictionary(),
            ServiceResponse().as_one_dictionary()
        )

    def test_positive_getting_basic_user_data(self):
        self.test_service = UserBasicDataService()
        
        pk = self.test_user.pk
        self.test_service._extract_basic_user_data(_id=pk)
        self.assertEqual(
            self.test_service.response.as_one_dictionary(),
                {'email': self.test_user.email})
    