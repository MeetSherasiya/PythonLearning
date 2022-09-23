import pandas as pd
import datetime

def sentEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")

if __name__ == "__main__":
    df = df.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []

    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday) and yearNow not in item['Year']:
            sentEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

for i in writeInd:
    yr = df.loc[i, 'Year']
    df.loc[i, 'year'] = str(yr) + ',' + str(yearNow)

df.to_excel('data.xslx', index=False)