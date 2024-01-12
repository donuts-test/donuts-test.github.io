import pandas as pd
import yaml

sheet_id = "1GhfX1QMrokc2cWaUUMfuTRBlbEmYqf2gLgEB-oobCBM"
sheet_name = "news"
news_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
news = pd.read_csv(url)


data_dict = news.to_dict(orient='records')

with open('_data/news.yaml', 'w') as file:
    yaml.dump(data_dict, file)



