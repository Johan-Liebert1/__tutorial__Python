import requests
import datetime
from requests_html import HTML
import pandas as pd
import os

# rgb(119, 255, 255)

BASE_DIR = os.path.dirname(__file__)

now = datetime.datetime.now()
year = now.year

def url_to_text(url, save = False):

    r = requests.get(url)

    if r.status_code == 200:
        html = r.text

        if save:
            with open(f'world-{year}.html', 'w') as f:
                f.write(html)

        return html

    return ""

def parse_and_extract(url, name = "2020"):

    html_text = url_to_text(url)
    r_html = HTML(html = html_text)

    table_class = ".imdb-scroll-table"

    r_table = r_html.find(table_class)

    if len(r_table) > 0:

        parsed_table = r_table[0]

        rows = parsed_table.find('tr')

        header = rows[0]
        header_cols = header.find('th')
        header_names = [x.text for x in header_cols]
        table_data = []

        for row in rows[1:]:
            cols = row.find('td')
            row_data = []

            for i, col in enumerate(cols):
                row_data.append(col.text)

            table_data.append(row_data)

    df = pd.DataFrame(table_data, columns = header_names)

    # setting up the correct path
    PATH = os.path.join(BASE_DIR, 'data')
    os.makedirs(PATH, exist_ok = True)
    filepath = os.path.join('data', f'{name}.csv')

    df.to_csv(filepath, index=False)


for year in range(2010, 2021):

    url = f"https://www.boxofficemojo.com/year/world/{year}"

    parse_and_extract(url, name = year)