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

import asyncio
import json
import logging
import aiohttp
from time import perf_counter

from .throttlers import (
    UnlimitedThrottler,
    BasicThrottler
)
from .errors import (
    CHException,
    HTTPException,
    NotSuccessful
)

LOG = logging.getLogger(__name__)

class HTTPClient:
    """ Client for low-level access to the API.
    Has to be initialized with 'create_session' and closed with 'close'.
    Alternatively use the 'async with' syntax to create a client.
    """

    __slots__ = (
        "__throttler",
        "__session",
        "__timeout"
    )

    def __init__(self, throttler = BasicThrottler(20), timeout = 30.0):
        self.__throttler = throttler
        self.__session = None
        self.__timeout = timeout
        
    async def create_session(self):
        if self.__session == None:
            self.__session = aiohttp.ClientSession(base_url = 'http://ClickerHeroes-SavedGames3-747864888.us-east-1.elb.amazonaws.com', timeout = aiohttp.ClientTimeout(total = self.__timeout))

    async def close(self):
        if self.__session:
            await self.__session.close()
            self.__session = None

    async def __aenter__(self):
        await self.create_session()
        return self

    async def __aexit__(self, exception_type, exception, traceback):
        await self.close()

    async def request(self, endpoint, params = {}):
        try:
            async with self.__throttler:
                timer_start = perf_counter()

                async with self.__session.get(endpoint, params = params) as response:
                    perf = (perf_counter() - timer_start) * 1000
                    log_info = {'method': 'GET', 'url': response.url, 'perf_counter': perf, 'status': response.status}
                    LOG.debug(f'API HTTP Request: {str(log_info)}')

                    data = await response.json(content_type = None, loads = _json_loads)

                    if 200 <= response.status < 300:
                        LOG.debug(f'{response.url} has responded with {data}.')
                        data['endpoint'] = endpoint
                        data['params'] = params
                        return data
                    else:
                        raise HTTPException(response, data)

        except:
            raise
        
    async def find_clan(self, clan_name):
        return await self.request('/clans/findGuild.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0, 'highestZoneReached': 0})
        


def _json_loads(text):
    """ Parses json formatted string to json object.
    """
    text = str(text).replace("\\", "\\\\")

    try:
        text = json.loads(text)
    except:
        raise

    return text