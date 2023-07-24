"""
MIT License

Copyright (c) 2023 YeetlePrime

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import base64
import zlib

def decode_save_data(save_data:str) -> json:
    """ Decodes an encrypted Clicker Heroes savefile.

    Returns the unencrypted save data as json object.
    ...
    Parameters
    ----------
    save_data:str
        encrypted save data that should be decoded
    """

    # remove the first 32 characters. they hold no information
    save_data = save_data[slice(32, len(save_data))]

    # decode the save data. data is base64 encoded.
    save_data = base64.b64decode(save_data)

    # decompress the save data.
    save_data = zlib.decompress(save_data)

    # return decoded save data as json object
    return json.loads(save_data)

def encode_save_data(save_data:json) -> str:
    """ Encodes unencrypted Clicker Heroes save data in json representation.

    ...
    Parameters
    ----------
    save_data:json
        unencrypted save data that should get encoded
    """

    # convert json to str
    save_data = json.dumps(save_data)

    # convert str to bytes
    save_data = str.encode(save_data)

    # compress data
    save_data = zlib.compress(save_data)

    # encode data with base64
    save_data = base64.b64encode(save_data)

    # convert encoded bytes into encoded str
    save_data = bytes.decode(save_data)

    # add default prefix data
    save_data = "7a990d405d2c6fb93aa8fbb0ec1a3b23" + save_data

    return save_data