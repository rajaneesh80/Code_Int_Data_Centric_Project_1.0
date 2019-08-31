from datetime import datetime, timedelta
import unittest


from recipe_app import create_app, db
from recipe_app.models import User, RecipePost
from flask_login import login_user, current_user, logout_user, login_required
from recipe_app.users.views import register, login, logout, account, user_recipies, \
    reset_password_request, reset_password

from config import Config



class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None

############################################################
class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan', email ="arti@arti.com", password ="arti" )
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
