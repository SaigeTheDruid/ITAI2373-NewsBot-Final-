def classify_intent(query):
    query = query.lower()
    if "positive" in query and "news" in query:
        return "get_positive_news"
    elif "summary" in query:
        return "get_summary"
    elif "entities" in query:
        return "get_entities"
    else:
        return "general_query"

