from sqlalchemy import create_engine
import pandas as pd
import uuid
import datetime
import os

db_pass = os.environ['DB_PASS']
engine = create_engine(f'postgresql://postgres:{db_pass}@halfwayhouse-local.ddns.net:5432/postgres')


def is_disk(s):
    return s.find("sd") >= 0


def main():
    df = pd.read_csv("tmp.txt", delim_whitespace=True)
    df['is_disk'] = [is_disk(x) for x in df['Filesystem']]
    df = df[df['is_disk']]
    df = df[['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted']]
    df['Size GB'] = df['1K-blocks'] / 1024 / 1024
    df['Used GB'] = df['Used'] / 1024 / 1024
    df['Available GB'] = df['Available'] / 1024 / 1024
    df = df[['Filesystem', 'Size GB', 'Used GB', 'Available GB', 'Use%', 'Mounted']]
    df['id'] = [str(uuid.uuid4()) for x in range(len(df))]
    df['date'] = datetime.datetime.now()
    df.to_sql('starmie_disk_space', con=engine, if_exists='append', index=False)


if __name__ == "__main__":
    main()
