# necessary import libraries
import numpy as np
import datetime,time
from sklearn.linear_model import LinearRegression

# dummy inputs (one day)
data=[10.0,11.1,12.3,13.2,14.8,15.6,16.7,17.5,18.9,19.7,20.7,21.1,22.6,23.5,24.9,25.1,26.3,27.8,28.8,29.6,30.2,31.6,32.1,33.7]
startDate = '2013-01-01'
endDate = '2013-01-01'
p = 1
n = 1

# utility function
def predictTemperature(startDate, endDate, temperature, n):
    # Extracting number of days from the input data
    days = int(len(temperature)/24)

    # Constructing Input data by serializing the given hours
    train_inputs = []
    for i in range(1,((24*days)+1)):
        train_inputs.append(i)

    # Constructing Target data
    target = temperature

    # Choosing Linear Regression Model
    lin_reg = LinearRegression()
    lin_reg.fit(np.asarray(train_inputs).reshape(-1,1),target)

    # Constructing Input Data for the prediction
    # Using the last hour and incrementing it by 1, It will be our starting point for Prediction Input
    start = train_inputs[-1] + 1
    pred_input = []
    for i in range(24*n):
        pred_input.append(start+1)
        start += 1

    # Predicting with the constructed input
    pred = lin_reg.predict(np.asarray(pred_input).reshape(-1,1).tolist())

    return pred

# call the utility function
print(predictTemperature(startDate, endDate, data, n))