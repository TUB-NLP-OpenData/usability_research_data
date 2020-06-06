"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import redu
import unittest

class Test(unittest.TestCase):
    def test_search(self):
        for e in redu.search("gps"):
            print (e)
        #self.assertEqual(0,1)

    def test_get_preview(self):
        df=redu.get_preview("001")
        df.head()
        #self.assertEqual(0,1)

    def test_dataset(self):
        df=redu.get_dataset("001")
        df.head()
        return True
