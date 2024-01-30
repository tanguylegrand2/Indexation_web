import click
from crawler import Crawler

@click.command()
@click.option('--seed_url', default="https://ensai.fr/", help='Seed URL for crawling')
@click.option('--max_urls_per_page', default=10, help='Maximum URLs to explore per page')
@click.option('--max_total_urls', default=50, help='Maximum total URLs to explore')
@click.option('--crawl_delay', default=3, help='Delay between requests for politeness')
def main(seed_url, max_urls_per_page, max_total_urls, crawl_delay):
    crawler = Crawler(seed_url, max_urls_per_page, max_total_urls, crawl_delay)
    crawler.crawl()
    crawler.save_to_file("crawled_webpages.txt")

if __name__ == "__main__":
    main()