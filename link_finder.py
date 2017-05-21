from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser, object):

	#Inheriting HTMLParser
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()


	#finds starting HTML tags from .feed() data
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value)  #handling relative urls
					self.links.add(url)


	#Stores scraped links
	def page_links(self):
		return self.links


	#Abstract method for HTMLParser, handels errors
	def error(self, message):
		pass
		

		