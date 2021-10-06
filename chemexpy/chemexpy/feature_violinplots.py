#Libraries----------------------------------------------------------------------

"""
Dependencies and modules necessary for analytical functions to work
"""


import seaborn as sns
import matplotlib.pyplot as plt




##Exploratory plots----------------------------------------------------------------------



def feature_violinplots(data,var1=None,type=None):
   
    """
    Function takes the data file provided by data_prep function and plots analytical violin plots to assess type distribution for selected fetaures.
    Note categorical type data needs to be provided, such as active or inactive, etc.

    Input: data frame generated by the data_prep function, as well as a variable name which distribution will be checked, e.g. "MW" and "TSPA", also a column name is required to select categorical data specified through "type" designation.

    Output: contour plot with feature distribution
    """

    #Error handling
    if var1 is None:
        print("Please enter a var1 for feature check")
        return data.head()
    #Missing data capture

    if var1 not in data.columns:
        print("%s variable is not in the data frame provided" % var1)
        return (data.head())


    if type not in data.columns:
        print("%s variable is not in the data frame provided" % Type)
        return (data.head())

    if type is None:
        print("Function provides feature distribution across specific conditions; that is, compound type categories, e.g. active and inactive. Please, supply this information.")

    #Plot

    #set values for plotting 
  

    data[var1] = data[var1].astype(float)
   
    data[type] = data[type].astype(str)


    #violin plot
    sns.violinplot(x=data[type], y=data[var1])
    plt.show()

    return