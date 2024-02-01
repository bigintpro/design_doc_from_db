import json
import unittest
import attrs

from db.oracle.OracleDbService import OracleDbService


class TestOracleDbService(unittest.TestCase):
    def test_get_all_table_names(self):
        service = OracleDbService()

        list = service.get_all_table_names("CYY")
        print(list)

        self.assertIsNotNone(list)


    def test_get_all_table_beans(self):
        service = OracleDbService()

        list = service.get_all_table_beans("CYY")
        # print(list)
        print(json.dumps(list, default=lambda o: o.__dict__, ensure_ascii=False))
        self.assertIsNotNone(list)


if __name__ == '__main__':
    unittest.main()
