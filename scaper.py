import requests
from bs4 import BeautifulSoup
import pprint  #for styling

def get_all_pages(num):
   all_links = []
   all_subtexts = []
   for i in range(1,num + 1):
     url = f'https://news.ycombinator.com/news?p={i}'
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'html.parser')
     links = soup.select('.titleline > a') 
     subtext = soup.select('.subtext')
     all_links.extend(links)
     all_subtexts.extend(subtext)
   return all_links,all_subtexts

def votes_sorted(lists):
   return sorted(lists, key = lambda x:x['votes']) # this sorts the dictionary regarding the number of votes


def create_custom(links,subtext):
    hn = []
    for indx, item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)
        vote = subtext[indx].select('.score')
        if len(vote):
          points = int(vote[0].get_text().replace(' points','')) 
          if points >= 100:
            hn.append({'title:':title,'link':href,'votes':points})
    return votes_sorted(hn)

links,subtexts = get_all_pages(4)
pprint.pprint(create_custom(links,subtexts))
#print(subtext)