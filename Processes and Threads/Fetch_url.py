import threading, _thread, urllib2

#Define a class which can fetch urls and writes its date on a txt file.
class Find_urls(threading.Thread):
    def __init__(self,urls, output):
        threading.Thread.__init__(self)
        self.urls=urls
        self.output=output
    def run(self):
        #Check url's one by one
        while self.urls:
            url=self.urls.pop()
            req=urllib2.Request(url)
            try:
                d=urllib2.urlopen(req)
            except urllib2.URLError as e:
                print ('Link %s has failed due to %s' %(url,e.reason))
            self.output.write(d.read())
            print('File written by %s' %self.name)
            print('url %s fetched by %s'%(url, self.name))

def main():
    urls1=['http://www.google.com','http://www.facebook.com']
    urls2=['http://www.yahoo.com','http://youtube.com']
    f=open('output.txt', 'w+')
    t1=Find_urls(urls1,f)
    t2=Find_urls(urls2,f)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__=='__main__':
    main()
