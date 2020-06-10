"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import redu
import unittest

class Test(unittest.TestCase):
    def test_search(self):
        for e in redu.get_elements_by_keywork("raedt"):
            print (e)
        #self.assertEqual(0,1)

    def test_get_preview(self):
        df=redu.get_preview("11303/8738/6/OABerlin2017_data_repositories.csv")
        print(df.head())
        #self.assertEqual(0,1)

    def test_dataset(self):
        df=redu.get_dataset("11303/8738/6/OABerlin2017_data_repositories.csv")
        df
        return True
