from unittest import TestCase

from core.Config import Config


class TestConfig(TestCase):
    def test_get_by_key(self):
        data = Config.get_by_key("db")
        print(data)
        self.assertTrue(data is not None)

    def test_get_module_tree(self):
        data = Config.get_module_tree()
        print(data)
