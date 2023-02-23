
from django.test import TestCase
import pytest

from .components.authentification import Authentification
from .components.authorisation import Authorisation


# Create your tests here.

"""Testing module registration.py"""
def test_one_positive():
    auth = Authentification()
