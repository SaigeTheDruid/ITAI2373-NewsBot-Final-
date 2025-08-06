def generate_response(intent, data):
    if intent == "get_positive_news":
        return f"Here are some positive news articles: {data}"
    elif intent == "get_summary":
        return f"Summary of the news: {data}"
    elif intent == "get_entities":
        return f"Entities found: {data}"
    else:
        return "Sorry, I didn't understand your request. Could you please rephrase?"

