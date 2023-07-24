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
from aiohttp import ClientResponse

class CHException(Exception):
    """ Base exception for ch.py.
    """

class HTTPException(CHException):
    """ Base exception for HTTP request fails.

    Attributes
    ----------
    response:
        :class:'aiohttp.ClientResponse' - The response of the failed HTTP request.

    status:
        :class:'int' - The status code of the HTTP request

    reason:
         :class:'str' - The reason provided by the API.
            This could be an empty string of nothing was given.
        
    message:
        :class'str' - The more detailed message provided by the API.
            This could be an empty string if nothing was given.
    """

    __slots__ = ("response", "status", "message", "reason", "_data")

    def _from_response(self, response, data):
        self.response = response
        self.status = response.status

        if isinstance(data, dict):
            self.reason = data.get("reason", "Unknown")
            self.message = data.get("message")
        elif isinstance(data, str):
            self.reason = data
            self.message = None
        else:
            self.reason = "Unknown"
            self.message = None
        
        fmt = "{0.reason} (status code: {0.status})"
        if self.message:
            fmt += ": {0.message}"
        super().__init__(fmt.format(self))
    
    def __init__(self, response=None, data=None):
        if isinstance(response, ClientResponse):
            self._from_response(response, data)
        else:
            self.response = None
            self.status = 0
            self.reason = None
            self.message = response

            fmt = "Unknown Error Occured: {0}"
            super().__init__(fmt.format(self.message))  