import webbrowser


query = input("Enter a word to search: ")
# url = f"https://www.google.com/search?q={query}"
url = f"https://www.perplexity.ai/search/new?q={query}"

webbrowser.open(url)

# we can use Google API
