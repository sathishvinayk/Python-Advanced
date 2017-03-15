import threading, _thread, urllib2
class Fetchurls(threading.Thread):
    def __init__(self,urls,output,lock):
        threading.Thread.__init__(self)
        self.urls=urls
        self.output=output
        self.lock=lock
    def run(self):
        while self.urls:
            url=self.urls.pop()
            req=urllib2.Request(url)
            try:
                d=urllib2.urlopen(req)
            except urllib2.URLError, e:
                print 'URL %s failed: %s'%(url,e.reason)
            self.lock.acquire()
            print 'Lock acquired by %s'%self.name
            print('Write done by %s'%self.name)
            print('lock released by %s'%self.name)
            self.lock.release()
            print('URL %s fetched by %s'%(url,self.name))
            print('DOne')
            self.lock.acquire()
            print 'Lock acquired by %s'%self.name
            print('Write done by %s'%self.name)
            print('lock released by %s'%self.name)
            self.lock.release()
            print('URL %s fetched by %s'%(url,self.name))

def main():
    urls1=['http://www.google.com','http://www.facebook.com']
    urls2=['http://www.yahoo.com','http://www.youtube.com']
    lock=threading.RLock()
    f=open('output.txt', 'w+')
    t1=Fetchurls(urls1,f,lock)
    t2=Fetchurls(urls2,f,lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__=='__main__':
    main()
