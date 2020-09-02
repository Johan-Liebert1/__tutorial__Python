import requests
import datetime
from requests_html import HTML
import pandas as pd

now = datetime.datetime.now()
year = now.year

url = "https://www.boxofficemojo.com/year/world/"


def url_to_text(url, save = False):

    r = requests.get(url)

    if r.status_code == 200:
        html = r.text

        if save:
            with open(f'world-{year}.html', 'w') as f:
                f.write(html)

        return html

    return ""

html_text = url_to_text(url)
r_html = HTML(html = html_text)

table_class = ".imdb-scroll-table"

r_table = r_html.find(table_class)

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
df.to_csv('movies.csv', index=False)