import pandas


print("Human Data")
df1=pandas.read_csv("debug_data/debugdata_human.csv")
print(df1)


print("\n\nAI data")
df=pandas.read_csv("debug_data/debugdata_ai.csv")
print(df)


print()

# df2=pandas.read_csv("debug_data/initialBoard.csv")
# print(df2)
