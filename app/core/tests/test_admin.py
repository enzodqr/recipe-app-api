from django.test import TestCase, Client
# Client allows us to make test request
from django.contrib.auth import get_user_model
from django.urls import reverse  # Generate urls for the django admin


class AdminSiteTest(TestCase):

    def setUp(self):
        """ A setup functions is a function that is ran before every test"""

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        """Check that our response contains a certain item"""

    def test_user_change_page(self):
        """Test that the user page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # Make a dinamic page url for every user
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
