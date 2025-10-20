import unittest
import sys
from tests.UI_tests.auth import test_gp_auth
from tests.UI_tests.auth import test_gv_auth
from tests.UI_tests.create_order import test_order_creation
from tests.UI_tests.trailer_list import test_open_trailers_list
from tests.UI_tests.vehicle_list import test_open_vehicles_list

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_gp_auth))
    suite.addTest(unittest.makeSuite(test_gv_auth))
    suite.addTest(unittest.makeSuite(test_order_creation))
    suite.addTest(unittest.makeSuite(test_open_vehicles_list))
    suite.addTest(unittest.makeSuite(test_open_trailers_list))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(create_suite())
    sys.exit(1 if result.failures or result.errors else 0)