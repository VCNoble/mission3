#from collections import Counter
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from decouple import config
 
subscription_key = config('subscription_key', default='')
 
search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = 'turners cars'
 
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
 
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
 
pages = search_results['webPages']
results = pages['value']
 
for result in results[:10]:
    response = requests.get(result['url'])
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find('body').get_text().strip()
    cleaned_text = ' '.join(text.split('\n'))
    cleaned_text = ' '.join(text.split())
    #counter = Counter([x for x in cleaned_text.split() if len(x) > 5])
    #print(counter.most_common(10))
    print(cleaned_text)
    break
