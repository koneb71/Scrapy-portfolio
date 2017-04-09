import pandas as pd

df = pd.read_csv("mongodb_results.csv")

df.dropna(axis=1, how="all", inplace=True)


df = df[[u'company', u'website', u'level', u'type', u'certified', u'industry', u'region', u'technology', u'description', u'language',
       u'src']]

df.to_csv("mongodb_results.csv", index=False)
