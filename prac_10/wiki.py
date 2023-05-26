import wikipedia

search=input("Search:")
while search != "":
    wiki_page=wikipedia.page(search)
    print("Title" + wiki_page.title)
    print(wikipedia.summary(search))
    print("URL" + wiki_page.url)
    search = input("Search:")