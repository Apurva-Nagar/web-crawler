from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *


class Spider:

	#Class variable, shared among all the spiders (instances).
	dir_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue_set = set()
	crawled_set = set()


	def __init__(self, dir_name, base_url, domain_name):
		Spider.dir_name = dir_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.dir_name + '\queue.txt'
		Spider.crawled_file = Spider.dir_name + '\crawled.txt'
		self.boot()
		self.crawl_page('Alpha Spidy', Spider.base_url)


	@staticmethod
	def boot():
		create_website_dir(Spider.dir_name)
		create_data_files(Spider.dir_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)


	@staticmethod
	def crawl_page(spider_name, page_url):
		if page_url not in Spider.crawled:
			print (spider_name + ' now crawling ' + page_url)
			print ('In Queue ' + str(len(Spider.queue)))
			print ('Crawled ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()


	@staticmethod
	def gather_links(page_url):
		html_str = ''
		try:
			response = urlopen(page_url)
			if 'text/html' in response.getheader('Content-Type'):
					html_bytes = response.read()
					html_str = html_bytes.decode("utf-8") 		#converting byte code returned by HTMLParser to UTF-8 encoded string
			finder = LinkFinder(Spider.base_url, page_url)  #LinkFinder object
			finder.feed(html_str)
		except Exception as e:
			print ("Can't crawl the page    " + str(e))
			return set()
		return finder.page_links()


	@staticmethod
	def add_links_to_queue(links):
		for link in links:
			if link in Spider.queue:
				continue
			if link in Spider.crawled:
				continue
			if Spider.domain_name != get_main_domain_name(link):
				continue
			Spider.queue.add(link)


	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)
