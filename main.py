#from user_input import user_input
from crawl import Crawl
from crawley import Crawley

crawley = Crawley()
crawley.welcome() 
url, levels, user_defined_regex = crawley.user_input()

crawl = Crawl(url, levels, user_defined_regex)
crawl.perform_crawl()