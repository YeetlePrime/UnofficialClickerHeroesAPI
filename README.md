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
##### Should be investigated
Retrieve the current version of the server.

---
#### /clans/findGuild.php
Get the info for a specified clan.  
Returns the info for a random clan if no clan name is specified.
```
uid                 any uid (doesn't have to be valid)
passwordHash        any passwordHash (doesn't have to be valid)
highestZoneReached  any zone (doesn't have to be valid)
guildName           name of the searched clan (optional: returns random clan if not specified)
```

---
#### /clans/getRaid.php
##### Should be investigated
Get the raid info for legacy raids.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
timestamp       any timestamp (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/getTitanHealth.php
##### Should be investigated
Get the damage numbers on todays legacy raid.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
timestamp       any timestamp (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/getNewRaid.php
##### Should be investigated
Get the raid info for immortal raids.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doesn't have to be valid)
guildName       name of the clan
```

---
#### /clans/getNewRaidRewards.php
##### Should be investigated
PURPOSE NOT KNOWN YET.
```
uid
passwordHash
guildName           name of the clan
lastRaidChecked
lastBonusChecked
```

---
#### /clans/requestBonusFight.php
##### Should be investigated
Initiate bonus immortal raid.  
Can only be done once daily after the regular immortal raid.
```
uid             any uid (doesn't have to be valid)
passwordHash    any passwordHash (doens't have to be valid)
guildName       name of the clan
```

---
#### /clans/getGuildInfo.php
##### Should be investigated
Get the clan info based on uid and passwordHash.  
Does the same thing as /clans/findGuild.php, but with different parameters.
```
uid             uid of the player
passwordHash    valid passwordHash for uid
```

---
#### /clans/createGuild.php
##### Should be investigated
Create a new clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name for the created clan
```

---
#### /clans/requestToJoinGuild.php
##### Should be investigated
Send a join request to a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the clan to join
```

---
#### /clans/cancelGuildRequest.php
##### Should be investigated
Cancel a join request to a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the requested clan
```

---
#### /clans/leaveGuild.php
##### Should be investigated
Leave a clan.
```
uid             id of the player
passwordHash    valid passwordHash to the uid
guildName       name of the clan

```

---
#### /clans/updatePlayer.php
##### Should be investigated
Update the highest Zone ever (HZE) of a player.
```
uid                 uid of a player
passwordHash        valid passwordHash for the uid
highestZone         new highest Zone ever (has to be >= current HZE to update)
```

---
#### /clans/updatePlayerExtended.php  NOT FINISHED
##### Should be investigated
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
#### /clans/changeNickname.php
##### Should be investigated
Change your nickname
```
uid             id of the player
passwordHash    valid passwordHash to the uid
newNickname     the wanted nickname
```

---
#### /clans/getGuildMessages.php
##### Should be investigated
Get the clan chat from a clan of choice.  
Contains messages with corresponding timestamp and uid.
```
uid             uid of a player in the clan
passwordHash    passwordHash of the player
guildName       name of the clan
```

---
#### /clans/sendGuildMessage.php
##### Should be investigated
Send a message in clan chat.
```
uid             id of the player who sends the message
passwordHash    passwordHash for the player
guildName       name of the clan in which the message should be sent
message         message to send
```

---
#### /clans/sendTitanDamage.php
##### Should be investigated
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
##### Should be investigated
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
#### /clans/kickGuildMember.php
##### Should be investigated
Kick a clan member.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
uidToKick           uid of the member that should get kicked
```

---
#### /clans/acceptGuildRequest.php
##### Should be investigated
Accept a clan join request.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
uidToAccept         uid of requesting player
guildName           name of the clan
```

---
#### /clans/rejectGuildRequest.php
##### Should be investigated
Reject a clan join request.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
uidToReject         uid of requesting player
guildName           name of the clan
```

---
#### /clans/disbandGuild.php
##### Should be investigated
Disband a clan.
```
uid             id of the clan leader
passwordHash    valid passwordHash to the uid
guildName       name of the clan
```

---
#### /clans/acceptGuildAutoJoin.php
##### Should be investigated
Enable the clan auto-join feature.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
```

---
#### /clans/cancelGuildAutoJoin.php
##### Should be investigated
Disable the clan auto-join feature.
```
guildMasterUid      uid of the clan leader
passwordHash        valid passwordHash for guildMasterUid
guildName           name of the clan
```

---
#### /clans/requestNewRaidLock.php
##### Should be investigated
Lock or unlock the immortal raid level.
```
uid             uid of the clan leader
passwordHash    valid passwordHash for uid
isLocked        leave it empty for unlocking, anything else for locking
```

---
#### /clans/changeGuildMaster.php
##### Should be investigated
Appoints another member to the clan leader.
```
currentGuildMasterUid   uid of the clan leader
passwordHash            valid passwordHash for currentGuildMasterUid
guildName               name of the clan
newGuildMasterUid       uid of the member that should become the new leader
```

---
#### /clans/guildMessageMonitor.php
##### Should be investigated
Get the clan chat from a clan of choice.  
Contains the clan chat as displayed in the game (with names and relative time).
```
guildName       name of the clan
```

---
#### /clans/updateGuildRank.php
##### Should be investigated
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
#### /clans/requestToAutoJoinGuild.php
##### Should be investigated
Use is unclear for now.
```

```