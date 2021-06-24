import numpy as np 
#find today's date
today_d = np.datetime64('today','D')
print("The date today is", today_d)
  
# find yesterday's date by subtracting 1
yesterday_d = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  
print("Yester day's  date was ", yesterday_d)
  
# find tomorrow's date by adding 1
tomorrow_d = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  
print("Tomorrow date is ", tomorrow_d)