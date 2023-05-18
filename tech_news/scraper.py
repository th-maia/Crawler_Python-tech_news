import requests
import time
from requests.exceptions import Timeout, HTTPError
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        return response.text
    except(HTTPError, Timeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    urls = selector.css("h2 a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(html_content)
        next_page_url = selector.css("a.next::attr(href)").get()
    except TypeError:
        None
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    scraped_new = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css("span.author a.url::text").get(),
        "reading_time": int(
            selector.css(".meta-reading-time::text").get().split(" ")[0]
        ),
        "summary": ("".join(selector.css(
            ".entry-content > p:nth-of-type(1) *::text",
        ).getall())).strip(),
        "category": selector.css("span.label::text").get(),
    }
    return scraped_new


# Requisito 5
def get_tech_news(amount):
    page_url = "https://blog.betrybe.com/"
    notice_list = []

    while len(notice_list) < amount:
        html_content = fetch(page_url)
        notice_urls = scrape_updates(html_content)

        for notice_url in notice_urls:
            new_page = fetch(notice_url)
            scraped_new = scrape_news(new_page)
            notice_list.append(scraped_new)
            if len(notice_list) >= amount:
                break
        page_url = scrape_next_page_link(html_content)

    create_news(notice_list)
    return notice_list
