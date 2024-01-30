import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import os
from urllib import robotparser

class Crawler:
    def __init__(self, seed_url, max_urls_per_page, max_total_urls, crawl_delay):
        self.seed_url = seed_url
        self.max_urls_per_page = max_urls_per_page
        self.max_total_urls = max_total_urls
        self.crawl_delay = crawl_delay
        self.visited_urls = set()
        self.queue = [seed_url]

    def crawl(self):
        while self.queue and len(self.visited_urls) < self.max_total_urls:
            current_url = self.queue.pop(0)
            
            if current_url not in self.visited_urls:
                print(f"Crawling: {current_url}")
                self.visited_urls.add(current_url)
                self.download_page(current_url)
                self.extract_links(current_url)

                time.sleep(self.crawl_delay) #Respect de la politeness de telchargement entre les pages
        time.sleep(self.crawl_delay) #Respect de la politeness de telechargmenent de la dernière page
        print(len(self.queue))

    def download_page(self, url):
        try:
            if url not in self.visited_urls:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    print(f"Title: {soup.title.string}")
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")

    def extract_links(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links[:self.max_urls_per_page]:
                    absolute_url = urljoin(url, link['href'])
                    if self.is_valid_url(absolute_url):
                        self.queue.append(absolute_url)
        except requests.RequestException as e:
            print(f"Error extracting links from {url}: {e}")

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.scheme in ('http', 'https') and parsed_url.netloc not in self.visited_urls and self.is_allowed_to_crawl(url)==True
    
    def is_allowed_to_crawl(self, url):
        try:
            # Construire l'URL du fichier robots.txt
            robots_url = f"{url}/robots.txt"

            # Initialiser un objet RobotParser
            rp = robotparser.RobotFileParser()
            rp.set_url(robots_url)
            rp.read()

            # Vérifier si l'URL est autorisée à être explorée
            return rp.can_fetch("*", url)

        except Exception as e:
            print(f"Erreur lors de la vérification du fichier robots.txt : {e}")
            return False
        
        
        def read_sitemap(self, url):
            try:
                # Vérifier si le site autorise le crawling du fichier sitemap.xml
                if self.is_allowed_to_crawl(url):
                    response = requests.get(url)
                    if response.status_code == 200:
                        root = ET.fromstring(response.text)
                        return [urljoin(url, loc.text) for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
            except Exception as e:
                print(f"Erreur lors de la lecture du sitemap : {e}")
            return []


    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for url in self.visited_urls:
                file.write(url + '\n')
