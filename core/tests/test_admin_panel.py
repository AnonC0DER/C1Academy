from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminPanelTests(TestCase):
    '''Test admin panel'''

    # setUp() function runs before every test
    def setUp(self):
        '''Create a superuser and a student user'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'testsuperuser@gmail.com',
            username = 'testuser',
            password = 'testpass123@',
            first_name = 'Test',
            last_name = 'User',
            user_post = 'superuser'
        )
        # user must be logged in
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = 'testStudent@gmail.com',
            username = 'testStudent',
            password = 'testpass123@',
            first_name = 'Test',
            last_name = 'Student',
            user_post = 'student'
        )

    def test_users_listed(self):
        '''Test users are listed and visible for superuser'''
        # The url that this variable generates : /admin/core/account/
        url = reverse('admin:core_account_changelist')
        response = self.client.get(url)
        
        # Check there are user's details or not
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)
        self.assertContains(response, self.user.user_post)

    def test_user_change_page(self):
        '''Test the user edit page works just fine'''
        # url = admin/core/account/ID/change/
        url = reverse('admin:core_account_change', args=[self.user.id])
        # Create request
        response = self.client.get(url)

        # Check url response status code
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        '''Test the user create page works'''
        # url = admin/core/account/add/
        url = reverse('admin:core_account_add')
        # Create request
        response = self.client.get(url)

        # Check url response status code
        self.assertEqual(response.status_code, 200)