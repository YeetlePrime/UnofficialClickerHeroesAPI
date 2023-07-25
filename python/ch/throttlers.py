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
import logging
from time import process_time

LOG = logging.getLogger(__name__)



class UnlimitedThrottler:
    """ Throttler with unlimited frequency.
    """
    __slots__ = (
        "__lock"
    )

    def __init__(self):
        self.__lock = asyncio.Lock()

    async def __aenter__(self):
        async with self.__lock:
            return self
    
    async def __aexit__(self, exception_type, exception, traceback):
        pass


class BasicThrottler:
    """ Standard throttler. 
    Throttles for requests that are faster than the provided frequency.
    """
    __slots__ = (
        "__sleep_time",
        "__last_run",
        "__lock"
    )

    def __init__(self, frequency):
        self.__sleep_time = 1/frequency
        self.__last_run = None
        self.__lock = asyncio.Lock()

    async def __aenter__(self):
        async with self.__lock:
            if self.__last_run:
                difference = process_time() - self.__last_run
                remaining_sleep_time = self.__sleep_time - difference
                if remaining_sleep_time > 0:
                    LOG.debug(f"Request throttled. Sleeping for {remaining_sleep_time} seconds.")
                    await asyncio.sleep(remaining_sleep_time)
                
            self.__last_run = process_time()
            return self
        
    async def __aexit__(self, exception_type, exception, traceback):
        pass