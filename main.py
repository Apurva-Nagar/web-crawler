import threading
from queue import Queue
from spider import Spider 
from domain import *
from general import *


DIR_NAME = 'xkcd'
HOMEPAGE = 'http://xkcd.com/'
DOMAIN_NAME = get_main_domain_name(HOMEPAGE)
QUEUE_FILE = DIR_NAME + '\queue.txt'
CRAWLED_FILE = DIR_NAME + '\crawled.txt'
NUMBER_OF_SPIDERS = 20

queue = Queue()
Spider(DIR_NAME, HOMEPAGE, DOMAIN_NAME)


def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)


def create_spiders():		
	for _ in range(NUMBER_OF_SPIDERS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()


def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()


def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' links in queue.')
		create_jobs()


create_spiders()
crawl()
