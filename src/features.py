import re
import tldextract
from bs4 import BeautifulSoup

# URL FEATURES (Ben) 

def has_ip_url(url: str) -> int:
    """Returns 1 if URL contains an IP address instead of domain name"""
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    return int(bool(re.search(pattern, str(url))))

# CONTENT FEATURES (Theryn) 

def has_javascript(email_body: str) -> int:
    """Returns 1 if email body contains JavaScript"""
    soup = BeautifulSoup(str(email_body), 'html.parser')
    return int(bool(soup.find('script')))

# HEADER FEATURES (Peter) 

def sender_domain_mismatch(from_domain: str, body_domain: str) -> int:
    """Returns 1 if sender domain doesn't match domain in email body"""
    return int(str(from_domain).strip().lower() != 
               str(body_domain).strip().lower())
