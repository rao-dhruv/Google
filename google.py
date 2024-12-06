from googlesearch import search
query = input("Enter the query: ")
for link in search(query , tld="com", stop=10):
    print(link)
