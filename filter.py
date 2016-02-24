import unittest

from new_format import apply_filter


class test_apply_filter(unittest.TestCase):

  def setUp(self):
    pass
  def tearDown(self):
    pass
def test_filter_by_name(self):
      self.assertEqual(apply_filter(1),"ether proto 0x88B8")
      self.assertEqual(apply_filter(2),"tcp port 102")
      self.assertEqual(apply_filter(3),"ether proto 0x88BA")
      
if __name__ == '__main__':
unittest.main()
