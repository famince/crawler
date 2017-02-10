import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME      = 'xiami'
HOMEPAGE          = 'http://www.xiami.com/artist?spm=a1z1s.6843761.1110925385.4.URj4Nh'
DOMAIN_NAME       = get_domain_name(HOMEPAGE)
QUEUE_FILE        = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE      = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)




