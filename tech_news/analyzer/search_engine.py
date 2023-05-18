from tech_news.database import search_news
from datetime import datetime


def search_by_title(title: str):
    searched_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in searched_news]


def search_by_date(date):
    try:
        searched_news = search_news({
            "timestamp": datetime.strptime(date, "%Y-%m-%d").strftime(
                    "%d/%m/%Y"
                )})
        return [(new["title"], new["url"]) for new in searched_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    searched_news = search_news({"category": {
        "$regex": category, "$options": "i"
        }})
    return [(new["title"], new["url"]) for new in searched_news]
