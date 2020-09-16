import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import os
import re
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('fivethirtyeight')
'''
only games completed on or before 9/15/2020
'''

def clean_games(games):
    games_df = pd.DataFrame(columns=['visitor_score', 'home_score'])
    games_lst = []
    visitor = []
    home = []
    for i, game in enumerate(games):
        x = re.findall("\(\d+\)", str(game))
        x = ','.join(x)
        x = x.translate({ord(i): None for i in '()'})
        x = x.split(',')
        games_lst.append(x)
    
    for score in games_lst:
        if len(score)>1:
            visitor.append(int(score[0]))
            home.append(int(score[1]))

    games_df.visitor_score = visitor
    games_df.home_score = home

    return games_df

    



if __name__ == '__main__':
    
    client = MongoClient('localhost', 27017)
    db = client['baseball_reference']
    table = db['gl_2020']

    soup = BeautifulSoup(requests.get('https://www.baseball-reference.com/leagues/MLB/2020-schedule.shtml').content, 'html.parser')
    '''
    class = "game"

    '''
    games = [i for i in soup.find_all(class_="game")]

    cleaned = clean_games(games)
    cleaned['MOV'] = np.abs(cleaned.visitor_score - cleaned.home_score)
    plt.hist(cleaned.MOV, bins=20)

    # group = cleaned.groupby("MOV").count()
    # group['percent'] = group.home_score / 24297
    
    plt.title('2020 Margin of Victory')
    plt.savefig('2020.png')
    plt.tight_layout()
    plt.show()

    test = np.random.poisson(lam=1.0, size = 900)
    plt.hist(test, bins=5)
    plt.close()

    print(f'2020 Mean:{np.mean(cleaned.MOV)}')
    print(f'2020 Std: {np.std(cleaned.MOV)}')
    print(f'2020 Median: {np.median(cleaned.MOV)}')
    # print(f'2020 Mode: {stats.mode(cleaned.MOV)}')

    