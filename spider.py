#import urllib.request
#from urllib.request import urlopen
from urllib.request import FancyURLopener
from link_finder import LinkFinder
from general import *

class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


class Spider:
    # calss variables (share from all instances)
    project_name = ''
    base_url     = ''
    domain_name  = ''
    queue_file   = ''
    crawled_file = ''
    queue        = set()
    crawled      = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url     = base_url
        Spider.domain_name  = domain_name
        Spider.queue_file   = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)
        
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)

        Spider.queue   = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | crawled  ' + str(len(Spider.crawled)))
            Spider.dump_class_variables()
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

        
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            #response = urlopen(page_url)
            #response = urlopen(page_url)
            #html     = response.read()
            #print(html)
            myopener = MyOpener()
            rsp = myopener.open(page_url)

            #print(rsp.read())
            #print(rsp.headers)
            #print(rsp.info())
            #print(rsp.geturl())

            html_types  = rsp.read()
            html_string = html_types.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print('Error: can not crawl this page')
            print(e)
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        #print(links)
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        print('starting update_files......')
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

    @staticmethod
    def dump_class_variables():
        print(Spider.project_name)
        print(Spider.base_url)
        print(Spider.domain_name)
        print(Spider.queue_file)
        print(Spider.crawled_file)
        print(Spider.queue)
        print(Spider.crawled)
