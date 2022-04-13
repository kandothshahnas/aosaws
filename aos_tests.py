import unittest
import aos_methods as methods


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user():
        methods.setup()
        methods.validate_dash_board()
        methods.create_new_account()
        methods.check_username_display()
        methods.logout()
        methods.login()
        methods.check_username_display()
        methods.check_out_shopping_cart()
        methods.delete_order()
        methods.delete_user()
        methods.teardown()
