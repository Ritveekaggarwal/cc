import pandas as pd

data = {
    'refund' : ["yes", "no" , "no", "yes" , "no", "no","yes", "no", "no", "no"],
    'Marital status' : ["single","married","single","married","divorced","married","divorced","single","married","single"],
    'taxable income(k)' : [125,100,70,120,95,60,220,85,75,90],
    'cheat' : ["no","no","no","no","yes","no","no","yes","no","yes"]
}

df = pd.DataFrame(data)
print(df)