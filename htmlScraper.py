from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import requests
from tabulate import tabulate
from html.parser import HTMLParser

path = ("file_name.html")

with open(path, 'r', encoding='utf-8') as file:
  html_content = file.read()

html_page = bs(html_content, 'html.parser')

persons = html_page.find_all("table",attrs={"id":"StudentTable"})

StudentRecord = []
for i in persons:
  a = f"{persons.index(i)+1}: {i}"
  html = bs(a, 'html.parser')
  b = html.find_all("table", attrs={"id":"RequirementTable"})
  StudentRecord.append(b)
first_Student = StudentRecord[0]

from sre_constants import IN_IGNORE
all_data = []
proReq = first_Student.find_all("table", attrs={"id": "RequirementTable"})
for req in proReq:
    soup = bs(str(req), "html.parser")
    reqName = soup.find("span", attrs={"class": "ReqName"})
    pattern = r'(?<=:\s).*?(?=\s\()'
    reqName = reqName.get_text()
    reqName = re.findall(pattern, reqName)

    tables = req.find_all("table", attrs={"id": "CoursesTable"})
    for table in tables:
        if table:
            rows = table.find_all('tr')
            data = []
            for row in rows:
                columns = row.find_all('td')
                row_data = [col.text.strip() for col in columns]
                data.append(row_data)
            if data:
                df = pd.DataFrame.from_dict(data, orient='columns', dtype=None, columns=None)
                data = [subarray for subarray in data if len(subarray) > 0]
                header = data[0]
                data = data[1:]
                df1 = pd.DataFrame(data)
                df1 = df1.reset_index(drop=True)
                df1['Sub_ReqGroup'] = "subject_names"
                df1['ReqGroup'] = reqName[0]
                list = df1.values.tolist()
                all_data.append(list)

flat_list = []
header1 = [['SNo', 'Course', 'Title', 'Needed', 'Term', 'Grade', 'Credits', '', 'Notes', 'SubGrp', 'ReqGroup']]
for sublist in all_data:
    for subsublist in sublist:
        flat_list.append(subsublist)
df2 = pd.DataFrame(flat_list, columns=header1)
df2.to_csv('output.csv', index=False)