from urllib.parse import urlparse


#ex.- forbes.com
def get_main_domain_name(url):
	try:
		results = get_full_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''

#ex.- mail.gov.forbes.com
def get_full_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

