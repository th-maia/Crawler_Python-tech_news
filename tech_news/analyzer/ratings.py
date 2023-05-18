from tech_news.database import db
# Requisito 10


def top_5_categories():
    count_by_category = {
        "$group": {
            "_id": "$category",
            "quantity": {"$sum": 1}
        }
    }
    sort = {"$sort": {"quantity": -1, "_id": 1}}
    limit = {"$limit": 5}
    query = [
        count_by_category,
        sort,
        limit
    ]
    return [i.get("_id") for i in db.news.aggregate(query)]
