import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from mfcc import mfcc_calc

AUDIO_DIR = 'C:\\Users\\gaura\\Desktop\\fma_small'
META_DIR = 'C:\\Users\\gaura\\Desktop\\fma_metadata\\tracks.csv'

tracks = pd.read_csv(META_DIR, index_col=0, header=[0, 1])

keep_cols = [('set', 'split'), ('set', 'subset'), ('track', 'genre_top')]

df_all = tracks[keep_cols]
df_all = df_all[df_all[('set', 'subset')] == 'small']

df_all['track_id'] = df_all.index

grouped_df = df_all.groupby(('track', 'genre_top')).first().reset_index()

for index, row in grouped_df.iterrows():
    track_id = int(row['track_id'])
    genre = row[('track', 'genre_top')]
    mfcc_calc(track_id, genre)

plt.show()
