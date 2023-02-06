import pandas as pd
time_series = pd.Series(time_list)
average_time = pd.to_timedelta(time_series.mean()).components.hours