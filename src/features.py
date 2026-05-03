import re
import tldextract
from bs4 import BeautifulSoup
from datetime import datetime

# URL FEATURES (Ben) 
def has_ip_url(url: str) -> int:
    """Returns 1 if URL contains an IP address instead of domain name"""
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    return int(bool(re.search(pattern, str(url))))

def has_fresh_domain(url: str, threshold_days: int = 60) -> int:
    """Returns 1 if domain was registered less than threshold_days ago.
    Uses python-whois to check WHOIS registration date.
    Returns 0 if lookup fails or times out."""
    try:
        import whois
        import socket
        socket.setdefaulttimeout(5)
        domain = tldextract.extract(str(url)).registered_domain
        if not domain:
            return 0
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date is None:
            return 0
        age_days = (datetime.now() - creation_date).days
        return int(age_days < threshold_days)
    except:
        return 0

def has_nonmatching_url(html_body: str) -> int:
    """Returns 1 if any anchor tag's visible text and href destination differ.
    Specifically checks cases where both text and href contain http links."""
    try:
        soup = BeautifulSoup(str(html_body), 'html.parser')
        for tag in soup.find_all('a', href=True):
            link_text = tag.get_text(strip=True)
            href = tag['href']
            if link_text and href and link_text != href:
                if 'http' in link_text and 'http' in href:
                    return 1
        return 0
    except:
        return 0

def num_links(html_body: str) -> int:
    """Returns total number of anchor tags found in the email body."""
    try:
        soup = BeautifulSoup(str(html_body), 'html.parser')
        return len(soup.find_all('a'))
    except:
        return 0

def num_domains(html_body: str) -> int:
    """Returns number of unique domains found across all URLs in the email body."""
    try:
        soup = BeautifulSoup(str(html_body), 'html.parser')
        domains = set()
        for tag in soup.find_all('a', href=True):
            extracted = tldextract.extract(tag['href'])
            if extracted.registered_domain:
                domains.add(extracted.registered_domain)
        return len(domains)
    except:
        return 0

def max_dots(url: str) -> int:
    """Returns the number of dots in the URL.
    High dot count indicates suspicious subdomain stacking."""
    try:
        return str(url).count('.')
    except:
        return 0

def has_url_shortener(url: str) -> int:
    """Returns 1 if URL uses a known URL shortening service."""
    try:
        shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co',
                      'ow.ly', 'short.link', 'buff.ly', 'is.gd']
        return int(any(s in str(url) for s in shorteners))
    except:
        return 0

# CONTENT FEATURES (Theryn) 
def has_javascript(email_body: str) -> int:
    """Returns 1 if email body contains JavaScript"""
    soup = BeautifulSoup(str(email_body), 'html.parser')
    return int(bool(soup.find('script')))

# HEADER FEATURES (Peter) 
def sender_domain_mismatch(from_domain: str, email_body: str) -> int:
    """Returns 1 if sender domain doesn't match domain in email body. Checks the entire body for the substring of the sender domain, if it is not found then returns 1, if it is found then returns 0. If either value is empty or None then returns -1."""
    
    # If empty strings or None values are passed, return -1
    if from_domain is None or email_body is None or str(from_domain).strip() == '' or str(email_body).strip() == '':
        return -1
    # Extract domain from email body
    body_domain = tldextract.extract(str(email_body)).domain
    return int(str(from_domain).strip().lower() not in 
               str(body_domain).strip().lower())

def has_spf_fail(email_body: str) -> int:
    """Returns 1 if email header has SPF authentication failure. Looks at the body of the email and checks for a substring of "spf=fail" (returns 1) or "spf=pass" (returns 0). If neither is found then returns 1 since the status can not be confirmed. If the parameter is empty or None then returns -1."""
    # If empty strings or None values are passed, return -1
    if email_body is None or str(email_body).strip() == '':
        return -1
    
    # From what I can tell the way to understand if an email from the data set has an SPF failure I need to look for the substring "spf=fail" in the email body.
    if 'spf=fail' in str(email_body).strip().lower():
        return 1
    
    if 'spf=pass' in str(email_body).strip().lower():
        return 0
    return 1  # If it does not say fail or pass then we will assume it is a fail

def timestamp_anomaly(date: str, received: str) -> int:
    """Returns 1 if difference exceeds 24 hours. Compares the date header with the recieived header"""
    
    # If empty strings or None values are passed, return -1
    if date is None or received is None or str(date).strip() == '' or str(received).strip() == '':
        return -1
    # Example format to reference: "Tue, 05 Aug 2008 16:31:02 -0700"
    # Parse the day, month, year, and time from the date and timestamp
    date_parts = str(date).strip().split()
    received_parts = str(received).strip().split()
    # If the date is the same then 24 hours have not been exceeded, return 0
    if str(date_parts[1]).strip() == str(received_parts[1]).strip():
        if str(date_parts[2]).strip() == str(received_parts[2]).strip():
            if str(date_parts[3]).strip() == str(received_parts[3]).strip():
                return 0
            else:
                return 1 # If the year does not match then 24 hours have been exceeded, return 1
        else:
            return 1 # If the month does not match then 24 hours have been exceeded, return 1
    else:
        # Check if the days are more than 1 apart, if so then 24 hours have been exceeded, return 1
        if abs(int(date_parts[1].strip()) - int(received_parts[1].strip())) > 1:
            return 1
    # Check if the timestamp is within 24 hours of the date's timestamp
    format = "%H:%M:%S"
    time_difference = datetime.strptime(received_parts[4], format) - datetime.strptime(date_parts[4], format)
    if abs(time_difference.total_seconds()) > 24 * 3600:
        return 1
    else:
        return 0
