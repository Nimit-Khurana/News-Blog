from .paper import topStories

hindustan_feed_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
hindu_international = "https://www.thehindu.com/news/international/feeder/default.rss"
hindu_national = "https://www.thehindu.com/news/national/feeder/default.rss"
toi_top = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
toi_national = "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
toi_international = "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"

def extract(feed):
    content = topStories(feed)
    return content
    # pubDate guid link src 
    #for item in content:
    #    print ( "<-- " + item['title'] + " -->" )
    #    print ( item['description'] )
    #    print ("\n")

def newspaper_cli():
    print ("[h]indu \
            h[i]ndustan \
            [t]imes of India")
    user = input("Which newspaper? ")
    if user == "h":
        extract( hindustan_feed_url )
    elif user == 't':
        user_two = input("[n]ational | [i]nternational :")
        if user_two == "n":
            extract( toi_national )
        else:
            extract( toi_international )
    else:
        user_two = input("[n]ational | [i]nternational :")
        if user_two == "n":
            extract( hindu_national )
        else:
            extract( hindu_international )

if __name__ == "__main__":
    newspaper_cli()