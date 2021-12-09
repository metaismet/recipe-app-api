from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating new user"""
        email = 'test@eagle.mk'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_model_normalized(self):
        """Test the email address is normalized"""
        email = 'test@EAGLE.MK'
        user = get_user_model().objects.create_user(email, 'asdfa345345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_user(self):
        """Test creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asdfasd123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@eagle.mk'
            'asdfqsdaf123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
