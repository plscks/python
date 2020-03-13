# COVID-19 Data pull class
# version 0.1
# written by plscks
# [X]  Pull data from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data in .csv format
# [X]  Parse data
# [X]  Output data
# []  Format data for input to I2C screen output
#
import datetime
import pandas as pd

def dataGrab():
    now = datetime.datetime.now()
    csvFormat = f'{now.month:02d}-{(now.day-1):02d}-{now.year}.csv'
    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{csvFormat}'
    df = pd.read_csv(url,names=['Province', 'Country', 'Updated', 'Confirmed', 'Deaths', 'Recovered', 'Latitude', 'Longitude'], skiprows=1)
    return df

def parseData(region, df):
    if region == 'world':
        worldTotals = []
        worldTotals.append(df.Confirmed.sum())
        worldTotals.append(df.Deaths.sum())
        return worldTotals
    elif region == 'us':
        usTotals = []
        usTotals.append(df[df.Country == 'US'].Confirmed.sum())
        usTotals.append(df[df.Country == 'US'].Deaths.sum())
        return usTotals
    else:
        localTotals = []
        localTotals.append(df[df.Province == 'Illinois'].Confirmed.sum())
        localTotals.append(df[df.Province == 'Illinois'].Deaths.sum())
        return localTotals

def output(world, us, local):
    print('COVID-19 Data')
    print('~~~~~~~~~~~~~')
    print(f'Worldwide confirmed cases:   {world[0]}')
    print(f'Worldwide confirmaed deaths: {world[1]}')
    print('')
    print(f'US confirmed cases:  {us[0]}')
    print(f'US confirmed deaths: {us[1]}')
    print('')
    print(f'Illinois confirmed cases:  {local[0]}')
    print(f'Illinois confirmed deaths: {local[1]}')

if __name__ == "__main__":
    data = dataGrab()
    worldData = parseData('world', data)
    usData = parseData('us', data)
    localData = parseData('local', data)
    output(worldData, usData, localData)
