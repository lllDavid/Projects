from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

StoreUser = get_user_model()


class StoreUserModelTestCase(TestCase):

    def setUp(self):
        self.user = StoreUser.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='securepassword123',
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            shipping_address='123 Test Lane'
        )
        self.superuser = StoreUser.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='adminpassword'
        )

    def test_user_creation(self):
        """
        Verify a regular user is created with the correct fields.
        """
        user = StoreUser.objects.get(email='testuser@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('securepassword123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser_creation(self):
        """
        Verify that a superuser has staff and superuser privileges.
        """
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    def test_email_required(self):
        """
        Ensure that creating a user without email raises a ValueError.
        """
        with self.assertRaisesMessage(ValueError, 'The Email field must be set'):
            StoreUser.objects.create_user(email=None, username='nouser', password='pass')

    def test_unique_email_constraint(self):
        """
        Ensure duplicate email creation raises IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            StoreUser.objects.create_user(
                email='testuser@example.com',
                username='anotheruser',
                password='password'
            )

    def test_unique_username_constraint(self):
        """
        Ensure duplicate username creation raises IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            StoreUser.objects.create_user(
                email='another@example.com',
                username='testuser',
                password='password'
            )

    def test_str_method(self):
        """
        The __str__ method should return the user's email.
        """
        self.assertEqual(str(self.user), 'testuser@example.com')

    def test_get_full_name(self):
        """
        get_full_name should return a string combining first and last name.
        """
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_get_short_name(self):
        """
        get_short_name should return the user's first name.
        """
        self.assertEqual(self.user.get_short_name(), 'Test')

    def test_default_values(self):
        """
        Fields like is_active and date_joined should be set by default.
        """
        user = StoreUser.objects.get(email='testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.date_joined)