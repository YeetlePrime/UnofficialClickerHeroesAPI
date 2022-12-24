# UnofficialClickerHeroesAPI
An Unofficial API for Clicker Heroes.

## Requests
All requests are made via GET to the base-url "http://ClickerHeroes-SavedGames3-747864888.us-east-1.elb.amazonaws.com".

All requests have to be made in the form "BASE-URL/COMMAND?KEY1=VALUE1&KEY2=VALUE2.....".

Example:  
http://ClickerHeroes-SavedGames3-747864888.us-east-1.elb.amazonaws.com/clans/findGuild.php?uid=0&passwordHash=0&highestZoneReached=0&guildName=1234  
Retrieves the clan info for the clan '1234'.

---
#### /clans/getServerVersion.php
Retrieve the current version of the server.

---
#### /clans/requestToJoinGuild.php
Send a join request to a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the clan to join
```

---
#### /clans/cancelGuildRequest.php
Cancel a join request to a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the requested clan
```

---
#### /clans/leaveGuild.php
Leave a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the clan

```

---
#### /clans/changeNickname.php
Change your nickname
```
uid             id of the player
passwordHash    valid passwordHash to the uid
newNickname     the wanted nickname
```

---
#### /clans/sendGuildMessage.php
Send a message in clan chat.
```
uid             id of the player who should send the message
passwordHash    any passwordHash (doesn't have to match the uid)
guildName       name of the clan in which the message should be sent
message         message to send
```

---
#### /clans/createGuild.php
Create a new clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name for the created clan
```

---
#### /clans/disbandGuild.php
Disband a clan.
```
uid             id of the clanmaster
passwordHash    valid passwordHash to the uid
guildName       name of the clan
```

---
#### /clans/acceptGuildRequest.php
```

```

---
#### /clans/rejectGuildRequest.php
```

```

---
#### /clans/acceptGuildAutoJoin.php
```

```

---
#### /clans/cancelGuildAutoJoin.php
```

```

---
#### /clans/kickGuildMember.php
```

```

---
#### /clans/changeGuildMaster.php
```

```

---
#### /clans/findGuild.php
Get the info for a specified clan.  
Returns the info for a random clan if no clan name is specified.
```
uid                 any uid (doesn't have to be valid)
passwordHash        any passwordHash (doesn't have to be valid)
highestZoneReached  any zone (doesn't have to be valid)
guildName           name of the searched clan (optional)
```

---
#### /clans/getGuildInfo.php
```

```

---
#### /clans/getGuildMessages.php
```

```

---
#### /clans/guildMessageMonitor.php
```

```

---
#### /clans/getRaid.php
```

```

---
#### /clans/getNewRaid.php
```

```

---
#### /clans/getNewRaidRewards.php
```

```

---
#### /clans/getTitanHealth.php
```

```

---
#### /clans/requestBonusFight.php
```

```

---
#### /clans/requestNewRaidLock.php
```

```

---
#### /clans/sendNewImmortalDamage.php
```

```

---
#### /clans/sendTitanDamage.php
```

```

---
#### /clans/updateGuildRank.php
```

```

---
#### /clans/updatePlayer.php
```

```

---
#### /clans/updatePlayerExtended.php
```

```

---
#### /clans/requestToAutoJoinGuild.php
```

```