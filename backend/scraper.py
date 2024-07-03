import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    profile_data = {
        'name': soup.find('li', {'class': 'inline t-24 t-black t-normal'}).text.strip() if soup.find('li', {'class': 'inline t-24 t-black t-normal'}) else '',
        'headline': soup.find('h2', {'class': 'mt1 t-18 t-black t-normal'}).text.strip() if soup.find('h2', {'class': 'mt1 t-18 t-black t-normal'}) else '',
        'about': soup.find('p', {'class': 'pv-about__summary-text mt4 t-14 ember-view'}).text.strip() if soup.find('p', {'class': 'pv-about__summary-text mt4 t-14 ember-view'}) else '',
        'experience': [item.text.strip() for item in soup.find_all('span', {'class': 'mr1 t-bold'})] if soup.find_all('span', {'class': 'mr1 t-bold'}) else [],
        'education': [item.text.strip() for item in soup.find_all('span', {'class': 'pv-entity__school-name t-16 t-black t-bold'})] if soup.find_all('span', {'class': 'pv-entity__school-name t-16 t-black t-bold'}) else []
    }

    return profile_data