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
uid             id of the clan leader
passwordHash    valid passwordHash to the uid
guildName       name of the clan
```

---
#### /clans/acceptGuildRequest.php
Accept a clan join request.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
uidToAccept         uid of requesting player
guildName           name of the clan
```

---
#### /clans/rejectGuildRequest.php
Reject a clan join request.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
uidToReject         uid of requesting player
guildName           name of the clan
```

---
#### /clans/acceptGuildAutoJoin.php
Enable the clan auto-join feature.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
```

---
#### /clans/cancelGuildAutoJoin.php
Disable the clan auto-join feature.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
```

---
#### /clans/kickGuildMember.php
Kick a clan member.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
uidToKick           uid of the member that should get kicked
```

---
#### /clans/changeGuildMaster.php
Appoints another member to the clan leader.
```
currentGuildMasterUid   uid of the clan leader
passwordHash            valid passwordHash for currentGuildMasterUid
guildName               name of the clan
newGuildMasterUid       uid of the member that should become the new leader
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
Get the clan info based on uid and passwordHash.  
Does the same thing as /clans/findGuild.php, but with different parameters.
```
uid             uid of the player
passwordHash    valid passwordHash for uid
```

---
#### /clans/getGuildMessages.php
Get the clan chat from a clan of choice.  
Contains messages with corresponding timestamp and uid.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/guildMessageMonitor.php
Get the clan chat from a clan of choice.  
Contains the clan chat as displayed in the game (with names and relative time).
```
guildName       name of the clan
```

---
#### /clans/getRaid.php
Get the raid info for legacy raids.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
timestamp       any timestamp (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/getNewRaid.php
Get the raid info for immortal raids.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/getNewRaidRewards.php
PURPOSE NOT KNOWN YET.
```
uid
passwordHash
guildName           name of the clan
lastRaidChecked
lastBonusChecked
```

---
#### /clans/getTitanHealth.php
Get the damage numbers on todays legacy raid.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
timestamp       any timestamp (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/requestBonusFight.php
Initiate bonus immortal raid.  
Can only be done once daily after the regular immortal raid.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doens't have to be valid)
guildName       name of the clan
```

---
#### /clans/requestNewRaidLock.php
Lock or unlock the immortal raid level.
```
uid             uid of the clan leader
passwordHash    valid passwordHash for uid
isLocked        leave it empty for unlocking, anything else for locking
```

---
#### /clans/sendTitanDamage.php
Add *damageDone* damage to the uids dealt damage in the legacy raid.
```
uid             uid of the attacking player
passwordHash    valid passwordHash for the uid
guildName       name of the clan (the uid doesn't have to be a member of this clan)
damageDone      damage that should be dealt
levelStarted    raid boss level before the attack
levelReached    raid boss level after the attack
timestamp       any timestamp (doesn't have to be valid)
```

---
#### /clans/sendNewImmortalDamage.php
Change damage dealt of *uid* to *damageDone*.  
Also sets the immortal raid level to *level*.
```
uid             uid of attacking player
passwordHash    valid passwordHask for uid
guildName       name of the clan
damageDone      damage that should be dealt (current dealt damage gets replaced  
                by that value iff it is smaller than the new damageDone)
level           level of the immortal. can be changed
isBonusFight    leave empty for regular fight. anything else is bonus fight.
```

---
#### /clans/updateGuildRank.php
Update highestZoneReachedAverage of clan to a new value.  
Apparently used for leaderboard stuff, although there is no ClickerHeroes leaderboard that I know of.  
Maybe there is some intern leaderboard that is not accessible to users.
```
uid                         any uid (doesn't have to be valid)
passwordHash                any passwordHash (doesn't have to be valid)
guildName                   name of the clan
highestZoneReachedAverage   new average zone value
```

---
#### /clans/updatePlayer.php
Update the highest Zone ever (HZE) of a player.
```
uid                 uid of a player
passwordHash        valid passwordHash for the uid
highestZone         new highest Zone ever (has to be >= current HZE to update)
```

---
#### /clans/updatePlayerExtended.php  NOT FINISHED
Update the chosenClass and classLevel of a player.
```
uid                         uid of the player
passwordHash                valid passwordHash for the uid
chosenClass                 0 -> None, 1 -> Rogue, 2 -> Mage  
                            3 -> Priest, everything else bugs out
classLevel
lastRewardTimestamp
lastBonusRewardTimestamp
```

---
#### /clans/requestToAutoJoinGuild.php
Use is unclear for now.
```

```