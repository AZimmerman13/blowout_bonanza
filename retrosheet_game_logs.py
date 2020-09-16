import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('fivethirtyeight')
'''
The information used here was obtained free of
charge from and is copyrighted by Retrosheet.  Interested
parties may contact Retrosheet at "www.retrosheet.org".

https://www.retrosheet.org/gamelogs/glfields.txt
https://www.retrosheet.org/gamelogs/index.html
'''
if __name__ == '__main__':
    game_log_cols = None
    files = ['GL2010', 'GL2011', 'GL2012', 'GL2013', 'GL2014', 'GL2015', 'GL2016', 'GL2017', 'GL2018', 'GL2019']
    df = pd.DataFrame(columns=['visitor_score','home_score'])
    for f in files:
        hold = pd.read_csv(f'gl2010_19/{f}.TXT', usecols=[9,10], names=['visitor_score', 'home_score'])
        df = df.append(hold, ignore_index=True)


    df['MOV'] = np.abs(df.visitor_score - df.home_score)
    plt.hist(df.MOV, bins=20)
    
    plt.title('Pre-2020 Margin of Victory')
    plt.savefig('pre2020.png')
    plt.tight_layout()
    plt.show()
    
    print(f'Pre-2020 Mean:{np.mean(df.MOV)}')
    print(f'Pre-2020 Std: {np.std(df.MOV)}')
    print(f'Pre-2020 Median: {np.median(df.MOV)}')
    # print(f'Pre-2020 Mode: {stats.mode(df.MOV)}')