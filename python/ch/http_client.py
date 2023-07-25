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


def _json_loads(text):
    """ Parses json formatted string to json object.
    """
    text = str(text).replace("\\", "\\\\")

    try:
        text = json.loads(text)
    except:
        raise

    return text


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





    # IMPORTANT SECURITY UPDATE --------------------------------------------------------------------------------------------
    # THE FOLLOWING FUNCTIONS HAVE TO BE REVISITED
    async def get_server_version(self):
        return await self.request('/clans/getServerVersion.php')

    async def find_clan(self, clan_name):
        return await self.request('/clans/findGuild.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0, 'highestZoneReached': 0})
        
    async def find_random_clan(self):
        return await self.request('/clans/findGuild.php', {'uid': 0, 'passwordHash': 0, 'highestZoneReached': 0})    
    
    async def get_raid(self, clan_name):
        return await self.request('/clans/getRaid.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0, 'timestamp': -1, 'day': 'today'})
    
    async def get_raid_health(self, clan_name):
        return await self.request('/clans/getTitanHealth.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0, 'day': 'today', 'timestamp': -1})
    
    async def get_new_raid(self, clan_name):
        return await self.request('/clans/getNewRaid.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0, 'day': 'today'})
    
    async def get_new_raid_rewards(self, uid, clan_name):
        return await self.request('/clans/getNewRaidRewards.php', {'guildName': clan_name, 'uid': uid, 'passwordHash': 0, 'lastRaidChecked': 1, 'lastBonusChecked': 1})
    
    async def request_bonus_fight(self, clan_name):
        return await self.request('/clans/requestBonusFight.php', {'guildName': clan_name, 'uid': 0, 'passwordHash': 0})
    
    async def get_clan_info(self, uid, password_hash):
        return await self.request('/clans/getGuildInfo.php', {'uid': uid, 'passwordHash': password_hash})
    
    async def create_clan(self, uid, password_hash, clan_name):
        return await self.request('/clans/createGuild.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def make_join_request(self, uid, password_hash, clan_name):
        return await self.request('/clans/requestToJoinGuild.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def cancel_join_request(self, uid, password_hash, clan_name):
        return await self.request('/clans/cancelGuildRequest.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def update_player(self, uid, password_hash, highest_zone):
        return await self.request('/clans/updatePlayer.php', {'uid': uid, 'passwordHash': password_hash, 'highestZone': highest_zone})
    
    async def get_clan_messages(self, uid, password_hash, clan_name):
        return await self.request('/clans/getGuildMessages.php', {'guildName': clan_name, 'uid': uid, 'passwordHash': password_hash})
    
    async def send_clan_message(self, uid, password_hash, clan_name, message):
        return await self.request('/clans/sendGuildMessage.php', {'guildName': clan_name, 'uid': uid, 'passwordHash': password_hash, 'message': message})

    async def attack_new_raid(self, uid, password_hash, clan_name, damage_dealt, is_bonus_fight = False, level = 1):
        if is_bonus_fight:
            is_bonus_fight = True
        else:
            is_bonus_fight = ''
        return await self.request('/clans/sendNewImmortalDamage.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name, 'damageDone': damage_dealt, 'isBonusFight': is_bonus_fight})
        
    async def leave_clan(self, uid, password_hash, clan_name):
        return await self.request('/clans/leaveGuild.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def kick_clan_member(self, uid, password_hash, uid_to_kick, clan_name):
        return await self.request('/clans/kickGuildMember.php', {'guildMasterUid': uid, 'passwordHash': password_hash,'uidToKick': uid_to_kick, 'guildName': clan_name})
    
    async def accept_join_request(self, uid, password_hash, uid_to_accept, clan_name):
        return await self.request('/clans/acceptGuildRequest.php', {'guildMasterUid': uid, 'passwordHash': password_hash,'uidToAccept': uid_to_accept, 'guildName': clan_name})
    
    async def reject_join_request(self, uid, password_hash, uid_to_reject, clan_name):
        return await self.request('/clans/rejectGuildRequest.php', {'guildMasterUid': uid, 'passwordHash': password_hash,'uidToReject': uid_to_reject, 'guildName': clan_name})
    
    async def disband_clan(self, uid, password_hash, clan_name):
        return await self.request('/clans/disbandGuild.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def activate_clan_auto_join(self, uid, password_hash, clan_name):
        return await self.request('/clans/acceptGuildAutoJoin.php', {'guildMasterUid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def deactivate_clan_auto_join(self, uid, password_hash, clan_name):
        return await self.request('/clans/cancelGuildAutoJoin.php', {'guildMasterUid': uid, 'passwordHash': password_hash, 'guildName': clan_name})
    
    async def lock_new_raid(self, uid, password_hash, clan_name):
        return await self.request('/clans/requestNewRaidLock.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name, 'isLocked': True})
    
    async def unlock_new_raid(self, uid, password_hash, clan_name):
        return await self.request('/clans/requestNewRaidLock.php', {'uid': uid, 'passwordHash': password_hash, 'guildName': clan_name, 'isLocked': ''})
