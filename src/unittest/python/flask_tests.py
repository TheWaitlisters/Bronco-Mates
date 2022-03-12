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
FAVORITES = "/favorites"

'''
Code if you need to check status of a response.
Warning will pop up before the unit test displays
what happened in the assertion.

    response = self.client.post(website,
            data = { ... }
    status = response.status
    logging.warning("Status code: " + status)
'''


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    '''
        Tests for a missing piece of information
        The first couple tests are to test if there is a
        piece of required information missing. The
        rest will assume that required information is given
    '''
    def test_account_settings_given_all_defaults(self):
        response = self.client.post(ACCOUNT_SETTINGS,
            data = { "username" : "username1",
                     "password" : "password1",
                     "phoneNumber" : "",
                     "email" : "",
                     "age" : "",
                     "gender" : "",
                     "standing" : "",
                     "major" : "",
                     "minor" : "",
                     "smoker" : "",
                     "pets" : "",
                     "budget" : "",
                     "children" : "",
                     "ocupation" : "",
                     "mSchedule1" : "",
                     "mSchedule2" : "",
                     "tSchedule1" : "",
                     "tSchedule2" : "",
                     "wSchedule1" : "",
                     "wSchedule2" : "",
                     "thSchedule1" : "",
                     "thSchedule2" : "",
                     "fSchedule1" : "",
                     "fSchedule2" : "",
                     "satSchedule1" : "",
                     "satSchedule2" : "",
                     "sunSchedule1" : "",
                     "sunSchedule2" : "",
                     "moveDate" : "",
                     "bio" : ""
                     })
        assert response.status_code == 302

    def test_account_settings_given_all(self):
        response = self.client.post(ACCOUNT_SETTINGS,
            data = { "username" : "user1",
                     "password" : "password1",
                     "phoneNumber" : "123-456-7890",
                     "email" : "email@email.com",
                     "age" : "22",
                     "gender" : "male",
                     "standing" : "Prefer not to disclose",
                     "major" : "Computer",
                     "minor" : "Science",
                     "smoker" : "False",
                     "pets" : "0",
                     "budget" : "20.0",
                     "children" : "0",
                     "ocupation" : "Student",
                     "mSchedule1" : "08:00",
                     "mSchedule2" : "18:00",
                     "tSchedule1" : "",
                     "tSchedule2" : "",
                     "wSchedule1" : "",
                     "wSchedule2" : "",
                     "thSchedule1" : "",
                     "thSchedule2" : "",
                     "fSchedule1" : "",
                     "fSchedule2" : "",
                     "satSchedule1" : "",
                     "satSchedule2" : "",
                     "sunSchedule1" : "08:00",
                     "sunSchedule2" : "18:00",
                     "moveDate" : "2022-02-02",
                     "bio" : "This is a bio"
                     })
        assert response.status_code == 302

    # Status code: 200
    # When missing password, warning message is flashed
    # post method works, but never redirected
    def test_account_settings_missing_password(self):
        response = self.client.post(ACCOUNT_SETTINGS,
            data = { "username" : "username1",
                     "password" : "",
                     "phoneNumber" : "",
                     "email" : "",
                     "age" : "",
                     "gender" : "",
                     "standing" : "",
                     "major" : "",
                     "minor" : "",
                     "smoker" : "",
                     "pets" : "",
                     "budget" : "",
                     "children" : "",
                     "ocupation" : "",
                     "mSchedule1" : "",
                     "mSchedule2" : "",
                     "tSchedule1" : "",
                     "tSchedule2" : "",
                     "wSchedule1" : "",
                     "wSchedule2" : "",
                     "thSchedule1" : "",
                     "thSchedule2" : "",
                     "fSchedule1" : "",
                     "fSchedule2" : "",
                     "satSchedule1" : "",
                     "satSchedule2" : "",
                     "sunSchedule1" : "",
                     "sunSchedule2" : "",
                     "moveDate" : "",
                     "bio" : ""
                     })
        assert response.status_code == 200

    # Status code: 200
    # When missing username, warning message is flashed
    # post method works, but never redirected
    def test_account_settings_missing_password(self):
        response = self.client.post(ACCOUNT_SETTINGS,
            data = { "username" : "",
                     "password" : "password1",
                     "phoneNumber" : "",
                     "email" : "",
                     "age" : "",
                     "gender" : "",
                     "standing" : "",
                     "major" : "",
                     "minor" : "",
                     "smoker" : "",
                     "pets" : "",
                     "budget" : "",
                     "children" : "",
                     "ocupation" : "",
                     "mSchedule1" : "",
                     "mSchedule2" : "",
                     "tSchedule1" : "",
                     "tSchedule2" : "",
                     "wSchedule1" : "",
                     "wSchedule2" : "",
                     "thSchedule1" : "",
                     "thSchedule2" : "",
                     "fSchedule1" : "",
                     "fSchedule2" : "",
                     "satSchedule1" : "",
                     "satSchedule2" : "",
                     "sunSchedule1" : "",
                     "sunSchedule2" : "",
                     "moveDate" : "",
                     "bio" : ""
                     })
        assert response.status_code == 200

    def test_check_urls(self):
        response = self.client.get(HOME_PAGE)
        assert response.status_code == 200
        response = self.client.get(HELLO)
        assert response.status_code == 200
        response = self.client.get(DATABASE_TEST)
        assert response.status_code == 200
        response = self.client.get(CREATE_LISTING)
        assert response.status_code == 200
        response = self.client.get(FAVORITES)
        assert response.status_code == 200

    '''
        Test for getting username and password from login page
    '''
    def login_data_test(self):
        response = self.client.get(LOGIN)
        # 302 == login data successfully recieved
        assert response.status_code == 302
    
