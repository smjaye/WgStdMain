import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class WeGoStudyAppPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_main_we_go_study_app():
        methods.setUp()
        methods.log_in()
        methods.schools()
        methods.filter_by_study()
        methods.filter_by_city()
        methods.filter_by_province()
        methods.filter_by_program()
        methods.my_we_go_study()
        methods.commissions()
        methods.view_application_list()
        methods.log_out()
        methods.tearDown()