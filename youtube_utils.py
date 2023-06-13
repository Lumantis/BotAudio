from youtube_search import YoutubeSearch

def search_youtube(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    if results:
        return f"https://www.youtube.com/watch?v={results[0]['id']}"
    else:
        return None
