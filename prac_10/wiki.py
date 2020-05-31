import wikipedia


search = input("Search: ")
while search != "":
    try:
        page = wikipedia.page(search)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search = input("Search: ")
