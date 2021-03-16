import pandas as pd
import dask.dataframe as dd

a = pd.read_csv('PopulationBySex.csv')
print(a.head())

b = dd.read_csv('PopulationBySex.csv')
print(b.compute())

import pyspark as spark
#from pyspark import SparkContext, SQLContext

ac = spark.SparkContext()
s = spark.SQLContext(ac)

c = s.read.format("PopulationBySex.csv").options(header=True)

