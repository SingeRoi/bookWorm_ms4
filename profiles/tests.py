from django.test import TestCase

# Create your tests here.

class SignupTestCase(TestCase):

    def test_signup(self):
        response = self.client.post('/accounts/signup/', {'email': 'dd@dd.com', 'email2': 'dd@dd.com', \
                                                          'username': 'ddddd', 'password1': 'dddd1234', 'password2': 'dddd1234'})
        self.assertRedirects(response, '/accounts/confirm-email/')


class LoginTestCase(TestCase):

    def test_login(self):
        response = self.client.get('/accounts/login/', {'login': 'aaaaa','password': 'aaaa1234'} )
        self.assertEqual(response.status_code, 200)

