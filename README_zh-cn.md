# PoPoBot

[English](README.md)

PoPoBot 是用于 PoPoIM 的机器人库。

> "PoPoIM" 是一系列 PHP 聊天源代码，包括 H5 移动版、Web 版和 uniapp 版。

## 特点

PoPoBot 提供了一系列 API，旨在为 PoPoIM 创建聊天机器人提供便利。

支持的功能包括：

- 接收消息

- 向好友和群发送消息

- 群聊管理（踢出成员、禁言、解散、邀请等）

- 接受/拒绝好友请求

- 查看帐户消息

- 注销登录

而且消息使用 Markdown，因此您可以轻松发送不同类型的内容。

## 用法

从Pypi上安装：
```Bash
pip install popobot
```


PoPoIM 以“会话 ID”的形式管理 Cookie，因此您需要登录设备上的 PoPoIM，通过抓包或F12来捕获 Cookie，并保持登录状态而不退出以获取 Cookie。

```Python
from popobot import *

cookie = '...' #Your cookie.
bot=Account(cookie) #Login to PoPoIM
```
然后，您可以管理您的机器人。

示例:
```Python
bot.SendGroupMessage(groupId,'Hello world!')
```

PoPoBot 支持：

```Python
SendGroupMessage(group,message) # 发送群组消息
SendFriendMessage(friend , message) # 发送好友消息

GetGroupMessage(group, limit=20) # 获取群消息
GetFriendMessage(friend, limit=20) # 获取好友消息

GetInfo() # 获取信息

GetSelfInfo() # 获取自身信息
GetFriendsList() # 获取好友列表
GetGroupList() # 获取群组列表
GetChattings() # 获取聊天列表

GetApplyList() # 获取申请列表
GetApplyDetail(nid) # 获取申请详情
AgreeApply(nid) # 同意申请
RefuseApply(nid) # 拒绝申请

GetGroupInfo(group) # 获取群组信息
GroupKick(group,friend) # 将成员踢出群组
GroupInvite(group,friend) # 邀请用户加入群组
GroupLeave(group) # 退出群组
GroupDel(group) # 解散群组

Logout() # 注销登录
```
