

import io
import os
import sys
import uuid

import mock
from PIL import Image
from django.apps import apps
from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile

from utils.abstractions.data_structures.service_response import ServiceResponse
from utils.abstractions.types.error_type import Error

from users.models import SoundHomeUsersAdditionalInfo
from users.models import SoundHomeUsers

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

        self.make_user()
    
    def tearDown(self) -> None:
        del self.test_user
        self.make_user()

    def make_user(self) -> None:
        component = Registration()
        self.test_user = component.create_user(
            email=self.TEST_DATA['email'], 
            password=self.TEST_DATA['password'])


class UserWithSomePotentialData(VirginUser):
    def setUp(self) -> None:
        super().setUp()
        image_content_type = 'png'
        img_good = io.BytesIO()
        Image.new(mode='RGB', size=(999, 999)).save(img_good, format=image_content_type)
        
        img_bad = io.BytesIO()
        Image.new(mode='RGB', size=(1001, 1000)).save(img_bad, format=image_content_type)

        self.mok_img_good = self.mok_InMemoryUploadedFile(
            img=img_good,
            field_name='ImageField',
            file_name='pic'+ f'{uuid.uuid4()}',
            content=image_content_type,
            size=sys.getsizeof(img_good)
        )
        self.mok_img_bad = self.mok_InMemoryUploadedFile(
            img=img_bad,
            field_name='ImageField',
            file_name='pic'+ f'{uuid.uuid4()}',
            content=image_content_type,
            size=sys.getsizeof(img_bad)
        ) 


        self.test_nickname_good = '@JorjoJiovanni'
        self.test_nickname_bad = '@JorjoJi@ovanni'

        self.TEST_DATA.update({
            'test_image_good': self.mok_img_good,
            'test_image_bad': self.mok_img_bad,
            'test_nickname_good': self.test_nickname_good,
            'test_nickname_bad': self.test_nickname_bad,
        })
        self.DO_DELETE = False
    
    @staticmethod
    def mok_InMemoryUploadedFile(
        img, field_name, file_name, content, size, charset=None) -> InMemoryUploadedFile:

        return InMemoryUploadedFile(
            file=img, 
            field_name=field_name,
            name=file_name,
            content_type=content,
            size=size,
            charset=charset)

    def tearDown(self) -> None:
        if self.DO_DELETE:
            os.remove(self.test_user.soundhomeusersadditionalinfo.image.path)
        super().tearDown()


"""Testing module 'database_requests.py'"""


class UserWithSomeDataCases(UserWithSomePotentialData):
    def test_setting_up_account_positive(self) -> None:
        pk = self.test_user.pk
        response = dbq.add_user_ava_and_nickname_end_set_user_active(
            pk=pk, 
            ava=self.TEST_DATA['test_image_good'],
            nickname=self.TEST_DATA['test_nickname_good'])
        
        try:
            self.assertEqual(response, True)
        except Exception as E:
            self.fail(f"{E}")
        else:
            self.DO_DELETE = True

    def test_setting_up_account_negative(self) -> None:
        pk = self.test_user.pk
        response = dbq.add_user_ava_and_nickname_end_set_user_active(
            pk=666, 
            ava=self.TEST_DATA['test_image_bad'],
            nickname=self.TEST_DATA['test_nickname_good'])
        
        try:
            self.assertIsInstance(response, Error)
        except Exception as E:
            self.DO_DELETE = True
            self.fail(f"{E}")
        else:
            pass


class VirginUserCases(VirginUser):
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

    def test_user_own_reviews(self) -> None:
        pk = self.test_user.pk
        rvws = dbq.get_user_own_review_ids(pk=pk)
        
        self.assertEqual(rvws, [])

    def test_user_favourite_reviews(self) -> None:
        pk = self.test_user.pk
        
        rvws = dbq.get_user_favourites_reviews_ids(pk=pk)
        self.assertEqual(rvws, [])


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
    