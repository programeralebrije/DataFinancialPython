import pandas as pd
import matplotlib.pyplot as plt
 url = 'http://apmonitor.com/che263/uploads/Main/goog.csv'
    data = pd.read_csv(url, header=None, parse_dates=[0], index_col=0, squeeze=True)    # read data from url
    data.plot()   
    
    data = pd.read_csv(url)
print(data['Close'][0:5])
print('min: '+str(min(data['Close'][0:20])))
print('max: '+str(max(data['Close'][0:20])))

# plot data with pyplot
plt.figure()
plt.plot(data['Open'][0:20])
plt.plot(data['Close'][0:20])
plt.xlabel('days ago')
plt.ylabel('price')
plt.show()
                                                                     # plot data