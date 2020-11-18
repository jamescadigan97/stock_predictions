import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
import csv
import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv('stock_predictions/App/Resources/EDU.csv')
print(df)


# plt.scatter(df['PE'], df['PRICE'], color='red')
# plt.title('PRICE Vs PE', fontsize=14)
# plt.xlabel('PE', fontsize=14)
# plt.ylabel('PRICE', fontsize=14)
# plt.grid(True)
# plt.show()

X = df[['MARKETCAP','PB']].astype(float) # here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['PRICE'].astype(float) # output variable (what we are trying to predict)

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# tkinter GUI
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)

# New_Market_Cap label and input box
label1 = tk.Label(root, text=' Type Market Cap: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

# New_PB label and input box
label2 = tk.Label(root, text=' Type Price to Book: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)

def values(): 
    global New_Market_Cap #our 1st input variable
    New_Market_Cap = float(entry1.get()) 
    
    global New_PB #our 2nd input variable
    New_PB = float(entry2.get()) 
    
    Prediction_result  = ('Predict Stock Price: ', regr.predict([[New_Market_Cap ,New_PB]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)

button1 = tk.Button (root, text='Predict Stock Price',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)

#plot 1st scatter 
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['MARKETCAP'].astype(float),df['PRICE'].astype(float), color = 'r')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['PRICE']) 
ax3.set_xlabel('MARKETCAP')
ax3.set_title('MARKETCAP Vs. Stock Price')


#plot 2nd scatter 
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['PB'].astype(float),df['PRICE'].astype(float), color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root) 
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['PRICE']) 
ax4.set_xlabel('PB')
ax4.set_title('PB Vs. Stock Price')


root.mainloop()



# # with statsmodels
# X = sm.add_constant(X) # adding a constant
 
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X) 
 
# print_model = model.summary()
# print(print_model)


# plt.rc('figure', figsize=(12, 7))
# #plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
# plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
# plt.axis('off')
# plt.tight_layout()
# plt.savefig('edu_output.png')