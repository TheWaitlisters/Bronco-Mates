from mockito import mock, verify
import unittest
import logging

from app import *

HOME_PAGE = "/"
HELLO = "/hello"
DATABASE_TEST = "/databasetest"
ACCOUNT_SETTINGS = "/accountsettings"
CREATE_LISTING = "/createlisting"
LOGIN = '/login'

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    '''
        Test for receiving data properly from account settings
    '''
    def test_account_settings_full_data(self):
        size = len(messages)
        response = self.client.post(ACCOUNT_SETTINGS, 
            data = { "username" : "testname1",
                     "email" : "testemail@email",
                     "phoneNumber" : "714714714",
                     "standing" : "Freshman",
                     "major" : "CS",
                     "minor" : "Math",
                     "addInfo": "..."}
        )
        # status = response.status
        # logging.warning("status code: " + status)

        # 302 = respones has been redirected
        assert response.status_code == 302
        # size has increased
        assert size == len(messages) - 1

    '''
        Test for if one of the required fields is missing
        In this instance: email
    '''
    def test_account_settings_missing_email(self):
        response = self.client.post(ACCOUNT_SETTINGS, 
            data = { "username" : "testname1" })
        # 400 = bad request
        assert response.status_code == 400

    '''
        Test for if one of the required fields is missing
        In this instance: username
    '''
    def test_account_settings_missing_user(self):
        response = self.client.post(ACCOUNT_SETTINGS, 
            data = { "email" : "email1" })
        # 400 = bad request
        assert response.status_code == 400
    
    def test_check_urls(self):
        response = self.client.get(HOME_PAGE)
        assert response.status_code == 200
        response = self.client.get(HELLO)
        assert response.status_code == 200
        response = self.client.get(DATABASE_TEST)
        assert response.status_code == 200
        response = self.client.get(CREATE_LISTING)
        assert response.status_code == 200

    '''
        Test for getting username and password from login page
    '''
    def login_data_test(self):
        response = self.client.get(LOGIN)
        # 302 == login data successfully recieved
        assert response.status_code == 302
    
    