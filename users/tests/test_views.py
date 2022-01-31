from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized


def custom_name_func(testcase_func, param_num, param):
    return "%s_%s" % (
        testcase_func.__name__,
        parameterized.to_safe_name(param.args[4]),
    )


class RegisterViewTest(TestCase):
    def test_register_get(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_post_valid(self):
        response = self.client.post(reverse('users:register'),
                                    data={
                                        'username': 'username',
                                        'email': 'email@mail.com',
                                        'password1': 'password',
                                        'password2': 'password'
                                    })
        self.assertRedirects(response, reverse('store:index'))

    @parameterized.expand([('abcd*', 'email@mail.com', 'password', 'password', 'username', 'Username is invalid'),
                           ('abcd', 'mail.com', 'password', 'password', 'email', ['Enter a valid email address.',
                                                                                  'Email is invalid']),
                           ('abcd', 'email@mail.com', 'passwor', 'passwor', 'password2',
                            'This password is too short. It must contain at least 8 characters.'),
                           ('abcd', 'email@mail.com', 'password', 'password', 'first_name', 'First name is invalid',
                            'Aaa__'),
                           ('abcd', 'email@mail.com', 'password', 'password', 'last_name', 'Last name is invalid',
                            '', 'Aaa__'),
                           ], name_func=custom_name_func)
    def test_register_post_invalid(self, username, email, password1, password2, wrong_field_name, error,
                                   first_name='', last_name='', profile_pic=''):
        response = self.client.post(reverse('users:register'),
                                    data={
                                        'username': username,
                                        'email': email,
                                        'password1': password1,
                                        'password2': password2,
                                        'first_name': first_name,
                                        'last_name': last_name,
                                        'profile_pic': profile_pic,
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', wrong_field_name, error)

    def test_register_template(self):
        response = self.client.get(reverse('users:register'))
        self.assertTemplateUsed(response, 'users/register.html')
