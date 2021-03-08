import wikipedia


def query_wiki(word):
    page = wikipedia.page(word)
    content = page.content
    return content
