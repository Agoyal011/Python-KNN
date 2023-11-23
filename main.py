import pandas as pd
import numpy as np





df = pd.read_csv("C:/Users/Aniket/AI_datasets/new_bc_data.csv")

print(df)
df = df.drop("Unnamed: 0", axis=1)
print(df)


df = df.rename(columns={"Diagnosis":"label"})
print(df)


def my_function(dataframe, proportion_tr, proportion_test):

    train = dataframe.sample(frac=proportion_tr, random_state=200)  # random state is a seed value
    test = dataframe.drop(train.index)
    print(train)
    print(test)
    print(len(train))
    print(len(test))

    return train, test


train, test = my_function(df,0.7,0.3)


