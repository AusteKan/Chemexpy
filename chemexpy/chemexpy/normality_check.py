#Libraries----------------------------------------------------------------------

"""
Dependencies and modules necessary for analytical functions to work
"""


#Data processing

import scipy
from scipy import stats
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt


##Exploratory plots----------------------------------------------------------------------

def normality_check(data,var=None):
   
    """
    Function takes the data file provided by the data_prep function and plots histogram with estimated probability density function.
    #Input: data frame generated by the data_prep function, as well as a single variable to check normality, e.g. "MW" and "TSPA".
    #Output: bar plot with an estimated normal distribution line plot based on distribution probability.
    """
    #Error handling
    if var is None:
        print("Please enter a variable to check normality for")
        return data.head()
    #histogram and normal probability plot
    if var not in data.columns:
        print("%s not in the data frame" % var)
        return data.head()
    
  

    x=data[var]
    ax = sns.histplot(x, kde=False, stat='density')

    # calculate the PDF
    x0, x1 = ax.get_xlim()  # extract the endpoints for the x-axis
    x_pdf = np.linspace(x0, x1, 100)
    y_pdf = scipy.stats.norm.pdf(x_pdf, loc = x.mean(), scale = x.std())
    ax.plot(x_pdf, y_pdf, 'r', lw=2, label='pdf')                                                   
    ax.legend()
    plt.show()


    return