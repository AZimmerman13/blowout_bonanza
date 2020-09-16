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

    group = df.groupby("MOV").count()
    group['percent'] = group.home_score / 24297
'''
         visitor_score  home_score   percent
MOV
0                1           1  0.000041
1             7030        7030  0.289336
2             4465        4465  0.183768
3             3443        3443  0.141705
4             2836        2836  0.116722
5             2024        2024  0.083302
6             1487        1487  0.061201
7             1016        1016  0.041816
8              702         702  0.028892
9              458         458  0.018850
10             313         313  0.012882
11             201         201  0.008273
12             112         112  0.004610
13              89          89  0.003663
14              48          48  0.001976
15              28          28  0.001152
16              23          23  0.000947
17               8           8  0.000329
18               6           6  0.000247
19               2           2  0.000082
20               3           3  0.000123
21               2           2  0.000082
'''