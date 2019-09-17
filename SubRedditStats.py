import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Enter Subreddit Name
subredditName = input("Enter SubReddit Name: ")
# bypass HTTPError: Bad Gateway
while True:
    try:
        # Get the HTML of the page using urllib
        getHTML = urllib.request.urlopen('https://www.reddit.com/r/{}/'.format(subredditName)).read()
        # Parse the HTML 
        soupVar = BeautifulSoup(getHTML,'html.parser')
        # find all tags with specific attribute  
        stats = soupVar.find_all('p', attrs={'class':'_3XFx6CfPlg-4Usgxm0gK8R'})
        member = stats[0].text.strip()  
        online = stats[1].text.strip()    
        print("\n" + member,"Members\n" + online,"Online")
        break
    except:
        continue