import requests
from bs4 import BeautifulSoup

def getTopOneHundred():
    
    userInput = input('Would you like the top 100 of all time or by year?: ')
    if userInput.lower() == 'year' or userInput.lower() == 'by year':
        yearInput = input('What year?: ')
        url = 'https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?year_selected='+yearInput+'&distribution=&sort=desc&view=detailed'
        user_agent = {'User-agent': 'Brave/1.43.93'} #my preferred browser
        urlReq = requests.get(url,headers = user_agent, allow_redirects=False)
        soup = BeautifulSoup(urlReq.content, 'lxml')
    else:
        url = 'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered'
        user_agent = {'User-agent': 'Brave/1.43.93'}
        urlReq = requests.get(url,headers = user_agent, allow_redirects=False)
        soup = BeautifulSoup(urlReq.content, 'lxml')

    results = soup.find('div', class_='title_bump')
    game_elements = results.find_all('tr')

    for game in game_elements:
        if game.find('h3') is not None:
            title = game.find('h3')
            print('\n'+title.text)
        if game.find('span', class_='data') is not None:
            platform = game.find('span', class_='data')
            print(platform.text.strip())
        if game.find('div', class_='metascore_w large game positive') is not None:
            score = game.find('div', class_='metascore_w large game positive')
            print('metascore: '+score.text)

getTopOneHundred()
