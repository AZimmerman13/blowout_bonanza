import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest


if __name__ == '__main__':
    # Reading in data
    sample_means = pd.read_csv('pre2020_sample_means.csv', usecols=[1])
    sample_means = np.array(sample_means.iloc[:,0])
    df20 = pd.read_csv('2020_games.csv')
    dfpre = pd.read_csv('pre2020.csv')
    df20['mov'] = df20.visitor_score - df20.home_score
    avg20 = np.mean(df20.MOV)
    Ztest = ztest(df20.mov, dfpre.mov, value=0, alternative='larger')

    # Plotting
    plotting = False
    if plotting:
        test = [0,1,2,1,1,2,1,5,4,2,1,3,2,1,3,4,4,4,4,1,9,2,3,2]
        fig, ax = plt.subplots()
        ax.hist(sample_means)
        ax.axvline(avg20, color='red', label='2020 Average MOV')
        ax.set_title('Title')
        plt.tight_layout()
        plt.legend()
        plt.savefig('images/sample_means.png')
        plt.show()

    plt.hist(df20.mov, bins=10)
    plt.savefig('images/20normal.png')
    plt.title('2020 MOV (Home wins are negative)')
    plt.tight_layout()
    plt.show()

    plt.hist(dfpre.mov, bins=20)
    plt.savefig('images/pre20normal.png')
    plt.title('Pre-2020 MOV (Home wins are negative)')
    plt.tight_layout()
    plt.show()

    