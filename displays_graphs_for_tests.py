import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from data_analysis_for_training import data_analysis

graph = data_analysis()
graph.load_data('true')
dict_buy,dict_no_buy = graph.analysis()
custom_buy,custom_no_buy = graph.get_len_list()

df_buy = pd.DataFrame(list(dict_buy.items()),columns=['parameter','count'])
df_no_buy = pd.DataFrame(list(dict_no_buy.items()),columns=['parameter','count'])
# מחלצים מונה לכל ערך
def get_numerator(value, total):
    return f'{int(value * total)}/{total}'
df_buy['label'] = df_buy['count'].apply(lambda x: get_numerator(x, custom_buy))
df_no_buy['label'] = df_no_buy['count'].apply(lambda x: get_numerator(x, custom_no_buy))
fig1 = plt.figure(figsize=(6,5))
bars_1 = plt.bar(df_buy['parameter'],df_buy['count'],color='green',label='buy')
for bar, label in zip(bars_1, df_buy['label']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.01, label,ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=45)
# plt.show()
st.pyplot(fig1)
fig2 = plt.figure(figsize=(6,5))
bars_2 = plt.bar(df_no_buy['parameter'],df_no_buy['count'],alpha=0.6,color='red',label='not buy')
for bar, label in zip(bars_2, df_no_buy['label']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.01, label,ha='center', va='bottom',fontsize=10)
plt.xticks(rotation=45)
# plt.show()
st.pyplot(fig2)
print(dict_buy)
print(dict_no_buy)
