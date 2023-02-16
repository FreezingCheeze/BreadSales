from datetime import datetime
from meteostat import Point, Daily

datetime_2021_start = datetime(2021, 1, 4)
datetime_2021_end = datetime(2022, 1, 2)
location_jumbo_508 = Point(53.207500, 6.591850)

# Get meteostat params by start, end and location
def get_daily_data(start = datetime_2021_start, end = datetime_2021_end, location = location_jumbo_508):
    data = Daily(location, start, end)
    data = data.fetch()
    return data

# Plot line including average, minimum and maximum
# data = get_daily_data()
# data.plot(y=['tavg', 'tmin', 'tmax'])
# plt.show()

