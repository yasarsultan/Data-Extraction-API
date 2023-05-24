import requests
import pandas as pd

def main():
    # Calling api
    url = "http://data.fixer.io/api/latest?access_key=7bc643487cdb57f1d92bdd4fa5c7ebdb"
    text = requests.get(url)
    # print(text.json())

    dataframe = pd.DataFrame(text.json())
    # print(dataframe)

    dataframe.drop(columns=['success', 'timestamp', 'base', 'date'], inplace=True)
    dataframe.rename(columns={"rates": "EUR_rates"}, inplace=True)
    # print(dataframe)

    dataframe.to_csv("exchangerates.csv")

main()