#from user_input import user_input
from crawl import Crawl
from crawley import Crawley

crawley = Crawley()
crawley.welcome() 
url, levels, user_defined_regex = crawley.user_input()

crawl = Crawl(url, levels, user_defined_regex)
crawl.perform_crawl()
crawl.test_variables()
crawl.save_to_pdf()

while True:
    if crawley.crawl_another() == True:
        url, levels, user_defined_regex = crawley.user_input()
        crawl = Crawl(url, levels, user_defined_regex)
        crawl.perform_crawl()
        crawl.test_variables()
        crawl.save_to_pdf()
    else:
        crawley.goodbye()
        break