import unittest

from gitvtag.Git import Git


class TestTags(unittest.TestCase):
  def setUp(self):
    self.git= Git()

  def test_increment(self):
    self.assertEqual(self.git.increment_tag("v1"), "v2")
    self.assertEqual(self.git.increment_tag("v0.1"), "v0.2")
    self.assertEqual(self.git.increment_tag("v15.1-rc"), "v15.2-rc")
    self.assertEqual(self.git.increment_tag("v2.3.4-beta5"), "v2.3.4-beta6")
    with  self.assertRaises(ValueError) as dummy:
      self.git.increment_tag("vOne-beta-five")

  def test_last_tag(self):
    pass  # TODO


if __name__ == "__main__":
  unittest.main()
