# PoPoBot

[简体中文](README_zh-cn.md)

A bot library for [PoPoIM](https://popoim.com). 

> "PoPoIM" is a series of PHP chat source codes, including H5 mobile version, web version, and uniapp version.

## Features

PoPoBot provides a series of APIs aimed at making it easy to create chatbots for PopoIM.

The supported features include:

- Receiving messages
- Sending messages to friends and groups
- Group chat management (kicking members, muting, dissolving, inviting)
- Accepting/rejecting friend requests
- Viewing account messages
- Logging out

And messages use Markdown, so you can send different type of content easily.

## Usage
Install from Pypi:
```Bash
pip install popobot
```


PoPoIM manages cookies in the form of 'session IDs', so you need to obtain the cookie by logging in to PoPoIM on a device, capturing the cookie through packet capture, and keeping logged in without logging out.

```Python
from popobot import *

cookie = '...' #Your cookie.
bot=Account(cookie) #Login to PoPoIM
```

Then you can manage your bot.

Example:
```Python
bot.SendGroupMessage(groupId,'Hello world!')
```

PoPoBot supports:

```Python
SendGroupMessage(group, message) # Send group message
SendFriendMessage(friend, message) # Send friend message

GetGroupMessage(group, limit=20) # Get group messages
GetFriendMessage(friend, limit=20) # Get friend messages

GetInfo() # Get information

GetSelfInfo() # Get self information
GetFriendsList() # Get friends list
GetGroupList() # Get group list
GetChattings() # Get chatting list

GetApplyList() # Get apply list
GetApplyDetail(nid) # Get apply detail
AgreeApply(nid) # Agree to apply
RefuseApply(nid) # Refuse apply

GetGroupInfo(group) # Get group information
GroupKick(group, friend) # Kick member out of the group
GroupInvite(group, friend) # Invite user to join group
GroupLeave(group) # Leave group
GroupDel(group) # Disband group

ApplyFriend(friend) # Apply to add as a friends
FriendDel(friend) # Delete a Friend

Mute(group) # Mute the group
UnMute(group) # Unmute the group

Logout() # Logout
```
