import re

class Regex_patterns:
    def url(self):
        return r"(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+([a-z0-9/.:=?_&#]+)?"
    
    def domain(self):
        return r"(http(s)?://)?(www.)?[a-z0-9-]+.[a-z]+"

    def pure_domain(self):
        return r"(?<=\/\/)(www.)?[a-z0-9-]+.[a-z]+"

    def http(self):
        return r"http(s)?://"

    def email(self):
        return r"[a-zA-Z0-9\.\-\_]+@[0-9a-zA-Z\.\-]+.[a-zA-Z]+"
    
    def phone_number(self):
        return r"[+(\d]{1}[\d+() ]{4,12}[\d]{1}"

    def html_comment(self):
        return r"<!--[ -~]*-->"

    def js_comment(self):
        return r"(?<!:)\/\/[ -~]*"

    def word(self):
        return r"[^a-zA-Z ]+"
