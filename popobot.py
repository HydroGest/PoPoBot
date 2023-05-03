"""
@author: HydroGest
@date: 2023-5-3

泡泡IM机器人库

使用方法:
    :from popobot import *
    

开源包，任何人都可以使用并修改！
"""

__version__ = '0.1'

from requests import get,post
from json import loads,dumps

class Account:
    def __init__(self, cookie):
        self.cookie = cookie

    def SendGroupMessage(group,message):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Referer':'https://im.popoim.com/im/h5/group/chat/%s'%group,
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/h5/message/send'
        to=group
        content=message
        uniqueId=int(time.time())
        data = {
            "to": to,
            "content": content,
            "type": 'group',
            "uniqueId": "%s"%uniqueId
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
    
    def GetInfo():
        url='https://im.popoim.com/web/pop/get'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        return loads(str(get(url,headers=headers).text))['data']
       
    def GetFriendsList():
        url='https://im.popoim.com/web/friend/getlist'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        return loads(str(get(url,headers=headers).text))['data']

    def SendFriendMessage(friend,message):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Referer':'https://im.popoim.com/im/h5/friend/chat/%s'%friend,
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/h5/message/send'
        to=friend
        content=message
        uniqueId=int(time.time())
        data = {
            "to": to,
            "content": content,
            "type": 'friend',
            "uniqueId": "%s"%uniqueId
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']

    def GetGroupMessage(group,limit=20):
        url='https://im.popoim.com/web/message/get?id=%s&type=group&limit=%s'%(group,limit)
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        return loads(str(get(url,headers=headers).text))['data']
    
    def GetFriendMessage(friend,limit=20):
        url='https://im.popoim.com/web/message/get?id=%s&type=friend&limit=%s'%(friend,limit)
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        return loads(str(get(url,headers=headers).text))['data']
        
    def GetGroupList():
        url='https://im.popoim.com/web/pop/get'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data= loads(str(get(url,headers=headers).text))['data']
        if 'group' in data:
            return data['group']
    
    def GetSelfInfo():
        url='https://im.popoim.com/web/pop/get'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data= loads(str(get(url,headers=headers).text))['data']
        if 'mine' in data:
            return data['mine']
        else:
            return {}
    
    def GetChattings():
        url='https://im.popoim.com/web/pop/get'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data= loads(str(get(url,headers=headers).text))['data']
        if 'chatting' in data:
            return data['chatting']
        else:
            return {}

    def GetApplyList():
        url='https://im.popoim.com/web/friend/applylist'
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        return loads(str(get(url,headers=headers).text))['data']
    
    def GetApplyDetail(nid):
        url='https://im.popoim.com/web/friend/applydetail?nid=%s'%nid
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data= loads(str(get(url,headers=headers).text))['data']
        return data
    
    def AgreeApply(nid):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/friend/agree'
        data = {
            'nid':nid
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
    
    def GetGroupInfo(group):
        url='https://im.popoim.com/web/group/detail?gid=%s'%group
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }
        data= loads(str(get(url,headers=headers).text))['data']
        return data
    
    def GroupKick(group,friend):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/group/memberdel'
        data = {
            'gid':group,
            'members[]':friend
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
    
    def GroupInvite(group,friend):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/group/memberadd'
        data = {
            'gid':group,
            'members[]':friend
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
    
    def GroupLeave(group):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/group/leave'
        data = {
            'gid':group
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
        
    def GroupDel(group):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/group/delete'
        data = {
            'gid':group
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
    
    def RefuseApply(nid):
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/friend/refuse'
        data = {
            'nid':nid
        }
        return loads(str(post(url,headers=headers,data=data).text))['data']
        
    def Logout():
        headers = {
            'Origin':'https://im.popoim.com',
            'Host':'im.popoim.com',
            'Cookie':self.cookie,
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
       }
        url='https://im.popoim.com/web/login/logout'
        return loads(str(post(url,headers=headers,data=data).text))['data']
