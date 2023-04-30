import pandas as pd

print("Hello World!")

Names = ["Iga", "Radek", "Krystian", "Maciek", "Madzia"]
Ages = [22,24,25,24,13]

df = pd.DataFrame(Names,columns = ["Names"])

df['Ages'] = Ages
                   
print(df)

df.describe()