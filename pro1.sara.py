import numpy as np
import pandas as pd
from fontTools.misc.cython import returns
from khayyam import JalaliDatetime, JalaliDate

#Read Excel and convert to csv
x = pd.read_excel("e1.xlsx")
x.to_csv("data.csv")
x = pd.read_csv("data.csv")

#Convert to dataframe
df = pd.DataFrame(x)

#Print dataframe
print(df)
print("-"*50)

#Chack types of data
print(df.dtypes)
print("-"*50)

#Information of data
print(df.shape)
print(df.size)
print(df.ndim)
print("-"*50)

#Check information
df.info()
print("-"*50)

#Check false dtypes
print(df.columns.tolist())
df[["Quantity", "UnitPrice", "CustomerID"]] = df[["Quantity", "UnitPrice", "CustomerID"]].apply(pd.to_numeric, errors="coerce")
df[["InvoiceDate"]] = df[["InvoiceDate"]].apply(pd.to_datetime, errors="coerce")
print(df)
print("-"*50)

#Chack None data
print(df.isna())
print(df.isna().sum())
print("-"*50)

#Remove row that has None data
print(df.dropna())
print("-"*50)

#Inplace None data
print(df.fillna(1000, inplace=True))
#print(df.fillna(method="ffill", inplace=True))
#print(df.fillna(method="bfill", inplace=True))
print("-"*50)

#Describe of data
print(df.describe())
print("-"*50)

#Check allowable range
print(df[["UnitPrice"]]>=20)
print(df[["CustomerID"]]>=20000)
print(df[["Quantity"]]>=500)
print("-"*50)

#Min & Max
print("Min:")
print(df[["Quantity"]].min(axis=0))
print("Max:")
print(df[["Quantity"]].max(axis=0))
print("-"*50)

#Production
print("Product:")
print(df[["Quantity"]].prod())
print("-"*50)

#Print data by location of index
print(df[["InvoiceNo","Description"]].iloc[0])
print("-"*50)

#Performing comparison operations on columns
mask = df[["CustomerID"]]>17000
print(mask)
print(df[["CustomerID"]][mask])
print(df[["CustomerID"]].where(df[["CustomerID"]]>17500))
print("-"*50)

#Make column letters smaller
df["Description"] = df["Description"].astype(str)
df["Description"] = df["Description"].str.lower()
print(df[["Description"]])
print("-"*50)

#Remove duplicate rows
print(df.duplicated())
print(df.duplicated().sum())
print("-"*50)

#Convert milady to Shamsi
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
def convert_date(milady_date):
    return JalaliDatetime(milady_date).strftime("%Y/%m/%d")
df["Persian"] = df["InvoiceDate"].apply(convert_date)
print(df["Persian"])
print("-"*50)