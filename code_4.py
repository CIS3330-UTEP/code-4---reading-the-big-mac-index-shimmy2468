import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3 == '{country_code.upper()}' and date <= '{year}-12-31' and date >= '{year}-01-01')"
    df_1 = df.query(query)
    price_by_year = df_1['dollar_price'].mean()

    return round(price_by_year, 2)

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code.upper()}')"
    df_2 = df.query(query)
    price_by_country= df_2['dollar_price'].mean()
   
    return round(price_by_country, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date <= '{year}-12-31' and date >= '{year}-01-01')"
    df_3 = df.query(query)
    index_min_value = df_3['dollar_price'].idxmin()
    output = df_3.loc[index_min_value]

    return f"{output['name']}({output['iso_a3']}): ${round(output['dollar_price'], 2)}" 


def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date <= '{year}-12-31' and date >= '{year}-01-01')"
    df_4 = df.query(query)
    index_max_value = df_4['dollar_price'].idxmax()
    output = df_4.loc[index_max_value]

    return f"{output['name']}({output['iso_a3']}): ${round(output['dollar_price'], 2)}" 

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2009, "mex"))
    print(get_big_mac_price_by_country("rus"))
    print(get_the_cheapest_big_mac_price_by_year(2016))
    print(get_the_most_expensive_big_mac_price_by_year(2016))


