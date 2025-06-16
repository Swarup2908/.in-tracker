# scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ARCHIVE_URL = "https://www.registry.in/domain-archives"

def get_pdf_links():
    resp = requests.get(ARCHIVE_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    pdf_links = []

    for a in soup.select('a[href$=".pdf"]'):
        href = urljoin(ARCHIVE_URL, a['href'])
        if "Statistics" in href or "domain" in href.lower():
            pdf_links.append(href)

    return sorted(set(pdf_links), reverse=True)
