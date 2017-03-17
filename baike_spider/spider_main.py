# -*- coding: UTF-8 -*-
'''
Created on 2017年3月11日

@author: Dell
'''
#爬虫总调度程序
from baike_spider import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
    #初始化
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    
    #传入爬虫抓取的入口地址
    def craw(self, root_url):
        count=1
        #将该URL添加到带爬取的URL集合
        self.urls.add_new_url(root_url)
        #有需要爬取的URL
        while self.urls.has_new_url():
            try:
                #获取一个待爬取的URL，并打印相关信息
                new_url=self.urls.get_new_url()
                print 'crow %d : %s'%(count,new_url)
                #下载器下载该URL的内容
                html_cont=self.downloader.download(new_url)
                #解析器解析当前爬取URL，将信息存放到URL集合中，并将数据保存下来
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count==20:
                    break
                count=count+1
            except:
                print 'craw failed'
        self.outputer.output_html()
    
    



if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.html"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    