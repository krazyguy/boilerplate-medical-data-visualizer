import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df =  pd.read_csv("medical_examination.csv")


df['overweight'] = np.where((df['weight'] / (df['height']/100) ** 2) >25 ,1,0)


df['gluc'] = np.where((df['gluc']) >1 ,1,0)
df['cholesterol'] = np.where((df['cholesterol']) >1 ,1,0)


def draw_cat_plot():
    
    df_cat = pd.melt(df, id_vars = "cardio", var_name = 'variable', value_vars = ['active','alco', 'cholesterol', 'gluc', "overweight",'smoke'])




    
    df_cat = pd.melt(df, id_vars = "cardio", var_name = 'variable', value_vars = ['active','alco', 'cholesterol', 'gluc', "overweight",'smoke'])

    

    



    
    fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("variable", "total").fig




    
    fig.savefig('catplot.png')
    return fig



def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
(df['height'] >= df['height'].quantile(0.025)) &
(df['height'] <= df['height'].quantile(0.975)) &
(df['weight'] >= df['weight'].quantile(0.025))&
(df['weight'] <= df['weight'].quantile(0.975))  ]

    
    corr=df_heat.corr()
    

    
    mask = mask=np.triu(np.ones_like(corr, dtype=bool))



    
    fig, ax =  plt.subplots(figsize=(11, 9))

    
    sns.heatmap(corr,mask=mask,ax=ax, fmt='.1f',vmax=.3, linewidths=.5,square=True,annot=True, center=0,cbar_kws={'shrink': 0.5}
)



    
    fig.savefig('heatmap.png')
    return fig
