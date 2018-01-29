# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,string,goslate,requests,wikipedia,ast,os.path,urllib,shutil,subprocess,urllib,tempfile,urllib2,urllib3,pafy
from random import randint
from bs4 import BeautifulSoup
from googletrans import Translator
from gtts import gTTS
import subprocess as cmd

cl = LINETCR.LINE()
cl.login(token="TOKEN_MU_TARUH_SINI")
cl.loginResult()

print "=======  LOGIN SUKSES WIB======="
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔═[ ωเɓ ૮σɱɱαɳ∂ ]══
║
╠[❅]-Mymid
╠[❅]-Myname:
╠[❅]-Mybio:
╠[❅]-Mid  @ 
╠[❅]-Copy  @
╠[❅]-Backup
╠[❅]-Getpict @
╠[❅]-Getcover  @
╠[❅]-Getvid  @
╠[❅]-Mypict 
╠[❅]-Mycover 
╠[❅]-Myvid 
╠[❅]-Getname
╠[❅]-Getinfo @
╠[❅]-Getprofile @
╠[❅]-Mygroup 
╠[❅]-Pictgroup 
╠[❅]-Cover group 
╠[❅]-Mimic on/off 
╠[❅]-Mimic add/del
╠[❅]-Mimic list 
╠[❅]-Clear mimic 
╠[❅]-Read on/off
╠[❅]-Read set:
╠[❅]-Respon on/off 
╠[❅]-Respon set:
╠[❅]-Wm on/off 
╠[❅]-Wm set:
╠[❅]-Wm1 on/off
╠[❅]-Wm1 set:
╠[❅]-Wm2 on/off 
╠[❅]-Wm2 set: 
╠[❅]-Lm on/off 
╠[❅]-Lm set: /
╠[❅]-Message add: 
╠[❅]-Message cek
╠[❅]-Comment set:
╠[❅]-Comment cek
╠[❅]-Sticker cek
╠[❅]-Sticker list
╠[❅]-Stid 
╠[❅]-Stpkg 
╠[❅]-Stver 
╠[❅]-Ginfo 
╠[❅]-Onlink / Oflink 
╠[❅]-Gurl 
╠[❅]-Invite:on 
╠[❅]-Invite2:on 
╠[❅]-Invite: 
╠[❅]-Gcancel: 
╠[❅]-Gn: 
╠[❅]-Bye @
╠[❅]-Ats
╠[❅]-Say 
╠[❅]-Cctv 
╠[❅]-Cek 
╠[❅]-Spam add: [ teks ]
╠[❅]-Spam: [ jumlah ]
╠[❅]-Gift -jmlah
╠[❅]-View: tgl-bln-thn
╠[❅]-Gcast: - Bc all grup
╠[❅]-Mcast: - Bc all member
╠[❅]-Fcast: - Bc all friend
╠[❅]-Cancel 
╠[❅]-Ban:on 
╠[❅]-Unban:on
╠[❅]-Ban all - BL all member
╠[❅]-Banlist 
╠[❅]-Clear ban
╠[❅]-Killban 
╠[❅]-Great / Cleanse
╠[❅]-Removechat 
╠[❅]-Restart 
╠[❅]-Translate
╠[❅]-Music: - judul 
╠[❅]-Ytb: - judul 
╠[❅]-Lyric: - judul
╠[❅]-Wiki: - judul
╠[❅]-Image: - nama
╠[❅]-Insta: - nama ig
╠[❅]-Say: - teks ke voice
╠[❅]-Text: - fancytext
╠[❅]-Qrprotect on/off
╠[❅]-Blockinvite on:off
╠[❅]-Namelock on:off
║
╚═[ ℬℽ : W⃟   I⃟   B⃟   ]═══"""

trhelp ="""
╔══════════════
║  ☫ Translator Menu ☫
╠══════════════
╠[-Tr  id     to > Indonesia
╠[-Tr  en    to > English
╠[-Tr  fr    to > Fance
╠[-Tr  ar    to > Arab
╠[-Tr  cn    to > Cina
╠[-Tr  de    to > Denmark
╠[-Tr  hi     to > Hindi
╠[-Tr  jp     to > Japan
╠[-Tr  jw    to > Jawa
╠[-Tr  su    to > Sunda
╠[-Tr  ms   to > Malaysia
╠[-Tr  vi     to > Vietnam
╠[-Tr  ko    to > Korea
╠[-Tr  th     to > Thailand
╚═══════════════"""

KAC = [cl]
mid = cl.getProfile().mid
Bots = [mid,"u4a361586c55ac4ef218a0a9b78b2f1b3"]
admin = ["u4a361586c55ac4ef218a0a9b78b2f1b3"]
owner = ["u4a361586c55ac4ef218a0a9b78b2f1b3"]
protectname = []
protecturl = []
protection = []
autocancel = {}

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    "winvite":False,
    "winvite2":False,
    'autoAdd':False,
    'message':"Thanks For Add Me",
    "lang":"JP",
    "comment":"Auto Like by: ™ WIB ™",
    "likeOn":False,
    "welkam":"Selamat Bergabung",
    "welkam1": "Selamat Bergabung",
    "welkam2": "Selamat Bergabung",
    "bye":"Selamat Jalan.. !!",
    "tag":"Jangan tag Kalau kangen PC aja Kaleee... !!!",
    "read":"Masuk chat sini.. !!",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "Welcome":False,
    "Welcome1": False,
    "Welcome2": False,
    "Leave": False,
    "Mention": False,
    "sticker":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "Protectcancel":False,
    "spam":"",
    "pro_name":{},    
    "dblacklist":False
}

wait3 = {
	'readMember':{},
	'readpoint':{},
	'ROM':{},
	'setTime':{}
    }
	
mimic = {
	'copy':False,
	'copy2':False,
	'status':False,
	'target':{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

settings = {
    "changePicture":{},
    "changeGroupPicture":{},
    "server":{},
    }

setTime = {}
setTime = wait3["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

tikel = {
     'STKID': '17866',
     'STKPKGID': '1070',
     'STKVER': '2'
     }

mulai = time.time()

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self.Talkclient.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = cl.server.post_content(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = cl.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         cl.sendImage(to_, path)
      except:
         try:
            cl.sendImage(to_, path)
         except Exception as e:
            raise e

def sendImageWithURL(self, to_, url):
        """Send a image with given image url

        :param url: image url to send
        """
        path = 'pythonLine.data'

        r = cl.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download image failure.')

        try:
            cl.sendImage(to_, path)
        except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = cl.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         cl.sendAudio(to_, path)
      except Exception as e:
         raise e
def sendAudio(self, to_, path):
      M = Message(to=to_,contentType = 3)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = cl.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'audio',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
def sendVideo(self, to_, path):
      M = Message(to=to_,contentType = 2)
      M.contentMetadata = {
           'VIDLEN' : '0',
           'DURATION' : '0'
       }
      M.contentPreview = None
      M_id = cl.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'video',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
def sendVideoWithURL(self, to_, url):
      path = 'pythonLines.data'
      r = cl.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         cl.sendVideo(to_, path)
      except Exception as e:
         raise e

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n • " + Name
                wait2['ROM'][op.param1][op.param2] = " • " + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendSticker(self,
                    stickerId = "13",
                    stickerPackageId = "1",
                    stickerVersion = "100",
                    stickerText="[null]"):
        try:
            message = Message(to=self.id, text="")
            message.contentType = ContentType.STICKER

            message.contentMetadata = {
                'STKID': stickerId,
                'STKPKGID': stickerPackageId,
                'STKVER': stickerVersion,
                'STKTXT': stickerText,
            }

            self._client.sendMessage(message)

            return True
        except Exception as e:
            raise e

def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)

def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('Update profile video picture failure.')
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')

def updateProfileCover(self, path, returnAs='bool'):
        if len(self.server.channelHeaders) < 1:
            raise Exception('LineChannel instance is required for acquire this action.')
        else:
            if returnAs not in ['objId','bool']:
                raise Exception('Invalid returnAs value')
            objId = self.uploadObjHome(path, type='image', returnAs='objId')
            home = self._channel.updateProfileCoverById(objId)
            if returnAs == 'objId':
                return objId
            elif returnAs == 'bool':
                return True

def updatebbbProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

def updateProfilePicture(self, path):
    file=open(path, 'rb')
    files = {
        'file': file
    }
    params = {
        'name': 'media',
        'type': 'image',
        'oid': self.profile.mid,
        'ver': '1.0',
    }
    data={
        'params': json.dumps(params)
    }
    r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
    if r.status_code != 201:
        raise Exception('Update profile picture failure.')
    return True

def updateGroupPicture(self, groupId, path):
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': groupId,'type': 'image'})}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/g/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update group picture failure.')
        return True

def downloadObjectMsg(self, messageId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        params = {'oid': messageId}
        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/talk/m/download.nhn', params)
        r = self.server.getContent(url)
        if r.status_code == 200:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download object failure.')

def genTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'linepy-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return os.path.join(fPath, fName)
        except:
            raise Exception('tempfile is required')

def genOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.genTempFile('file'),'ver': '1.0'}
        if returnAs not in ['json','b64','default']:
            raise Exception('Invalid parameter returnAs')
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList=json.dumps(oldList)
            return oldList
        elif returnAs == 'b64':
            oldList=json.dumps(oldList)
            return base64.b64encode(oldList.encode('utf-8'))
        elif returnAs == 'default':
            return oldList

def downloadObjectMsgId(self, messageId):
        saveAs = '%s/%s-%i.bin' % (tempfile.gettempdir(), messageId, randint(0, 9))
        params = {'oid': messageId}
        url = self.server.urlEncode('https://obs.line-apps.com', '/talk/m/download.nhn', params)
        r = self.server.getContent(url)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
				shutil.copyfileobj(r.raw, f)			
				return saveAs
        else:
            raise Exception('Download file failure.')

def urlEncode(self, url, path, params=[]):
        try:        # Works with python 2.x
            return url + path + '?' + urllib.urlencode(params)
        except:     # Works with python 3.x
            return url + path + '?' + urllib.parse.urlencode(params)

def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

def setChannelHeadersWithDict(self, headersDict):
        self.channelHeaders.update(headersDict)

def setChannelHeaders(self, argument, value):
        self.channelHeaders[argument] = value

def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
         
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    ki.cancelGroupInvitation(op.param1, matched_list)
                    kk.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if wait["Welcome1"] == True:
                ginfo = ki.getGroup(op.param1)
                ki.sendText(op.param1,"Selamat Bergabung di  " + str(ginfo.name)+"\n"+str(wait["welkam1"]))

        if op.type == 17:
            if wait["Welcome2"] == True:
                ginfo = kk.getGroup(op.param1)
                kk.sendText(op.param1,"Selamat Bergabung di  " + str(ginfo.name)+"\n"+str(wait["welkam2"]))

        if op.type == 17:
            if wait["Welcome"] == True:
                cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                if (wait["welkam"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendImageWithURL(op.param1, path)
                    cl.sendText(op.param1,str(wait["welkam"]))

        if op.type == 15:
            if wait["Leave"] == True:
                cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                if (wait["bye"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendImageWithURL(op.param1, path)
                    cl.sendText(op.param1,str(wait["bye"]))

        if op.type == 17:
            if mid in op.param3:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user flushing is complete")
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n\n『📷』•" + Name   
                        wait2['ROM'][op.param1][op.param2] = "『📷』" + Name 
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                  pass                  

        #------Protect Group Kick start------#
        if op.type == 11:
         #if op.param1 in wait["Protectgr"]:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
              	try:
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Block QR is on\nDon't open..!!")
                	cl.kickoutFromGroup(op.param1,[op.param2])
                	X = cl.getGroup(op.param1)
                	X.preventJoinByTicket = True
                	cl.updateGroup(X)
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "Already on blacklist")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Block QR is on\nDon't open..!!")
                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                	X = random.choice(KAC).getGroup(op.param1)
                	X.preventJoinByTicket = True
                	random.choice(KAC).updateGroup(X)
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Already on blacklist")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
         #if op.param1 in wait["Protectcancl"]:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              else:
                try:
                  cl.cancelGroupInvitation(op.param1, gMembMids)
                  cl.sendText(op.param1, "Block invite Is on\nDont invite members..!!")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1, "Block invite Is on\nDont invite members..!!")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
#-----------------------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                            cl.sendText(op.param1,"Groupname Lock on")
                            c = Message(to=op.param1, from_=None, text=None, contentType=13)
                            c.contentMetadata={'mid':op.param2}
                            cl.sendMessage(c)
        #------Joined User Kick start------#
        if op.type == 17:
         #if op.param1 in wait["Protectjoin"]:
          if wait["Protectjoin"] == True:
            if op.param2 in wait["blacklist"]:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Kick Joined is on")
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Kick Joined is on")
        #------Joined User Kick start------#
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
         #if op.param1 in wait["Protectcancel"]:
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                random.choice(KAC).sendText(op.param1, "Block cancel is on")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])   
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL already Locked.. !!\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u4a361586c55ac4ef218a0a9b78b2f1b3":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X = ki.getGroup(list_[1])
                            X = kk.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                            ki.updateGroup(X)
                            kk.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")

        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                	text = msg.text
                	if text is not None:
                		cl.sendText(msg.to,text)

        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     ret_ = "Ada apa  " + cName + "  ?\n" + str(wait["tag"])
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                   xname = cl.getContact(msg.from_).displayName
                                   xlen = str(len(xname)+1)
                                   msg.contentType = 0
                                   balas = "@"+xname+ " Jangan Tag Ahhh Jika Kangen PC Sono...\n\n","@"+xname+ " Fan Gue Buangeeeet...\n\n"
                                   msg.text = random.choice(balas)
                                   msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                                   cl.sendMessage(msg)
                                   msg.contentType = 7   
                                   msg.text = None
                                   msg.contentMetadata = tikel
                                           #"STKID": "527",
                                           #"STKPKGID": "2",
                                           #"STKVER": "100" }
                                   cl.sendMessage(msg)
#------------------------------------------------------------------------------------
            if msg.contentType == 1:
               if settings["changePicture"] == True:
                    path = cl.downloadObjectMsgId(msg.id)
                    settings["changePicture"] = False
                    cl.updateProfilePicture(path)
                    cl.sendText(msg.to, "Berhasil mengubah foto profile")
            if msg.toType == 2:
               if settings["changeGroupPicture"] == True:
                    path = cl.downloadObjectMsgId(msg.id)
                    settings["changeGroupPicture"].remove(msg.to)
                    cl.updateGroupPicture(msg.to, path)
                    cl.sendText(msg.to, "Berhasil mengubah foto group")

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1002)                    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = ki.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     ki.sendText(msg.to,"Done Invite : \n▶ " + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         kk.findAndAddContactsByMid(invite)
                                         kk.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         ki.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
            	if wait["winvite2"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = kk.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 kk.sendText(msg.to,"▶ " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 kk.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 kk.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     kk.findAndAddContactsByMid(target)
                                     kk.inviteIntoGroup(msg.to,[target])
                                     kk.sendText(msg.to,"Done Invite : \n▶ " + _name)
                                     wait["winvite2"] = False
                                     break
                                 except:
                                     try:
                                         kk.findAndAddContactsByMid(invite)
                                         kk.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite2"] = False
                                     except:
                                         kk.sendText(msg.to,"Limit invite njirrrr")
                                         wait["winvite2"] = False
                                         break

        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "Sticker Check:\n\n▪ STKID : %s\n▪ STKPKGID : %s\n▪ STKVER : %s\n\n▪ Link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    wait["sticker"] = False
                    cl.sendText(msg.to, filler)
                else:
                    pass

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"It's included in a blacklist already。")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I decided not to make a comment。")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist。")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist。")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"It's included in a blacklist already.。")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"It was added to the blacklist.。")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"It was eliminated from a blacklist。")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It isn't included in a blacklist。")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,helpt)

            elif msg.text in ["Translate"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,trhelp + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,trans)

            elif ("Mimic add " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Mimic del " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Mimic list"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target Mimic User:\n===============\n\n"
                            for mi_d in mimic["target"]:
                                mc += "▪ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc+"\n\nTotal: "+str(len(mimic["target"]))+" user\n===============")

            elif "Mimic copy " in msg.text:
                        if mimic["copy2"] == True:
                            siapa = msg.text.replace("Mimic copy ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Copy message on\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Copy message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif ("Gn: "in msg.text):
                if msg.toType == 2:
                    gg = cl.getGroup(msg.to)
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                    cl.sendText(msg.to,'Ganti dari:  ' + str(gg.name)+'\n\nKe:  '+str(X.name) + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,'Ganti dari:  ' + str(gg.name)+'\n\nKe:  '+str(X.name) + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 ki.sendText(msg.to,"send contact to invite.. !!")
            elif msg.text in ["Invite2:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 kk.sendText(msg.to,"send contact to invite.. !!")
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "Wib 1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif "Wib 2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Mybot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","K1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["愛のプレゼント","K2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kk.sendMessage(msg)

            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getContact(msg.to)
                targets = []
                for g in gs:
                    if target == []:
                    	targets.append(g.mid)
                    if t in targets:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '1345',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)

            elif msg.text in ["Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There isn't an invited person。")
                        else:
                            cl.sendText(msg.to,"you Sato face-like person absence。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")

            elif msg.text in ["Bot cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"There isn't an invited person。")
                        else:
                            ki.sendText(msg.to,"you Sato face-like person absence。")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Wm set: " in msg.text:
                wait["welkam"] = msg.text.replace("Wm set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Wm1 set: " in msg.text:
                wait["welkam1"] = msg.text.replace("Wm1 set: ","")
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm1 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Welcome message change to\n\n" + wait["welkam1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    ki.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Wm2 set: " in msg.text:
                wait["welkam2"] = msg.text.replace("Wm2 set: ","")
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Welcome message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    kk.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Wm2 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Welcome message change to\n\n" + wait["welkam2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    kk.sendText(msg.to,"Welcome message saat ini:\n\n" + wait["welkam2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Lm set: " in msg.text:
                wait["bye"] = msg.text.replace("Lm set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Leave message changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Lm cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Leave message saat ini:\n\n" + wait["bye"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Leave message saat ini:\n\n" + wait["bye"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Respon set: " in msg.text:
                wait["tag"] = msg.text.replace("Respon set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Auto respon changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Respon cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["tag"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["tag"])
                else:
                    cl.sendText(msg.to,"Auto respon saat ini:\n\n" + wait["tag"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Read set: " in msg.text:
                wait["read"] = msg.text.replace("Read set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Auto Read changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Read cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Auto Read change to\n\n" + wait["read"])
                else:
                    cl.sendText(msg.to,"Auto Read saat ini:\n\n" + wait["read"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment cek"]:
                cl.sendText(msg.to,"Comment saat ini:\n\n" + str(wait["comment"])+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["コメント:オン","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["コメント:オフ","Comment off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Qrprotect on"]:
                protecturl.append(msg.to)
                cl.sendText(msg.to,"QR protect already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qrprotect off"]:
                if msg.from_ in admin:
                    protecturl.remove(msg.to)
                    cl.sendText(msg.to,"QR protect Is Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Wm on"]:
              if msg.from_ in admin:
                if wait["Welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Wm off"]:
              if msg.from_ in admin:
                if wait["Welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Wm1 on"]:
              if msg.from_ in admin:
                if wait["Welcome1"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        ki.sendText(msg.to,"done")
                else:
                    wait["Welcome1"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Wm1 off"]:
              if msg.from_ in admin:
                if wait["Welcome1"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        ki.sendText(msg.to,"done")
                else:
                    wait["Welcome1"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Wm2 on"]:
              if msg.from_ in admin:
                if wait["Welcome2"] == True:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        kk.sendText(msg.to,"done")
                else:
                    wait["Welcome2"] = True
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Welcome message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        kk.sendText(msg.to,"done")
            elif msg.text in ["Wm2 off"]:
              if msg.from_ in admin:
                if wait["Welcome2"] == False:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        kk.sendText(msg.to,"done")
                else:
                    wait["Welcome2"] = False
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Welcome message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        kk.sendText(msg.to,"done")

            elif msg.text in ["Respon on"]:
              if msg.from_ in admin:
                if wait["Mention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Mention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Respon off"]:
              if msg.from_ in admin:
                if wait["Mention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto respon Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Mention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," Auto respon Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Lm on"]:
              if msg.from_ in admin:
                if wait["Leave"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Leave"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave message already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Lm off"]:
              if msg.from_ in admin:
                if wait["Leave"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Leave"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave message already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Sticker cek"]:
                if wait["sticker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Send sticker to Check\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["sticker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Send sticker to Check!\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif "Stid " in msg.text:
                tikel["STKID"] = msg.text.replace("Stid ","")
                cl.sendText(msg.to, "Sticker Id telah di Set\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif "Stver " in msg.text:
                tikel["STKVER"] = msg.text.replace("Stver ","")
                cl.sendText(msg.to, "Sticker version telah di Set\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif "Stpkg " in msg.text:
                tikel["STKPKGID"] = msg.text.replace("Stpkg ","")
                cl.sendText(msg.to, "Sticker package telah di Set\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Sticker list"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = tikel
                stk_id = tikel['STKID']
                stk_ver = tikel['STKVER']
                pkg_id = tikel['STKPKGID']
                filler = "Sticker saat ini:\n\n▪ STKID : %s\n▪ STKPKGID : %s\n▪ STKVER : %s" % (stk_id,pkg_id,stk_ver)
                cl.sendMessage(msg)
                cl.sendText(msg.to, filler)

            elif msg.text in ["Onlink"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR already Open\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"QR already Open\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Oflink"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR Close\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"QR Close\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif msg.text in ["Ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "refusal"
                        else:
                            u = "許可"
                        cl.sendText(msg.to,"[GROUP]\n" + str(ginfo.name) + "\n\n[GID]\n" + msg.to + "\n\n[GROUP CREATOR]\n" + gCreator + "\n\n[PROFILE GROUP]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMEMBER:" + str(len(ginfo.members)) + "Person\nINVITE:" + sinvitee + "Person\nƖNVITATION URL:" + u + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can't be used besides the group。")
                    else:
                        cl.sendText(msg.to,"Impossible use besides")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mymid" == msg. text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
            elif "Wkwk" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif "Sue" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "105",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kk.sendMessage(msg)
            elif "Welcome" == msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Last name" in msg.text:
                string = msg.text.replace("Last name","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
#---------------------------------------------------------
            elif "Wib1 name: " in msg.text:
                string = msg.text.replace("K1 name: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " ◀ Done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#--------------------------------------------------------
            elif "Wib2 name: " in msg.text:
                string = msg.text.replace("K2 name: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"The name " + string + " ◀ Done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#--------------------------------------------------------
            elif msg.text in ["Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)  

            elif msg.text.lower() in ["creator"]:
            	creator = 'u4a361586c55ac4ef218a0a9b78b2f1b3'
                msg.contentType = 13
                msg.contentMetadata = {'mid': creator}
                cl.sendText(msg.to,"⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"⏫⏫⏫⏫⏫⏫⏫⏫⏫⏫")
#--------------------------------------------------------
            elif "My bio: " in msg.text:
                string = msg.text.replace("My bio: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile_B = cl.getProfile()
                    profile_B.statusMessage = string
                    cl.updateProfile(profile_B)
                    cl.sendText(msg.to,"Change Display Name " + string + " done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Wib1 bio: " in msg.text:
                string = msg.text.replace("K1 bio: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"Change Display Name " + string + " done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Wib2 bio: " in msg.text:
                string = msg.text.replace("K2 bio: ","")
                if len(string.decode('utf-8')) <= 600000:
                    profile_C = kk.getProfile()
                    profile_C.statusMessage = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"Name Display Name " + string + " done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact already Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to," Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to," Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Gcancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refusal was turned off。\non, please designate and send the number of people.")
                        else:
                            cl.sendText(msg.to,"number of people")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to," Minimal: " + strnum + " member undangan grup diterima")
                        else:
                            cl.sendText(msg.to,strnum + "Self- you for below shinin-like small.")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"The price is wrong。")
                    else:
                        cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto Leave already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ԼЄƛƔЄ ƠƑƑ ƛԼƦЄƛƊƳ。")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƑƑ。")
            elif msg.text in ["Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Is On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                    else:
                        cl.sendText(msg.to,"Share Is Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Already。")                        
            elif "Read on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                cl.sendText(msg.to,"Auto Read Already \n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                
            elif "Read off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    cl.sendText(msg.to, "Auto Read Is Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to, "Auto Read Has been Not Set")
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="❇ Contact : On\n"       
                else: md+="❇ Contact : Off\n"      
                if wait["autoJoin"] == True: md+="❇ Auto join : On\n" 
                else: md +="❇ Auto join : Off\n"
                if wait["autoCancel"]["on"] == True:md+="❇ Group Cancel : " + str(wait["autoCancel"]["members"]) + " \n"     
                else: md+= "❇ Group Cancel : Off\n"  
                if wait["leaveRoom"] == True: md+="❇ Auto leave : On\n"   
                else: md+="❇ Auto leave : Off\n"
                if wait["timeline"] == True: md+="❇ Auto Share : On\n"  
                else:md+="❇ Auto Share : Off\n" 
                if wait["commentOn"] == True: md+="❇ Comment : On\n"   
                else:md+="❇ Comment : Off\n"    
                if wait["autoAdd"] == True: md+="❇ Auto add : On\n"  
                else:md+="❇ Auto add : Off\n"   
                #if wait["likeOn"] == True: md+="❇ Auto like : On\n"
                #else:md+="❇ Auto like : Off\n" 
                if wait["Welcome"] == True: md+="❇ Welcome message : On\n"  
                else:md+="❇ W message : Off\n"   
                if wait["Leave"] == True: md+="❇ Leave message : On\n"
                else:md+="❇ L mesage : Off\n" 
                if mimic["status"] == True: md+="❇ Mimic : On\n"
                else:md+="❇ Mimic : Off\n" 
                ma = ""
                if msg.to in autocancel: ma+="❇ Blockinvite : On\n"
                else:ma+="❇ Blockinvite : Off\n"
                if msg.to in protecturl: ma+="❇ Qrprotect : On\n"
                else:ma+="❇ Qrprotect : Off\n"
                if msg.to in wait["pname"]: ma+="❇ NameLock : On"
                else:ma+="❇ NameLock : Off"
                cl.sendText(msg.to,"[✧] Selfbot Status:\n\n"+md+"\n[✧] Group Status:\n\n"+ma + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion。")
                else:
                    cl.sendText(msg.to,"key is wrong。")
            elif msg.text in ["Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's on already。")
                    else:
                        cl.sendText(msg.to,"on already。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned on。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Turned on。")
            elif msg.text in ["Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It's off already。")
                    else:
                        cl.sendText(msg.to,"off already。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It was turned off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Turned off。")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                cl.sendText(msg.to,"The message was changed。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Auto addition→" in msg.text:
                wait["message"] = msg.text.replace("Auto addition→","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"The message was changed。")
                else:
                    cl.sendText(msg.to,"was change already。")
            elif msg.text in ["Message cek","自動追加問候語確認"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,".Message add saat ini:\n\n" + wait["message"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"One  of weeds on the surface below the self- additional breath image。\n\n" + wait["message"])
            elif msg.text in ["CHANGE","言語變更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"ƇƠƲƝƬƦƳ ԼƛƝƓƲƛƓЄ ƊƲƦƖƝƓ ƛ ƇHƛƝƓЄ。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,". The language was made English。")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link this group:\n\nline://ti/g/" + gurl+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ.。")
                    else:
                        cl.sendText(msg.to,"ƖMƤƠƧƧƖƁԼЄ ƲƧЄ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ. ")
            elif "Gurl:" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl:","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ƖƬ ƇƛƝ'Ƭ ƁЄ ƲƧЄƊ ƁЄƧƖƊЄƧ ƬHЄ ƓƦƠƲƤ。")
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    x = ki.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ƇƛƝ ƝƠƬ ƁЄ ƲƧЄƊ ƠƲƬƧƖƊЄ ƬHЄ ƓƦƠƲƤ")
                    else:
                        cl.sendText(msg.to,"ƝƠƬ ƑƠƦ ƲƧЄ ԼЄƧƧ ƬHƛƝ ƓƦƠƲƤ")
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send contact to blacklist")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send contact to delete blacklist")
            elif msg.text in ["cbc"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"There isn't a person made a blacklist。")
                else:
                    cl.sendText(msg.to,"Below is a blacklist。")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clocon"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"It's on already。")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was turned on")
            elif msg.text in ["Clocoff"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"It's off already.。")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"It was tuned off。")
            elif "Cloc:" in msg.text:
                n = msg.text.replace("Clck:","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"Last name clock。")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"It was renewed\n\n" + n)
            elif msg.text in ["Uclock"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"It was renewed。")
                else:
                    cl.sendText(msg.to,"Please turn on a name clock.。")

            elif msg.text.lower() in ["invgroupcall"]:
                if msg.toType == 2:
                   group = cl.getGroup(msg.to)
                   members = [mem.mid for mem in group.members]
                   call.acquireGroupCallRoute(msg.to)
                   call.inviteIntoGroupCall(msg.to, contactIds=members)
                   cl.sendText(msg.to, "Berhasil mengundang kedalam telponan group")
                else:
                   cl.sendText(msg.to, "Berhasil mengundang kedalam telponan group")
            elif msg.text.lower() in ["change pict"]:
                settings["changePicture"] = True
                cl.sendText(msg.to, "Silahkan kirim gambarnya")
            elif msg.text in ["Gpict change"]:
              if msg.toType == 2:
                settings["changeGroupPicture"][msg.to] = True
                settings["changeGroupPicture"].append(msg.to)
                cl.sendText(msg.to,"silahkan kirim gambarnya")
#---------------------------------Mention Members----------------------------------
            elif msg.text in ["Ats","Tagall"]:
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
#------------------------------------Kicker Join Start-----------------------------
            elif msg.text in ["Join all","Masuk"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Wib1 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Wib2 join"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)           
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to,Ti)

            elif msg.text in ["Bye all","Pulang"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
                except:
                     pass            

            elif msg.text in ["#pamit"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					cl.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["Wib1 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
                except:
                     pass

            elif msg.text in ["Wib2 bye"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					kk.leaveGroup(msg.to)
                except:
                     pass
#--------------------------------Kicker bye finish--------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bots Already Running On:\n\n"+waktu(eltime)
                cl.sendText(msg.to,van+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#-----------------------------------------------------------------------------------------
            elif "Cleanse" in msg.text:
              if msg.from_ in Bots or staff:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots:
                                try:
                                   klist=[cl,ki,kk]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                	pass

            elif "Great" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Great","")
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"")
                       else:
                           for target in targets:
                               if target not in Bots:
                                   try:
                                       cl.kickoutFromGroup(msg.to,[target])
                                   except:
                                       cl.sentText(msg.to,"")
#-----------------------------------------------------------                          
            elif "Bye" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                           ki.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

            elif "Wib1 kuy" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except:
                           kk.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

            elif "Wib2 kuy" in msg.text:
                if msg.contentMetadata is not None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kk.kickoutFromGroup(msg.to,[target])
                        except:
                           cl.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

            elif "Ko1 " in msg.text:
                       nk0 = msg.text.replace("Ko1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)

            elif "Ko2 " in msg.text:
                       nk0 = msg.text.replace("Ko2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kk.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kk.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

            elif msg.text in ["Mygroup"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "◓- %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"                     LIST GROUP\n══════════════════════\n"+ h +"\n\n[◓] Total group: " +"["+str(len(gid))+"]\n\nRead time: " + datetime.today().strftime('%H:%M:%S')+"\n══════════════════════")

            elif msg.text in ["Wib1 group"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[◓] %s\n" % (ki.getGroup(i).name +"→["+str(len(ki.getGroup(i).members))+"]")
                ki.sendText(msg.to,"                     LIST GROUP\n══════════════════════\n"+ h +"\n\n[◓] Total group: " +"["+str(len(gid))+"]\n\nRead time: " + datetime.today().strftime('%H:%M:%S')+"\n══════════════════════")

            elif msg.text in ["Wib2 group"]:
                gid = kk.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[◓] %s\n" % (kk.getGroup(i).name +"→["+str(len(kk.getGroup(i).members))+"]")
                kk.sendText(msg.to,"                     LIST GROUP\n══════════════════════\n"+ h +"\n\n[◓] Total group: " +"["+str(len(gid))+"]\n\nRead time: " + datetime.today().strftime('%H:%M:%S')+"\n══════════════════════")
#-----------------------------------------------------------
            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Group name Is Locked\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Group name Is Locked\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Group name Not Locked\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"Group name Not Locked\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
					
            elif "Blockinvite on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Protection already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif "Blockinvite off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Protection Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
				except:
					pass                                 

            elif msg.text in ["Jprotect on"]:
                wait["Protectjoin"] = True
                cl.sendText(msg.to,"Autopurge Already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))                
            elif msg.text in ["Jprotect off"]:
                wait["Protectjoin"] = False
                cl.sendText(msg.to,"Autopurge Is  Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr on"]:
                wait["Protectgr"] = True
                cl.sendText(msg.to,"QR Already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))                
            elif msg.text in ["Qr off"]:
                wait["Protectgr"] = False
                cl.sendText(msg.to,"QR Is Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Cprotect on"]:
                wait["Protectcancl"] = True
                cl.sendText(msg.to,"Block invite Already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))                
            elif msg.text in ["Cprotect off"]:
                wait["Protectcancl"] = False
                cl.sendText(msg.to,"Block invite Is  Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Cancel on"]:
                wait["Protectcancel"] = True
                cl.sendText(msg.to,"Cancel kick Already On\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))                
            elif msg.text in ["Cancel off"]:
                wait["Protectcancel"] = False
                cl.sendText(msg.to,"Cancel kick Is Off\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))                
#-----------------------------------------------------------
            elif "#END" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Otewe Spam...")
                       ki.sendText(g.mid,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")  
                       kk.sendText(g.mid,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")  
                       cl.sendText(msg.to, "Done Spam Target")
                       print "Done spam" 
#-----------------------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"ƤƠƝƓ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"ƤƠƝƓ 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#----------------------------------------------------------
            elif msg.text in ["Absen"]:
                ki.sendText(msg.to,"WIB 1")
                kk.sendText(msg.to,"WIB 2")

            elif msg.text in ["Respon"]:
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName
                kk.sendText(msg.to, text)
#----------------------------------------------------------
            elif msg.text in ["Cctv"]:
                cl.sendText(msg.to,"Detecting reader point..."+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                try:
                    del wait3['readpoint'][msg.to]
                    del wait3['readMember'][msg.to]
                    del wait3['setTime'][msg.to]
                except:
                    pass
                wait3['readpoint'][msg.to] = msg.id
                wait3['readMember'][msg.to] = {}
                wait3['setTime'][msg.to] = datetime.now()
            elif msg.text in ["Cek"]:
                if msg.to in wait3['readpoint']:
                    if wait3['readMember'][msg.to] != {}:
                        nama = wait3['readMember'][msg.to]
                        cb = ""
                        cb2 = ""
                        strt = int(0)
                        akh = int(0)
                        for md in nama:
                            akh = akh + int(5)
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + int(6)
                            akh = akh + 1
                            nrik = cl.getContact(md).displayName
                            cb2 += "@nrik\n"
                        cb = (cb[:int(len(cb)-1)])
                        msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+cb+']}', 'EMTVER': '4'}
                        msg.text = cb2 + "\nRead time cctv: %s" %datetime.today().strftime('%H:%M:%S')
                        msg.contentType = 0
                        try:
                            cl.sendMessage(msg)
                            #cl.sendText(msg.to,"Sukses ciduk: "+str(len(nama))+" cctv\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        except Exception as error:
                            print (error)
                    else:
                        cl.sendText(msg.to, "Nothing read point")
                else:
                    cl.sendText(msg.to, "Ketik 'Cctv' dulu Boss.. !!")
#-----------------------------------------------------------speed  ƧЄƝ SIƊЄƦ
#-----------------------------------------------
	    elif "Gcast: " in msg.text:
		bc = msg.text.replace("Gcast: ","")
		gid = cl.getGroupIdsJoined()
		for i in gid:
		    cl.sendText(i,bc)
		cl.sendText(msg.to,"Success BC to: "+str(len(gid))+ " group Boss")
#--------------------------------------------------------
#-----------------------------------------------
	    elif "Mcast: " in msg.text:
		bc = msg.text.replace("Mcast: ","")
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		for i in mi_d:
		    cl.sendText(i,bc)
		cl.sendText(msg.to,"Success BC to: "+str(len(mi_d))+" members Boss")
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success Recover Group...~")
#--------------------------------------------------------
	    elif msg.text in ["Removechat"]:
		ki.removeAllMessages(op.param2)
		kk.removeAllMessages(op.param2)
		ki.sendText(msg.to,"Removed chat done")
		kk.sendText(msg.to,"Removed chat done")
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["Restart"]:
		cl.sendText(msg.to, "Bot has been restarted.. !!\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
		restart_program()
		cl.sendText(msg.to," Restarting Done...~")
		print "@Restart"
#--------------------------------------------------------
#-----------------------------------------------
	    #elif "Ball" in msg.text:
		#thisgroup = cl.getGroups([msg.to])
		#Mids = [contact.mid for contact in thisgroup[0].members]
		         #for i in Mids:
			  #if target not in Bots:
			    #wait["blacklist"][i]=True
			#else:
			    #pass
            elif "Fcast: " in msg.text:
                bctxt = msg.text.replace("Fcast: ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
                    cl.sendText(msg.to,"Sukses BC to " + str(len(a)) + " friends")
#-----------------------------------------------
            elif "Bl " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
                      
            elif ("Wl " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Deleted Banned")
                   except:
                      pass                    

            elif "Ban all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Ban all","")
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                   except:
                                       cl.sentText(msg.to,"")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "▪ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"BLACKLIST USER :\n===============\n\n"+ mc + "\nƬƠƬƛL: " + str(len(wait["blacklist"]))+ " users\n\nRead time: \n" + datetime.today().strftime('%H:%M:%S')+"\n===============")
            elif msg.text in ["Gbl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "・" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,"ƁԼƛƇƘԼƖSƬ ƲSЄƦ :\n===============\n\n"+ cocoa + "\nList of the blacklist.。")
#---------------------------------------------------
            elif msg.text in ["Clearban"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Clear ban "+ str(len(wait["blacklist"]))+" user\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                wait["blacklist"] = {}
                cl.sendText(msg.to,"")

            elif msg.text in ["Clear mimic"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Sukses clear "+ str(len(mimic["target"]))+ " mimic target")
                mimic["target"] = {}
                cl.sendText(msg.to,"")
#-----------------------------------------------
            elif msg.text in ["Killban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,ks,kc,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass							
#-----------------------------------------------
            elif "Copy @" in msg.text:
                print "[Copy] OK"
                _name = msg.text.replace("Copy @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                    for target in targets:
                        try:
                            cl.CloneContactProfile(target)
                            cl.sendText(msg.to, "Success Copy profile\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        except Exception as e:
                            print e

            elif msg.text in ["Backup","backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Profile done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                except Exception as e:
                    cl.sendMessage(msg.to, str(e))

            elif "Wib1 copy @" in msg.text:
                print "[Copy] OK"
                _name = msg.text.replace("K1 copy @","")
                _nametarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                    for target in targets:
                        try:
                            ki.CloneContactProfile(target)
                            ki.sendText(msg.to, "Success Copy profile\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        except Exception as e:
                            print e

            elif msg.text in ["Wib1 backup"]:
                try:
                    ki.updateDisplayPicture(backup1.pictureStatus)
                    ki.updateProfile(backup1)
                    ki.sendText(msg.to, "Backup Profile done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                except Exception as e:
                    ki.sendMessage(msg.to, str(e))
                    ki.sendMessage(msg.to, "Backup Profile done ~")

            elif "Wib2 copy @" in msg.text:
                print "[Copy] OK"
                _name = msg.text.replace("K2 copy @","")
                _nametarget = _name.rstrip(' ')
                gs = kk.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                    for target in targets:
                        try:
                            kk.CloneContactProfile(target)
                            kk.sendText(msg.to, "Success Copy profile\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                        except Exception as e:
                            print e

            elif msg.text in ["Wib2 backup"]:
                try:
                    kk.updateDisplayPicture(backup2.pictureStatus)
                    kk.updateProfile(backup2)
                    kk.sendText(msg.to, "Backup Profile done\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                except Exception as e:
                    kk.sendText(msg.to, str(e))
#----------------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
#------------------------------------------------------------------
            elif "Getvid" in msg.text:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                  for target in targets:
                      try:
                          contact = cl.getContact(target)
                          path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                          cl.sendVideoWithURL(msg.to, path)
                      except Exception as e:
                          print e
#------------------------------------------------------------------			
            elif "Getpict @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Getname @" in msg.text:
                 _name = msg.text.replace("Getname @","")
                 _nametarget = _name.rstrip(" ")
                 gs = cl.getGroup(msg.to)
                 for h in gs.members:
                   if _nametarget == h.displayName:
                      cl.sendText(msg.to, h.displayName )
                   else:
                     pass

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"✴ Nama: " + contact.displayName + "\n\n✴ Mid:\n" + contact.mid + "\n\n✴ Bio:\n" + contact.statusMessage + "\n\n✴ Profile Picture:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n✴ Header:\n" + str(cu))
                except:
                    cl.sendText(msg.to,"✴ Nama: " + contact.displayName + "\n\n✴ Mid:\n" + contact.mid + "\n\n✴ Bio:\n" + contact.statusMessage + "\n\n✴ Profile Picture:\n" + str(cu))
            
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"☑ Nama: " + contact.displayName + "\n\n☑ Bio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"☑ Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"☑ Profile Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
#------------------------------------------------------------------
            elif "Pictgroup" in msg.text:    
                    print "[Command]dp executing"
                    try:
                        ginfo = cl.getGroup(msg.to)
                        path = "http://dl.profile.line-cdn.net/" + ginfo.pictureStatus
                        cl.sendImageWithURL(msg.to, path)
                    except:
                        pass
                    print "[Command]dp executed"

            elif "Mypict" in msg.text:    
                    print "[Command]dp executing"
                    try:
                        ginfo = cl.getProfile()
                        path = "http://dl.profile.line-cdn.net/" + ginfo.pictureStatus
                        cl.sendImageWithURL(msg.to, path)
                    except:
                        pass
                    print "[Command]dp executed"

            elif "Mycover" in msg.text:    
                    print "[Command]dp executing"
                    try:
                        h = cl.getContact(mid)
                        cu = cl.channel.getCover(mid)
                        path = str(cu)
                        cl.sendImageWithURL(msg.to, path)
                    except:
                        pass
                    print "[Command]dp executed"

            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
#--------------------[Pict Group pake nama grup]---------------------
            elif "Cover group " in msg.text:
                saya = msg.text.replace('Cover group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#------------------------------------------------------------------
            elif "ytb: " in msg.text.lower():
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Yt-mp4: " in msg.text:
                #if msg.from_ in admin:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           #cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           video = pafy.new(isi[0])
                           best = video.getbest(preftype="mp4")
                           s = best.url
                           hasil = video.title
                           hasil += '\n Like : ' + str(video.likes)
                           hasil += '\n Dislike : ' + str(video.dislikes)
                           hasil += '\n Durasi : ' + str(video.duration)
                           hasil += '\n Rating : ' + str(video.rating)
                           hasil += '\n Kategori : ' + str(video.category)
                           hasil += '\n Video Length : ' + str(video.length)
                           hasil += '\n Di Upload Oleh : ' + str(video.author)
                           cl.sendText(msg.to, hasil)
                           cl.sendImageWithURL(msg.to, video.thumb)
                           cl.sendText(msg.to, "Please wait for video download.. !!")
                           cl.sendVideoWithURL(msg.to, s)
                   except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Yt-mp3: " in msg.text:
                #if msg.from_ in admin:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           #cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           video = pafy.new(isi[0])
                           best = video.getbest(preftype="mp4")
                           s = best.url
                           hasil = video.title
                           hasil += '\n Like : ' + str(video.likes)
                           hasil += '\n Dislike : ' + str(video.dislikes)
                           hasil += '\n Durasi : ' + str(video.duration)
                           hasil += '\n Rating : ' + str(video.rating)
                           hasil += '\n Kategori : ' + str(video.category)
                           hasil += '\n Video Length : ' + str(video.length)
                           hasil += '\n Di Upload Oleh : ' + str(video.author)
                           cl.sendText(msg.to, hasil)
                           cl.sendImageWithURL(msg.to, video.thumb)
                           cl.sendText(msg.to, "Please wait for video download.. !!")
                           cl.sendVideoWithURL(msg.to, s)
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Musik: " in msg.text:
                songname = msg.text.replace("/music: ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to, "Judul: "+ song[0].encode('utf-8') + "\nDurasi: "+ song[1].encode('utf-8') +"\nLink download: " + song[4].encode('utf-8') + "\n\nWaiting for audio.. !!")
                    cl.sendAudioWithURL(msg.to, song[4])

            elif "Music: " in msg.text:
                songname = msg.text.replace("/musrik: ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') + "\n\n" + lyric)
                    cl.sendText(msg.to, "Tunggu untuk mendengarkan audio...")
                    cl.sendAudioWithURL(msg.to,song[4])
                    cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0].encode('utf-8'))
#--------------------------------- TRANSLATE --------------------------------
            elif "Tr id " in msg.text:
                isi = msg.text.replace("Tr id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr en " in msg.text:
                isi = msg.text.replace("Tr en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr fr " in msg.text:
                isi = msg.text.replace("Tr fr ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='fr')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr ar " in msg.text:
                isi = msg.text.replace("Tr ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr cn " in msg.text:
                isi = msg.text.replace("Tr cn ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-CN')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr de " in msg.text:
                isi = msg.text.replace("Tr de ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='de')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr hi " in msg.text:
                isi = msg.text.replace("Tr hi ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr jp " in msg.text:
                isi = msg.text.replace("Tr jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr jw " in msg.text:
                isi = msg.text.replace("Tr jw ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr su " in msg.text:
                isi = msg.text.replace("Tr su ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='su')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr ms " in msg.text:
                isi = msg.text.replace("Tr ms ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ms')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr vi " in msg.text:
                isi = msg.text.replace("Tr vi ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='vi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr ko " in msg.text:
                isi = msg.text.replace("Tr ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr th " in msg.text:
                isi = msg.text.replace("Tr th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
#-----------------------------------------------
            elif "Lyric: " in msg.text:
                songname = msg.text.replace("/lyric: ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') + "\n\n" + lyric)
#-----------------------------------------------
            elif 'wiki: ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wiki: ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))

            elif 'insta: ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/insta: ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    cl.sendImageWithURL(msg.to, text1[0])
                    cl.sendText(msg.to, user + user1 + followers + following + post + link)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))

            elif "Image: " in msg.text:
                  start = time.time()
                  keyword = msg.text[6:]
                  key = keyword.strip('@#$&?!/_,*"\£¢€¥^°={}~`|•√π÷×¶∆<>`[]|;')
                  search = key.replace(' ','%20')
                  url = 'https://www.google.com/search?q=' + search +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                  raw_html =  (download_page(url))
                  items = []
                  items = items + (_images_get_all_items(raw_html))
                  path = random.choice(items)
                  elapsed_time = time.time() - start
                  try:
                      cl.sendImageWithURL(msg.to,path)
                  except:
                     pass
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "Success Invite Creator Group ~"
                 except:
                    pass
#----------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya ▶  " + tanya + "  ◀ adalah :  " + jawaban + "\nBanyak banyak amal ya Nak ")
#---------------------------------#
            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak punya")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya ▶  " + tanya + "  ◀ adalah :  " + jawaban + "\nSegera tobatlah Nak")
	#-------------------------------#
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Iya","Tidak","Bisa jadi","Mungkin saja"," Ora ngerti")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------------------
            elif "Kapankah " in msg.text:
                  tanya = msg.text.replace("Kapankah ","")
                  jawab = ("Besok","Besok Lusa","Nanti malam","Besok pagi","Kapan kapan","Gak akan pernah","Masih lama")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------------------
            elif "Sudahkah " in msg.text:
                  tanya = msg.text.replace("Sudahkah ","")
                  jawab = ("Belum","Sudah","Masih males","Nanti saja")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------------------
            elif "Say: " in msg.text:
                  tanya = msg.text.replace("/say: ","")
                  tts = gTTS(text=tanya, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------------------
            elif "text: " in msg.text.lower():
                txt = msg.text.replace("/text: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)
#-----------------------------------------------------------
            elif "Gift " in msg.text:
                strnum = msg.text.replace("Gift ","")
                num = int(strnum)
                for var in range(0,num):
                	try:
                    	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                 'PRDTYPE': 'THEME',
                                 'MSGTPL': '10'}
                           msg.text = None
                           cl.sendMessage(msg)
                           print "SEND STICKER"
                        except:
                 	   pass

            elif msg.text.lower() == 'welkam':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name) + "\n\nOwner Grup: " + ginfo.creator.displayName+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam added\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam " in msg.text:
                strnum = msg.text.replace("Spam ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
#-----------------------------------------------------------
            elif msg.text in ["Single"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I have feigned and have canceled it。")
            elif "Random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "Album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made。")
                except:
                    cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "fakec→" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakec→","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass                
#-----------------------------------------------
            elif msg.text in ["Say "]:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    kk.sendText(msg.to," " + string + " ")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed","Desah"]:
                fake=["0.060653985673451...Detik","0.06812087588903164...Detik","0.07064537864566...Detik","0.07209868645890...Detik"]
                fspeed=random.choice(fake)
                cl.sendText(msg.to," Progress.....")
                cl.sendText(msg.to,(fspeed))  
                ki.sendText(msg.to,(fspeed))  
                kk.sendText(msg.to,(fspeed)) 
#-----------------------------------------------             
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"OK Boss 􀨁􀄻double thumbs up􏿿")
                kk.sendText(msg.to,"OK Boss 􀨁􀄻double thumbs up􏿿")

            elif msg.text in ["Bot like"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Auto Like Is Running")
                try:
                  likefriend()
                except:
                  pass
#-------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = random.choice(KAC).getGroup(op.param1)                        
                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = [cl,ki,kk]
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in mid:
                    if op.param2 in Bmid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)

                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)

                if op.param3 in Amid:
                    if op.param2 in Bots:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                    else:
                        G = random.choice(KAC).getGroup(op.param1)                        
                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        wait["blacklist"][op.param2] = False
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in Bmid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)

                if op.param3 in Bmid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Bmid:
                    if op.param2 in Bots:
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                    else:
                        G = random.choice(KAC).getGroup(op.param1)                        
                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(G)
                        Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        wait["blacklist"][op.param2] = False
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        if op.param4 in Bmid:
                            if op.param5 in Bots:
                                G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
            except:
                pass
             
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
                    
        if op.param1 in autocancel:
          if op.param2 not in Bots:
			if op.param2 in Bots:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				cl.cancelGroupInvitation(op.param1,InviterX)
				ki.cancelGroupInvitation(op.param1,InviterX)
				kk.cancelGroupInvitation(op.param1,InviterX)
				cl.kickoutFromGroup(op.param1,[op.param2])
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#------------------------------------------------------------------------------------
        if op.type == 55:
            if op.param1 in wait3['readpoint']:
                if op.param2 in wait3['readMember'][op.param1]:
                    pass
                else:
                    wait3['readMember'][op.param1][op.param2] = True
            else:
                pass 

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
#-------------------------------------Cek Sider------------------------------
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                #cl.mention(op.param1, op.param2)
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Jangan ngintip ae " +nick[0]+"!!!\n"+str(wait["read"]))
                                        #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                    else:
                                        cl.sendText(op.param1, "Jangan ngintip ae " +nick[1]+"!!!\n"+str(wait["read"]))
                                        #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                                else:
                                    cl.sendText(op.param1, "Jangan ngintip ae " +Name+"\n"+str(wait["read"]))
                                    #random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
#-------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,100):
        hasil = cl.activity(limit=100)
    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try: 
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'])
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'])
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'])
            print "Like"
        except:
            pass
    else:
        print "Already Liked"
        time.sleep(500)

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[7:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
#------------------------------------
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
