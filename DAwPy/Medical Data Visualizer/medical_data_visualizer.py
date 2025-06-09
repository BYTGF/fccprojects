import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (bmi > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="total")

    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', data=df_cat, kind='bar', col='cardio')

    # 8
    fig.savefig('catplot.png')
    return fig

# 9
def draw_heat_map():
    # 10
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11
    corr = df_heat.corr()

    # 12
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13
    fig, ax = plt.subplots(figsize=(10, 8))

    # 14
    sns.heatmap(corr, cmap="YlGnBu", annot=True, mask=mask, ax=ax)

    # 15
    fig.savefig('heatmap.png')
    return fig
