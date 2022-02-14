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

  def test_bytes(self):
    report= b'v0.2-8-gb661887-\n'
    split_report= report.decode('utf-8').split('-')
    self.assertEqual(split_report, ['v0.2', '8', 'gb661887', '\n'])


if __name__ == "__main__":
  unittest.main()
