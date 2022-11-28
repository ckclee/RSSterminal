import feedparser

url = input("Please input a valid RSS feed URL: \n")
rss = feedparser.parse(url)

print(rss.feed.title)
print(rss.feed.description)
print("\n")
print("Latest entries: \n")

for i in range(5):
    try:
        entry = rss.entries[i]
        print('TITLE: ' + entry.get('title', 'No title'))
        print('DESCRIPTION: ' + entry.get('summary', 'No description'))
        print('LINK: ' + entry.get('link', 'No link'))
        print()
    except IndexError:
        print("No more entries!")
        break       
