#qpy:console
import sys
import select
import socket
import time
import random
import threading
import os
import platform
import random
import urlparse
import BaseHTTPServer
import SocketServer
import urllib, urllib2, zlib, os, errno, base64, re, thread

print ('www.siberyazilimci.net')
		
def oku(adres,isim):
  
  proxy_support = urllib2.ProxyHandler({"http":"127.0.0.1:8080"})
  opener = urllib2.build_opener(proxy_support)
  urllib2.install_opener(opener)
  url="http://"+adres.replace("http://","")
  urls=urllib2.Request(url)
  urls.add_header("hakan","naber")
  print (urls.headers)
  try:
   kaynak = urllib2.urlopen(urls)
  except:
   d.makeToast("link bulunamadi sayfayi yenileyinn")
  if(url.find("watch?")>-1):
   print (url)
   kaynak=kaynak.read()
   isim=kaynak.split("<title>")[1].split("</title>")[0]
   kaynak=kaynak.split("stream_map\": \"")[1].split('"')[0];
   kaynak=urllib2.unquote(kaynak.decode()).replace("\u0026","&")
   kaynak=kaynak.split(",")
   for b in kaynak:
    
    if(b.find("itag=18")>-1 and b.find("url=")>-1):
     #d.setClipboard(b)
     url2=b.split("url=")[1].split("?")[0]
     sparams=b.split("sparams=")[1].split("&")[0]
     #d.setClipboard(b.split("url=")[1])
     try:
       signature=b.split("signature=")[1].split("&")[0]
     except:
       link="http://www.ytapi.com/api/"+url.split("v=")[1]+"/direct/18/"
       d.view("http://127.0.0.1:8080/"+link,"video/*")
       d.setClipboard(link)
       return
     #signature=WD(signature)
     print (signature)
     key=b.split("key=")[1].split("&")[0]
     y=sparams.split("%2C")
     link=url2+"?sparams="+sparams+"&signature="+signature+"&key="+key
     for i in y:
      link+="&"+i+"="+b.split(i+"=")[1].split("&")[0]
     print (link)
     #oku(link, isim)
     d.view("http://127.0.0.1:8080/"+link,"video/*")
     d.setClipboard(link)
     return
  else:
     indir(kaynak, isim)
   
def isimduzelt(x):
  liste=[":","*","?","/","\\","<",">","|","\""]
  for i in liste:
   x=x.replace(i," ")
  return x
 
def indir(kaynak, isim):
      yol="/sdcard/pGoogle/"
      if(os.path.isdir(yol)==False):
        os.mkdir(yol)
      isim=yol+isimduzelt(isim)+".mp4"
      d.makeToast(isim)
      sayi=0
      k=1024*16
      sayi2=0
      file=open(isim, "wb")
      toplam=int(kaynak.info().getheaders("Content-Length")[0])
      print (toplam)
      while True:
        inen=kaynak.read(k)
        if not inen: break
        sayi=sayi+k
        ind=(sayi/(toplam+0.0))*100
        if(ind>sayi2):
         d.makeToast("%"+str(ind).split(".")[0]+" indirildi")
         sayi2+=1
        file.write(inen)
      file.close()
      d.makeToast("dosya indirildi")


def WD(a): 
 a=list(a)
 a=a[::-1]
 a=a[1:]
 a=a[::-1]
 a=a[3:]
 a=XD(a,19)
 a=a[::-1]
 a=XD(a,35)
 a=XD(a,61)
 a=a[2:]
 return "".join(a) 
global XD 
def XD(a,b): 
 c=a[0]
 a[0]=a[b%len(a)]
 a[b]=c
 return a

#oku(d.getClipboard().result,"")
def izle(x):
    d.view(x, "video/*")

ru = lambda text: text.decode('utf-8', 'ignore')
cihaz=platform.system()
if(cihaz=="Linux"):
    x="/sdcard/com.hipipal.qpyplus/scripts/simple"
elif(cihaz=="Android"):
    x=""
else:
    x=""
ru = lambda text: text.decode('utf-8', 'ignore')
ur = lambda text: text.encode('utf-8', 'ignore')
class Info:
    def __init__(self, get):
        self.get = get
    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'Simple Server'
        if self.get.lower() == 'about':
            return 'Windows Version'
        if self.get.lower() == 'ver':
            return '1.00.10'
        if self.get.lower() == 'date':
            return '22/07/2013'
        if self.get.lower() == 'by':
            return 'InunxLABS'
        if self.get.lower() == 'mail':
            return 'inunxlabs@gembox.us'
class Pinger:
    def __init__(self):
        self.sets = Sets()
        self.host = []
        for server in self.sets.KEEP.split('|'):
            if server:
                self.host.append(server)
    def check(self):
        if self.host:
            try:
                request = urllib2.Request('http://%s/' % self.host[random.randint(0, len(self.host) - 1)])
                request.add_header('Accept-Encoding', 'identity, *;q=0')
                request.add_header('Connection', 'close')
                proxy_handler = urllib2.ProxyHandler({'http': '%s:%s' % ('127.0.0.1', self.sets.LPORT)})
                opener = urllib2.build_opener(proxy_handler)
                urllib2.install_opener(opener)
                urllib2.urlopen(request)
            except:
                pass
name = '%s.ini' % Info('name').get_info().replace(' ', '')
path = '/' 
#conf = '%s%s%s' % (os.getcwd(), path, name)
#conf=x+conf
class Sets:
    def __init__(self):
        self.LHOST = '127.0.0.1'
        self.LPORT = 8080
        self.FQUERY = ''
        self.MQUERY = ''
        self.BQUERY = ''
        self.RQUERY = ''
        self.CQUERY = ''
        self.IQUERY = ''
        self.IMETHOD = 1
        self.ILINE = 0
        self.ISPLIT = 5
        self.RPORT = 0
        self.RPATH = 0
        self.ADMODE = 0
        self.CUSHDR0 = ''
        self.VALHDR0 = ''
        self.CUSHDR1 = ''
        self.VALHDR1 = ''
        self.CUSHDR2 = ''
        self.VALHDR2 = ''
        self.CUSHDR3 = ''
        self.VALHDR3 = ''
        self.KEEP = ''
        self.RHTTP = 0
        self.RHTTPS = 1
        self.SBUFF = 1024
        self.TIMEOUT = 60
        self.PHOST = '13.95.85.114'
        self.PPORT = 3128
        self.PTYPE = 0
        #self.load()
    def load(self):
        try:
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)
        except:
            self.save()
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)
    def save(self):
        data = ''
        for name in self.__dict__.keys():
            line = name + ' = ' + repr(self.__dict__[name]) + '\r\n'
            data += line
        open(conf, 'wb').write(ur(data))
        del data	

if getattr(socket, 'socket', None) is None:
    raise ImportError('socket.socket missing, proxy support unusable')
ra = lambda text: text.decode('ascii', 'ignore')
_defaultproxy = None
_orgsocket = socket.socket
class ProxyError(Exception):
    pass
class GeneralProxyError(ProxyError):
    pass
class HTTPSError(ProxyError):
    pass
_generalerrors = ('success', 'invalid data', 'not connected', 'not available', 'bad proxy type', 'bad input')
def setdefaultproxy(proxytype = None, addr = None, port = None, rdns = True, username = None, password = None, useragent = None):
    global _defaultproxy
    _defaultproxy = (proxytype,
     addr,
     port,
     rdns,
     username,
     password,
     useragent)
def wrapmodule(module):
    if _defaultproxy != None:
        module.socket.socket = socksocket
    else:
        raise GeneralProxyError((4, 'no proxy specified'))
    return
class socksocket(socket.socket):

    def __init__(self, family = socket.AF_INET, tipe = socket.SOCK_STREAM, proto = 0, _sock = None, headers = None, newline = None):
        _orgsocket.__init__(self, family, tipe, proto, _sock)
        if _defaultproxy != None:
            self.__proxy = _defaultproxy
        else:
            self.__proxy = (None, None, None, None, None, None, None)
        self.__proxysockname = None
        self.__proxypeername = None
        self.__httptunnel = True
        self.__headers = headers
        self.__newline = newline
        return
    def __recvall(self, count):
        data = self.recv(count)
        while len(data) < count:
            d = self.recv(count - len(data))
            if not d:
                raise GeneralProxyError((0, 'connection closed unexpectedly'))
            data = data + d
        return data
    def sendall(self, content, *args):
        if not self.__httptunnel:
            content = self.__rewriteproxy(content)
        return super(socksocket, self).sendall(content, *args)
    def __rewriteproxy(self, header):
        host, endpt = (None, None)
        hdrs = header.split('%s' % self.__newline)
        for hdr in hdrs:
            if hdr.lower().startswith('host:'):
                host = hdr
            elif hdr.lower().startswith('get') or hdr.lower().startswith('post'):
                endpt = hdr
        if host and endpt:
            hdrs.remove(host)
            hdrs.remove(endpt)
            host = host.split(' ')[1]
            endpt = endpt.split(' ')
            if self.__proxy[4] != None and self.__proxy[5] != None:
                hdrs.insert(0, self.__getauthheader())
            hdrs.insert(0, 'Host: %s' % host)
            hdrs.insert(0, '%s http://%s%s %s' % (endpt[0],
             host,
             endpt[1],
             endpt[2]))
        return '%s' % self.__newline.join(hdrs)
    def __getauthheader(self):
        auth = self.__proxy[4] + ':' + self.__proxy[5]
        return 'Proxy-Authorization: Basic ' + base64.b64encode(auth)
    def setproxy(self, proxytype = None, addr = None, port = None, rdns = True, username = None, password = None, useragent = None):
        self.__proxy = (proxytype,
         addr,
         port,
         rdns,
         username,
         password,
         useragent)
    def getproxysockname(self):
        return self.__proxysockname
    def getproxypeername(self):
        return _orgsocket.getpeername(self)
    def getpeername(self):
        return self.__proxypeername
    def __negotiatehttp(self, destaddr, destport):
        if not self.__proxy[3]:
            addr = socket.gethostbyname(destaddr)
        else:
            addr = destaddr
        if self.__headers:
            headers = [self.__headers]
        else:
            headers = ['CONNECT ',
             addr,
             ':',
             str(destport),
             ' HTTPS/1.1%s' % self.__newline]
            headers += ['Host: ', destaddr, '%s' % self.__newline]
            if self.__proxy[6] is not None:
                headers += ['User-Agent: ', unicode(self.__proxy[6]), '%s' % self.__newline]
        if self.__proxy[4] != None and self.__proxy[5] != None:
            headers += [self.__getauthheader(), '%s' % self.__newline]
        headers.append('%s' % self.__newline)
        self.sendall(ra(''.join(headers).encode()))
        resp = self.recv(1)
        while resp.find('\r\n\r\n'.encode()) == -1:
            resp = resp + self.recv(1)
        self.__proxysockname = ('0.0.0.0', 0)
        self.__proxypeername = (addr, destport)
        return
    def connect(self, destpair):
        if type(destpair) not in (list, tuple) or len(destpair) < 2 or not isinstance(destpair[0], basestring) or type(destpair[1]) != int:
            raise GeneralProxyError((5, _generalerrors[5]))
        if self.__proxy[0] == 0:
            if self.__proxy[2] != None:
                portnum = self.__proxy[2]
            else:
                portnum = 8080
            _orgsocket.connect(self, (self.__proxy[1], portnum))
            _ports = (22, 443, 465, 563, 585, 587, 636, 706, 993, 995, 2083, 2211, 2483, 2949, 4747, 6679, 6697, 8883, 19999)
            if destpair[1] in _ports:
                self.__negotiatehttp(destpair[0], destpair[1])
            else:
                self.__httptunnel = True
        elif self.__proxy[0] == 1:
            if self.__proxy[2] != None:
                portnum = self.__proxy[2]
            else:
                portnum = 8080
            _orgsocket.connect(self, (self.__proxy[1], portnum))
            self.__negotiatehttp(destpair[0], destpair[1])
        elif self.__proxy[0] == None:
            _orgsocket.connect(self, (destpair[0], destpair[1]))
        else:
            raise GeneralProxyError((4, _generalerrors[4]))
        return
t=int(time.time())
x=urllib2.ProxyHandler({"http":"127.0.0.1:8080"})
y=urllib2.build_opener(x)
urllib2.install_opener(y)
ra = lambda text: text.decode('ascii', 'ignore')
sets = Sets()
logs = False
def ServerUpdate():
    global sets
    sets = Sets()
def LogWindow(flag = False):
    global logs
    logs = flag
class QueryHandler():
    def __init__(self, command = '', path = '/', headers = {}, https = False, phost = '', pport = 0):
        self.command = command
        self.path = path
        self.headers = headers
        self.https = https
        self.phost = phost
        self.pport = pport
    def get_path(self, path):
        if '/' in path:
            host, path = path.split('/', 1)
            path = '/%s' % path
        else:
            host = path
            path = '/'
        fport = False
        if self.https:
            port = 443
        else:
            port = 80
        if ':' in host:
            _host, _port = host.rsplit(':', 1)
            try:
                port = int(_port)
                host = _host
                fport = True
            except:
                pass
        return (fport,
         host,
         port,
         path)
    def get_query(self):
        if self.https:
            url = 'https://%s/' % self.path
        else:
            url = self.path
        url_scm, _, _, _, _, _ = urlparse.urlparse(url)
        if len(sets.FQUERY.split('/')) > 2:
            cgi_http = 'http/'
            if cgi_http in sets.FQUERY.lower():
                url_cgi = url.split(cgi_http)
                if len(url_cgi) > 1:
                    url = '%s://%s' % (url_scm, url_cgi.pop())
            else:
                url = url.replace(sets.FQUERY, '')
        if len(sets.MQUERY.split('/')) > 2:
            url = url.replace(sets.MQUERY, '')
        if len(sets.BQUERY.split('/')) > 2:
            url = url.replace(sets.BQUERY, '')
        url_len = len(url_scm) + 3
        url_path = url[url_len:]
        if sets.CQUERY:
            cquery_list = sets.CQUERY.split('|')
            for cquery in cquery_list:
                try:
                    old, new = cquery.split('>')
                    url_path = url_path.replace(old, new)
                except:
                    pass
        fport, host, port, path = self.get_path('%s%s' % (sets.FQUERY, url_path))
        advhost = host
        if fport and not sets.RPORT:
            path = '%s:%s%s%s%s' % (host,
             port,
             sets.MQUERY,
             path,
             sets.BQUERY)
        else:
            path = '%s%s%s%s' % (host,
             sets.MQUERY,
             path,
             sets.BQUERY)
        fport, host, port, path = self.get_path(path)
        if self.https:
            fport = True
            path = '%s:%s' % (host, port)
        elif self.phost and self.pport or sets.ADMODE:
            if sets.RQUERY:
                if sets.MQUERY.startswith('/'):
                    path = '%s%s%s' % (url[:url_len], sets.RQUERY, path)
                else:
                    path = '%s%s%s%s' % (url[:url_len],
                     sets.RQUERY,
                     sets.MQUERY,
                     path)
            elif fport and not sets.RPORT:
                path = '%s%s:%s%s' % (url[:url_len],
                 host,
                 port,
                 path)
            else:
                path = '%s%s%s' % (url[:url_len], host, path)
        else:
            _, path = path.split('/', 1)
            path = '/%s' % path
        cur_header = 'proxy-connection'
        if cur_header in self.headers and not self.phost and not self.pport:
            del self.headers[cur_header]
        cur_header = 'connection'
        if not self.https and not sets.PTYPE:
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = 'close'
        cur_header = 'host'
        if cur_header in self.headers:
            del self.headers[cur_header]
            if fport and not sets.RPORT and not self.https:
                self.headers[cur_header] = '%s:%s' % (host, port)
            else:
                self.headers[cur_header] = host
        if sets.RQUERY:
            cur_header = 'host'
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = sets.RQUERY
            cur_header = 'x-online-host'
            if cur_header in self.headers:
                del self.headers[cur_header]
            if fport and not self.https:
                self.headers[cur_header] = '%s:%s' % (host, port)
            else:
                self.headers[cur_header] = '%s' % host
        if sets.ADMODE:
            cur_header = 'host'
            if cur_header in self.headers:
                if sets.RQUERY:
                    del self.headers[cur_header]
                    self.headers[cur_header] = '%s' % sets.RQUERY
                    cur_header = 'x-online-host'
                    if cur_header in self.headers:
                        del self.headers[cur_header]
                    if fport and not self.https:
                        self.headers[cur_header] = '%s:%s' % (advhost, port)
                    else:
                        self.headers[cur_header] = '%s' % advhost
                elif self.phost and self.pport:
                    del self.headers[cur_header]
                    advhost = advhost.replace(sets.FQUERY, '').replace(sets.MQUERY, '').replace(sets.BQUERY, '')
                    if fport and not self.https:
                        self.headers[cur_header] = '%s:%s' % (advhost, port)
                    else:
                        self.headers[cur_header] = '%s' % advhost
        if sets.CUSHDR0 and not sets.VALHDR0:
            cur_header = sets.CUSHDR0.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
        if sets.CUSHDR0 and sets.VALHDR0:
            cur_header = sets.CUSHDR0.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = sets.VALHDR0
        if sets.CUSHDR1 and not sets.VALHDR1:
            cur_header = sets.CUSHDR1.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
        if sets.CUSHDR1 and sets.VALHDR1:
            cur_header = sets.CUSHDR1.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = sets.VALHDR1
        if sets.CUSHDR2 and not sets.VALHDR2:
            cur_header = sets.CUSHDR2.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
        if sets.CUSHDR2 and sets.VALHDR2:
            cur_header = sets.CUSHDR2.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = sets.VALHDR2
        if sets.CUSHDR3 and not sets.VALHDR3:
            cur_header = sets.CUSHDR3.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
        if sets.CUSHDR3 and sets.VALHDR3:
            cur_header = sets.CUSHDR3.lower()
            if cur_header in self.headers:
                del self.headers[cur_header]
            self.headers[cur_header] = sets.VALHDR3
        if sets.RPORT:
            cur_port = ':%s' % port
            path = path.replace(cur_port, '')
            cur_list = ('host', 'x-online-host')
            for cur_header in cur_list:
                if cur_header in self.headers and ':' in self.headers[cur_header]:
                    rhost, _ = self.headers[cur_header].split(':')
                    del self.headers[cur_header]
                    self.headers[cur_header] = rhost
        header = self.headers
        uahdr = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        cur_header = 'user-agent'
        if cur_header in self.headers:
            uahdr = self.headers[cur_header]
        self.del_garbage()
        return (path,
         header,
         uahdr,
         host,
         port,
         advhost)
    def del_garbage(self):
        del self.command
        del self.path
        del self.headers
        del self.https
        del self.phost
        del self.pport
class ProxyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def __getattr__(self, item):     
        if(self.path.find("youtube.com")>-1 and self.path.find("itag=22")<0 or self.path.find("pastebin")>-1 or self.path.find("xhamster")>-1): 
           return self.do_METHOD
        elif item.startswith('do_'):
           return self.do_COMMAND
    def do_COMMAND(self):
        #d.makeToast(self.path)
        self.get_urlcheck()
        self.get_headercheck()
        self.get_recv_headers()
        self.get_proxy()
        query = QueryHandler(self.command, self.path, self.headers, self.https, self.phost, self.pport)
        self.path, self.headers, self.uahdr, self.host, self.port, self.advhost = query.get_query()
        self.get_newline()
        self.get_requestline()
        self.get_injectline()
        self.get_send_inject()
        self.get_send_headers()
        soc = self.proxy_sock()
        try:           
             if self.connect_to(soc, self.host, self.port, self.advhost):
                data = ra('%s%s' % (self.get_injectline(), self.newline)).encode('hex')
                for header, value in self.headers.items():
                    data += ra('%s: %s%s' % (str(header).title(), value, self.newline)).encode('hex')
                post_header = 'content-length'
                if post_header in self.headers:
                    data += ra(self.newline).encode('hex')
                    data += self.rfile.read(int(self.headers[post_header])).encode('hex')
                    data += ra(self.newline).encode('hex')
                data += ra('%s%s' % (self.newline, self.get_send_end())).encode('hex')
                data = data.decode('hex')
                while data:
                    byte = soc.send(data)
                    data = data[byte:]
                self.get_response_data(soc)
                self.send_connection_close(soc)
                self.del_garbage()
        except socket.error as msg:
            self.send_connection_error(msg)
            self.send_connection_close(soc)
            return
        except:
            return
    def do_CONNECT(self):
        if sets.RHTTPS:
            self.get_urlcheck()
            self.get_headercheck()
            self.get_recv_headers()
            self.get_proxy()
            query = QueryHandler(self.command, self.path, self.headers, self.https, self.phost, self.pport)
            self.path, self.headers, self.uahdr, self.host, self.port, self.advhost = query.get_query()
            self.get_newline()
            self.get_requestline()
            self.get_injectline()
            self.get_send_inject()
            self.get_send_headers()
            soc = self.proxy_sock()
            try:
                if self.connect_to(soc, self.host, self.port, self.advhost):
                    data = '%s 200 Connection Established\r\nProxy-Agent: %s/%s' % (self.request_version, Info('name').get_info().replace(' ', ''), Info('ver').get_info()[:3])
                    self.send_response_data('%s\r\n' % data)
                    self.send_response_data('\r\n')
                    self.get_response_header(data)
                    self.get_response_data(soc)
                    self.send_connection_close(soc)
                    self.del_garbage()
            except socket.error as msg:
                self.send_connection_error(msg)
                self.send_connection_close(soc)
                return
            except:
                return
        else:
            self.send_connection_error((501, 'method not allowed'))
            self.connection.close()
            return
    def get_urlcheck(self):
        global t
        self.https = False
        if self.command == 'CONNECT':
            self.https = True
        if(self.path.find(".mp5")>0 or self.path.find(".flv")>-1 or self.path.find("video/mp4")>-1):
         if(self.headers["User-Agent"].find("Python")<0 and int(time.time())>t+3):
           d.setClipboard(self.path)
           d.makeToast("indirme linki kopyalandi, isterseniz tarayiciya yapistirip indirebilirsiniz")
           t=int(time.time())
           d.vibrate()
           if(self.path.find("video/mp4")>-1):
             d.makeToast(str(self.headers))
             thread.start_new_thread(oku(self.headers["Referer"],"",))
           else:
             print (6)
             thread.start_new_thread(izle("http://127.0.0.1:8088/"+self.path,))
             self.connection_close()
           return
    def hakanyeni(self):
        d.makeToast(self.path)
        path="http://"+self.path.split("/http://")[1]
        cur_pos = 0
        part_length = 0x100000 # 1m initial, at least 64k
        first_part = True
        content_length = 0
        text_content = True
        allowed_failed = 10
        while allowed_failed > 0:
            next_pos = 0
            self.headers["Range"] = "bytes=%d-%d" % (cur_pos, cur_pos + part_length - 1)
            # create request for GAppProxy
            params = urllib.urlencode({"method": "GET",
                                       "encoded_path": base64.b64encode(path),
                                       "headers": base64.b64encode(str(self.headers)),
                                       "postdata": base64.b64encode(""),
                                       "version": "1.0.5"})
            # accept-encoding: identity, *;q=0
            # connection: close
            request = urllib2.Request(fetch_server)
            request.add_header("Accept-Encoding", "identity, *;q=0")
            request.add_header("Connection", "close")
            # create new opene
            local_proxy=""
            if local_proxy != "":
                proxy_handler = urllib2.ProxyHandler({"http": local_proxy})
            else:
                proxy_handler = urllib2.ProxyHandler({"http","127.0.0.1:8080"})
            opener = urllib2.build_opener(proxy_handler)
            # set the opener as the default opener
            urllib2.install_opener(opener)
            resp = urllib2.urlopen(request, params)
            # parse resp
            # for status line
            line = resp.readline()
            words = line.split()
            status = int(words[1])
            # not range response?
            if status != 206:
                # reduce part_length and try again
                if part_length > 65536:
                    part_length /= 2
                allowed_failed -= 1
                continue
            # for headers
            if first_part:
                self.send_response(200, "OK")
                while True:
                    line = resp.readline().strip()
                    # end header?
                    if line == "":
                        break
                    # header
                    (name, _, value) = line.partition(":")
                    name = name.strip()
                    value = value.strip()
                    # get total length from Content-Range
                    nl = name.lower()
                    if nl == "content-range":
                        m = re.match(r"bytes[ \t]+([0-9]+)-([0-9]+)/([0-9]+)", value)
                        if not m or int(m.group(1)) != cur_pos:
                            # Content-Range error, fatal error
                            return
                        next_pos = int(m.group(2)) + 1
                        content_length = int(m.group(3))
                        continue
                    # ignore Content-Length
                    elif nl == "content-length":
                        continue
                    # ignore Accept-Ranges
                    elif nl == "accept-ranges":
                        continue
                    self.send_header(name, value)
                    # check Content-Type
                    if nl == "content-type":
                        if value.lower().find("text") == -1:
                            # not text
                            text_content = False
                if content_length == 0:
                    # no Content-Length, fatal error
                    return
                self.send_header("Content-Length", content_length)
                self.send_header("Accept-Ranges", "none")
                self.end_headers()
                first_part = False
            else:
                while True:
                    line = resp.readline().strip()
                    # end header?
                    if line == "":
                        break
                    # header
                    (name, _, value) = line.partition(":")
                    name = name.strip()
                    value = value.strip()
                    # get total length from Content-Range
                    if name.lower() == "content-range":
                        m = re.match(r"bytes[ \t]+([0-9]+)-([0-9]+)/([0-9]+)", value)
                        if not m or int(m.group(1)) != cur_pos:
                            # Content-Range error, fatal error
                            return
                        next_pos = int(m.group(2)) + 1
                        continue
            # for body
            if text_content:
                data = resp.read()
                if len(data) > 0:
                    self.wfile.write(zlib.decompress(data))
            else:
                self.wfile.write(resp.read())

            # next part?
            if next_pos == content_length:
                return
            cur_pos = next_pos  
    def izleyeni(self):
       b=urllib2.Request(self.path)
       #b.add_header("Range","bytes=1566645-2987676")
       a=urllib2.urlopen(b)
       self.send_response(200)
       self.send_header("Content-Type","video/mp4")
       self.send_header("Accept-Ranges","bytes")
       self.end_headers()
       while True:
         c=a.read(1024*16)
         if not c:
           break
         self.wfile.write(c)
       self.connection_close()
       return
    def get_headercheck(self):
        header_check = {}
        for header, value in self.headers.items():
            if header.find('\t') == -1 and header.find('\t') == -1:
                header_check[str(header).lower()] = value
        self.headers = header_check
    def get_proxy(self):
        self.phost = ''
        self.pport = 0
        self.puser = None
        self.ppass = None
        if ':' in sets.PHOST and not sets.PPORT:
            plist = sets.PHOST.split('>')
            count = len(plist)
            while 1:
                count -= 1
                if count >= 0:
                    plist = plist[random.randint(0, len(plist) - 1)]
                    if '@' in plist and plist:
                        try:
                            self.puser, self.ppass = plist.split('@')[1].split(':')
                            plist = plist.split('@')[0]
                        except:
                            pass
                    if ':' in plist and plist:
                        try:
                            self.phost, self.pport = plist.split(':')
                            self.pport = int(self.pport)
                        except:
                            pass
                        break
                else:
                    break
        elif sets.PHOST and sets.PPORT:
            self.phost, self.pport = sets.PHOST, sets.PPORT
        return
    def proxy_sock(self):
        if sets.IQUERY and self.https or self.https:
            data = ra('%s%s' % (self.get_injectline(), self.newline))
            for header, value in self.headers.items():
                data += ra('%s: %s%s' % (str(header).title(), value, self.newline))
            soc = socksocket(headers=data, newline=self.newline)
        else:
            soc = socksocket(newline=self.newline)
        if self.phost and self.pport:
            soc.setproxy(sets.PTYPE, self.phost, self.pport, rdns=True, username=self.puser, password=self.puser, useragent=self.uahdr)
        return soc
    def connect_to(self, soc, host, port, advhost):
        try:
            if sets.ADMODE:
                host, port = advhost, port
            soc.setblocking(1)
            soc.connect((host, port))
            return 1
        except socket.error as msg:
            self.send_connection_error(msg)
            self.send_connection_close(soc)
            return 0
        except:
            return 0
    def get_newline(self):
        self.newline = ['   /\r\n', '\n'][sets.ILINE]
    def get_requestline(self):
        if sets.RHTTP == 1:
            self.request_version = 'HTTP/1.0'
        elif sets.RHTTP == 2:
            self.request_version = 'HTTP/1.1'
        self.requestline = '%s %s %s' % (self.command, self.path.replace("/http://","http://"), self.request_version)
    def get_injectline(self):
        if sets.IQUERY:
            meth = ['HEAD',
             'GET',
             'POST',
             'DELETE',
             'CONNECT',
             'OPTIONS',
             'TRACE',
             'PUT'][sets.IMETHOD]
            if '/' in sets.IQUERY:
                host, path = sets.IQUERY.split('/', 1)
                path = '/%s' % path
            else:
                host = sets.IQUERY
                path = '/'
            if self.phost and self.pport or sets.ADMODE:
                path = 'http://%s%s' % (host, path)
            self.splitline = self.newline * 3
            if sets.ISPLIT:
                self.splitline = self.newline * sets.ISPLIT
            self.injectline = '%s %s HTTP/1.1%sHost: %s%s' % (meth,
             path,
             self.newline,
             host,
             self.splitline)
            #print self.injectline
            return '%s%s' % (self.injectline, self.requestline)
        else:
            return self.requestline
    def get_send_end(self):
        if sets.IQUERY:
            return self.newline
        else:
            return ''
    def get_recv_headers(self):
        self.send_connection_logger('+++Receive Request+++\r\nFrom Address - %s:%s\r\n%s\r\n' % (self.client_address[0], self.client_address[1], self.requestline))
        for header, value in self.headers.items():
            self.send_connection_logger('%s: %s\r\n' % (str(header).title(), value))
        self.send_connection_logger('\r\n')
    def get_send_inject(self):
        if sets.IQUERY:
            self.send_connection_logger('+++Send Inject+++\r\n')
            if self.phost and self.pport:
                self.send_connection_logger('Using Proxy - %s:%s\r\n' % (self.phost, self.pport))
            elif sets.ADMODE:
                self.send_connection_logger('Using Host - %s:%s\r\n' % (self.advhost, self.port))
            else:
                self.send_connection_logger('Using Server - %s:%s\r\n' % (self.host, self.port))
            for inject in self.injectline.split(self.splitline)[0].split(self.newline):
                self.send_connection_logger('%s\r\n' % inject)
            self.send_connection_logger('\r\n')
    def get_send_headers(self):
        self.send_connection_logger('+++Send Request+++\r\n')
        if self.phost and self.pport:
            self.send_connection_logger('Using Proxy - %s:%s\r\n' % (self.phost, self.pport))
        elif sets.ADMODE:
            self.send_connection_logger('Using Host - %s:%s\r\n' % (self.advhost, self.port))
        else:
            self.send_connection_logger('Using Server - %s:%s\r\n' % (self.host, self.port))
        self.send_connection_logger('%s\r\n' % self.requestline)
        for header, value in self.headers.items():
            self.send_connection_logger('%s: %s\r\n' % (str(header).title(), value))
        self.send_connection_logger('\r\n')
    def find_double_newline(self, data):
        pos1 = data.find('\n\r\n')
        if pos1 >= 0:
            pos1 += 3
        pos2 = data.find('\n\n')
        if pos2 >= 0:
            pos2 += 2
        if pos1 >= 0:
            if pos2 >= 0:
                return min(pos1, pos2)
            else:
                return pos1
        else:
            return pos2
    def get_data_splitter(self, data):
        if data.split('\r\n\r\n')[0].split(' ')[0] in ('HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1'):
            return 1
        else:
            return 0
    def get_response_header(self, data):
        if not self.https:
            index = self.find_double_newline(data)
            if index >= 0:
                data = str(data[:index].split('\r\n\r\n')[0])
                if self.get_data_splitter(data):
                    self.send_connection_logger('+++Receive Response+++\r\n%s\r\n' % data)
                    self.send_connection_logger('\r\n')
        elif self.get_data_splitter(data):
            self.send_connection_logger('+++Receive Response+++\r\n%s\r\n' % data)
            self.send_connection_logger('\r\n')
    def get_response_data(self, soc):
        iw = [self.connection, soc]
        ow = []
        count = 0
        timeout = 0
        while 1:
            timeout += 1
            ins, _, exs = select.select(iw, ow, iw, 3)
            if exs:
                break
            if ins:
                for resp in ins:
                    try:
                        data = resp.recv(sets.SBUFF)
                        if data:
                            if resp is soc:
                                if sets.IQUERY:
                                    if self.get_data_splitter(data):
                                        count += 1
                                    if not self.https:
                                        if count % 2 == 0:
                                            count = 0
                                            self.get_response_header(data)
                                            self.send_response_data(data)
                                    else:
                                        for idata in data.split('\r\n\r\n'):
                                            if count == 1 and not idata.startswith('HTTP/'):
                                                self.send_response_data(idata)
                                else:
                                    self.get_response_header(data)
                                    self.send_response_data(data)
                            else:
                                while data:
                                    byte = soc.send(data)
                                    data = data[byte:]
                            timeout = 0
                        else:
                            break
                    except:
                        break
            if timeout == sets.TIMEOUT:
                break
    def send_response_data(self, data):
        self.wfile.write(data)
    def send_connection_close(self, soc):
        soc.close()
        self.connection.close()
    def send_connection_error(self, msg, page = True):
        try:
            code, message = msg
        except:
            self.send_connection_error((501, 'unknown error'))
        message = str(message).capitalize()
        self.send_connection_logger('+++Connection Error+++\r\n')
        self.send_connection_logger('%s: %s\r\n\r\n' % (str(code), message))
        if page:
            self.send_error(502, '%s.' % message)
    def send_connection_logger(self, data):
        if logs:
            sys.stderr.write(data)
    def do_METHOD(self):
        # check http method and post data
        method = self.command
        if method == "GET" or method == "HEAD":
            # no post data
            post_data_len = 0
        elif method == "POST":
            # get length of post data
            post_data_len = 0
            for header in self.headers:
                if header.lower() == "content-length":
                    post_data_len = int(self.headers[header])
                    break
            # exceed limit?
            if post_data_len > self.PostDataLimit:
                self.send_error(413, "Local proxy error, Sorry, Google's limit, file size up to 1MB.")
                self.connection.close()
                return
        else:
            # unsupported method
            self.send_error(501, "Local proxy error, Method not allowed.")
            self.connection.close()
            return
        # get post data
        post_data = ""
        if post_data_len > 0:
            post_data = self.rfile.read(post_data_len)
            if len(post_data) != post_data_len:
                # bad request
                self.send_error(400, "Local proxy error, Post data length error.")
                self.connection.close()
                return
        # create new path
        #path = urlparse.urlunparse((scm, netloc, path, params, query, ""))
        path=self.path
        if(path.find("/")==0):
          path=path[1:]
        dhs = []
        for header in self.headers:
            hl = header.lower()
            if hl == "if-range":
                dhs.append(header)
            elif hl == "range":
                dhs.append(header)
        for dh in dhs:
            del self.headers[dh]
        #del self.headers["Host"]
        # create request for GAppProxy
        params = urllib.urlencode({"method": method,
                                   "encoded_path": base64.b64encode(path),
                                   "headers": base64.b64encode(str(self.headers)),
                                   "postdata": base64.b64encode(post_data),
                                   "version": "1.0.5"})
        # accept-encoding: identity, *;q=0
        # connection: close
        #print params
        request = urllib2.Request("http://hakanzn.appspot.com/fetch.py")
        request.add_header("Accept-Encoding", "identity, *;q=0")
        request.add_header("Connection", "close")
        #print request
        #request.add_header("Host",bedava_site)
        # create new opener
        try:
            resp = urllib2.urlopen(request, params)
        except urllib2.HTTPError as e:
            if e.code == 404:
                self.send_error(404, "Local proxy error, Fetchserver not found at the URL you specified, please check it.")
            elif e.code == 502:
                self.send_error(502, "Local proxy error, Transmission error, or the fetchserver is too busy.")
            else:
                self.send_error(e.code)
            self.connection.close()
            return
        except urllib2.URLError, e:
            if local_proxy == "":
                shallWeNeedGoogleProxy()
            self.connection.close()
            return
        # parse resp
        # for status line
        line = resp.readline()
        print (line)
        words = line.split()
        status = int(words[1])
        reason = " ".join(words[2:])
        print (status,reason)
        # for large response
        if status == 592 and method == "GET":
            self.processLargeResponse(path)
            self.connection.close()
            return
        # normal response
        try:
            self.send_response(status, reason)
        except socket.error, (err, _):
            # Connection/Webpage closed before proxy return
            if err == errno.EPIPE or err == 10053: # *nix, Windows
                return
            else:
                raise
        # for headers
        text_content = True
        while True:
            line = resp.readline().strip()
            # end header?
            if line == "":
                break
            # header
            (name, _, value) = line.partition(":")
            name = name.strip()
            value = value.strip()
            # ignore Accept-Ranges
            if name.lower() == "accept-ranges":
                continue
            self.send_header(name, value)
            # check Content-Type
            if name.lower() == "content-type":
                if value.lower().find("text") == -1:
                    # not text
                    text_content = False
        self.send_header("Accept-Ranges", "none")
        self.end_headers()
        # for page
        if text_content:
            data = resp.read()
            if len(data) > 0:
                self.wfile.write(zlib.decompress(data))
        else:
            self.wfile.write(resp.read())
        self.connection.close()
    def del_garbage(self):
        del self.https
        del self.path
        del self.headers
        del self.uahdr
        del self.host
        del self.port
        del self.advhost
        del self.newline
        del self.requestline
        del self.injectline
        del self.phost
        del self.pport
        del self.puser
        del self.ppass
class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    def handle_error(self, request, client_address):
        pass
class HTTPProxyService():
    def __init__(self):
        self.httpd = ThreadingHTTPServer((sets.LHOST, sets.LPORT), ProxyHandler)
        self.httpd.allow_reuse_address = True
    def serve_forever(self):
        self.httpd.serve_forever()
class Server:
    def __init__(self, get):
        self.get = get		
    def __init__(self):
        self.long = 79
        self.sets = Sets()
        self.name = Info('name').get_info()
        self.ver = Info('ver').get_info()
        self.form = Info('about').get_info()
        self.auth = Info('by').get_info()
        self.mail = Info('mail').get_info()
        #self.conf = conf
        self.noyes = [ru('No'), ru('Yes')]
        self.version = [ru('Default'), ru('HTTP/1.0'), ru('HTTP/1.1')]
        self.method = [ru('HEAD'),
         ru('GET'),
         ru('POST'),
         ru('DELETE'),
         ru('CONNECT'),
         ru('OPTIONS'),
         ru('TRACE'),
         ru('PUT')]
        self.line = [ru('\\r\\n'), ru('\\n')]
        self.split = [ru('Default'),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE)),
         ru('%s' % (self.line[self.sets.ILINE] * self.sets.ILINE))]
    def subs(self, data = '', cut = False):
        if data:
            data = data
        else:
            data = 'None'
        if cut:
            if len(data) > 5:
                data = '%s...' % data[:5]
        return data
    def about(self, title = ''):
        self.info = []
        self.info.append('=[ %s ]%s\n' % (title, '=' * (self.long - len(title) - 5)))
        self.info.append('Name : %s\n' % self.name)
        self.info.append('Version : %s\n' % self.ver)
        self.info.append('Author : %s\n' % self.auth)
        self.info.append('Mail : %s\n' % self.mail)
        self.info.append('\n\n')
        return ru(''.join(self.info))
    def warning(self, title = ''):
        self.info = []
        self.info.append('=[ %s ]%s\n' % (title, '=' * (self.long - len(title) - 5)))
        self.info.append('Sale : This program not for sale !!!\n')
        self.info.append("Mirror : Don't mirror this file/program outside gembox.us !!!\n")
        self.info.append('\n\n')
        return ru(''.join(self.info))
    def donate(self, title = ''):
        self.info = []
        self.info.append('=[ %s ]%s\n' % (title, '=' * (self.long - len(title) - 5)))
        self.info.append('Paypal : inunxelex@yahoo.com\n')
        self.info.append('Payza : inunxlabs@gmail.com\n')
        self.info.append('\n\n')
        return ru(''.join(self.info))

    def log(self, title = ''):
        self.info = []
        self.info.append('=[ %s ]%s\n' % (title, '=' * (self.long - len(title) - 5)))
        self.info.append('\n\n')
        return ru(''.join(self.info))
    def show(self):
        sys.stderr.write(self.config('Configuration'))
        sys.stderr.write(self.log('Ready'))
    def run(self):
        LogWindow(True)
        HTTPProxyService().serve_forever()
    def pinger(self):
        while 1:
            time.sleep(random.randint(30, 300))
            Pinger().check()
if __name__ == '__main__':
    services = [threading.Thread(target=Server().run, args=()), threading.Thread(target=Server().pinger, args=())]
    for serving in services:
        serving.start()

		
