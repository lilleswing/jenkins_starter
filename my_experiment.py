import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

_GRID_LINE_PROPERTIES = dict(color='#bdbdbd', linestyle='--', linewidth=0.5)

US_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
GLOBAL_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
             "/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


def download_files():
    r = requests.get(US_URL)
    with open('us.csv', 'wb') as fout:
        fout.write(r.content)

    r = requests.get(GLOBAL_URL)
    with open('global.csv', 'wb') as fout:
        fout.write(r.content)


def get_nyc_table():
    df = pd.read_csv('us.csv')
    df = df[df['Province_State'] == 'New York']
    df = df[df['Admin2'] == 'New York']
    d = df.to_dict()
    dates, deaths = [], []
    for k, v in d.items():
        try:
            my_date = datetime.datetime.strptime(k, '%m/%d/%y')

            dates.append(my_date)
            deaths.append(list(v.values())[0])
        except:
            pass
    nyc_table = pd.DataFrame(list(zip(dates, deaths)))
    nyc_table['delta'] = nyc_table.diff()[1]
    nyc_table = nyc_table.dropna()
    return nyc_table


def get_us_table():
    df = pd.read_csv("global.csv")
    df = df[df['Country/Region'] == 'US']
    dates, deaths = [], []
    d = df.to_dict()
    for k, v in d.items():
        try:
            my_date = datetime.datetime.strptime(k, '%m/%d/%y')

            dates.append(my_date)
            deaths.append(list(v.values())[0])
        except:
            pass
    us_table = pd.DataFrame(list(zip(dates, deaths)))
    us_table['delta'] = us_table.diff()[1]
    us_table = us_table.dropna()
    return us_table


def save_plots(nyc_table, us_table):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    fig.autofmt_xdate()

    ax1.plot(nyc_table[0][-20:], nyc_table['delta'][-20:], linewidth=1.5)
    ax1.grid(**_GRID_LINE_PROPERTIES)
    ax1.set_title("NYC Deaths Per Day")

    ax2.plot(us_table[0][-20:], us_table['delta'][-20:], linewidth=1.5)
    ax2.grid(**_GRID_LINE_PROPERTIES)
    ax2.set_title("US Deaths Per Day")
    plt.savefig('deaths_per_day.png')


def main():
    download_files()
    nyc_table = get_nyc_table()
    us_table = get_us_table()
    save_plots(nyc_table, us_table)


if __name__ == "__main__":
    main()
