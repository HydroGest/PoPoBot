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
SendGroupMessage(group,message)
SendFriendMessage(friend , message)

GetGroupMessage(group, limit=20)
GetFriendMessage(friend, limit=20)

GetInfo()
GetSelfInfo()
GetFriendsList()
GetGroupList()
GetChattings()

GetApplyList()
GetApplyDetail(nid)
AgreeApply(nid)
RefuseApply(nid)

GetGroupInfo(group)
GroupKick(group,friend)
GroupInvite(group,friend)
GroupLeave(group)
GroupDel(group)

Logout()
```
