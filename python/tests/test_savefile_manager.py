import unittest

from ch import decode_save_data, encode_save_data

import json

class TestSavefileManager(unittest.TestCase):
    def test_encoder(self):
        data_json = {"test": True}
        data_str = "7a990d405d2c6fb93aa8fbb0ec1a3b23eJyrVipJLS5RslIoKSpNrQUAJPMFFw=="
        self.assertEqual(encode_save_data(data_json), data_str)

    def test_decoder(self):
        data_json = {"test": True}
        data_str = "7a990d405d2c6fb93aa8fbb0ec1a3b23eJyrVipJLS5RslIoKSpNrQUAJPMFFw=="
        self.assertEqual(decode_save_data(data_str), data_json)

    def test_revert(self):
        data_json = {"test": True}
        self.assertEqual(data_json, decode_save_data(encode_save_data(data_json)))

        data_str = "7a990d405d2c6fb93aa8fbb0ec1a3b23eJyrVipJLS5RslIoKSpNrQUAJPMFFw=="
        self.assertEqual(data_str, encode_save_data(decode_save_data(data_str)))


if __name__ == '__main__':
    unittest.main()