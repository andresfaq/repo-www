from django.test import TestCase
from django.contrib.auth.models import User
import autofixture


class UserTestCase(TestCase):
    def setUp(self):
        usuarios = autofixture.create('auth.User', 10, field_values={'is_superuser': True})
        for x in usuarios:
            User.objects._insert(x)


