import pandas as pd

data = {
    'artist': ['A', 'A', 'B', 'A', 'C', 'B', 'A'],
    'venue': ['X', 'Y', 'X', 'X', 'Y', 'Y', 'Y'],
    'date': pd.to_datetime([
        '2023-01-01', '2023-01-15', '2023-01-20',
        '2023-02-01', '2023-02-05', '2023-02-10', '2023-03-01'
    ])
}

df = pd.DataFrame(data)

df['yearmonth'] = df['date'].dt.to_period('M')

artists = pd.Series(df['artist'].unique())
venues = pd.Series(df['venue'].unique())

artist_venue_pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

concertcounts = (
    df.groupby(['yearmonth', 'artist', 'venue'])
      .size()
      .unstack(['artist', 'venue'])
      .reindex(columns=artist_venue_pairs, fill_value=0)
      .fillna(0)
)

concertcounts.index = concertcounts.index.astype(str)

print(concertcounts)