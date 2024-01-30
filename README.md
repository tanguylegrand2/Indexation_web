
# Crawler Project

**Contributor:** Legrand Tanguy

## Features
Respect the politeness between the download of two URL  
Limits the number of URL to crawl  
Limits the number of links we takes per pages  
dont crawl URL not allowed  
Read sitemap.xml  
Be polite about the download speed of the last page  


## Project Structure

crawler/  
│  
├── main.py  
├── crawler.py  
├── README.md  



main.py: Entry point of the program using Click for command line options.  
crawler.py: Implementation of the crawler with required features.  
README.md: Project documentation.  



The crawler starts from the seed URL, downloads pages, extracts links, and follows the specified rules. The crawled URLs are saved to crawled_webpages.txt.



## Configuration

You can configure the crawler by modifying the parameters in main.py:  

seed_url :Seed URL for crawling  
max_urls_per_page: Maximum URLs to explore per page  
max_total_urls: Maximum total URLs to explore  
crawl_delay: Delay between requests for politeness  



## How to Run

1. Make sure you have Python installed.  
2. Install required packages using `pip install requests beautifulsoup4 click`.  
3. Execute the crawler using `python main.py`.  

### Usage with Click

- Run the crawler with default settings:  
  ```bash  
  python main.py  



  Customize settings using command line options:  

  python main.py --seed_url "https://example.com" --max_urls_per_page 10 --max_total_urls 100 --crawl_delay 5  
