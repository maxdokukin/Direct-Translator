import pandas as pd

df1 = pd.read_csv(r'/Users/xewe/Documents/Hobbies/Programming/Python/Direct-Translator/data/russian-dictionary/adjectives.csv', sep='\t')
df2 = pd.read_csv(r'/Users/xewe/Documents/Hobbies/Programming/Python/Direct-Translator/data/russian-dictionary/nouns.csv', sep='\t')
df3 = pd.read_csv(r'/Users/xewe/Documents/Hobbies/Programming/Python/Direct-Translator/data/russian-dictionary/others.csv', sep='\t')
df4 = pd.read_csv(r'/Users/xewe/Documents/Hobbies/Programming/Python/Direct-Translator/data/russian-dictionary/verbs.csv', sep='\t')

df1.drop(columns=['accented', 'translations_de'], inplace=True)
df2.drop(columns=['accented', 'translations_de'], inplace=True)
df3.drop(columns=['accented', 'translations_de'], inplace=True)
df4.drop(columns=['accented', 'translations_de'], inplace=True)

df1 = df1.melt(
    id_vars=['translations_en'],
    value_vars=[
        'bare', 'comparative', 'superlative', 'short_m', 'short_f', 'short_n', 'short_pl',
        'decl_m_nom', 'decl_m_gen', 'decl_m_dat', 'decl_m_acc', 'decl_m_inst', 'decl_m_prep',
        'decl_f_nom', 'decl_f_gen', 'decl_f_dat', 'decl_f_acc', 'decl_f_inst', 'decl_f_prep',
        'decl_n_nom', 'decl_n_gen', 'decl_n_dat', 'decl_n_acc', 'decl_n_inst', 'decl_n_prep',
        'decl_pl_nom', 'decl_pl_gen', 'decl_pl_dat', 'decl_pl_acc', 'decl_pl_inst', 'decl_pl_prep'
    ],
    value_name='value'
)

df2 = df2.melt(
    id_vars=['translations_en'],
    value_vars=[
        'bare',
        'sg_nom', 'sg_gen', 'sg_dat', 'sg_acc', 'sg_inst', 'sg_prep',
        'pl_nom', 'pl_gen', 'pl_dat', 'pl_acc', 'pl_inst', 'pl_prep'
    ],
    value_name='value'
)

df3 = df3.rename(columns={'bare': 'value'})
df3 = df3[['translations_en', 'value']]

df4 = df4.melt(
    id_vars=['translations_en'],
    value_vars=[
        'bare', 'partner', 'imperative_sg', 'imperative_pl',
        'past_m', 'past_f', 'past_n', 'past_pl',
        'presfut_sg1', 'presfut_sg2', 'presfut_sg3',
        'presfut_pl1', 'presfut_pl2', 'presfut_pl3'
    ],
    value_name='value'
)

df1.drop(columns=['variable'], inplace=True)
df2.drop(columns=['variable'], inplace=True)
df4.drop(columns=['variable'], inplace=True)

print(df1.columns)
print(df2.columns)
print(df3.columns)
print(df4.columns)

merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)
merged_df = merged_df.map(lambda x: x.replace("'", "") if isinstance(x, str) else x)
merged_df = merged_df[['value', 'translations_en']]
merged_df.rename(columns={'value': 'ru', 'translations_en': 'en'}, inplace=True)
merged_df.dropna(inplace=True)

print(merged_df.columns)
print(len(merged_df))

merged_df.to_csv("data/dictionary.csv", index=False)
