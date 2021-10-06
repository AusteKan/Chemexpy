#Libraries----------------------------------------------------------------------

"""
Dependencies and modules necessary for analytical functions to work
"""

import seaborn as sns
import matplotlib.pyplot as plt



##Exploratory plots----------------------------------------------------------------------



def correlation_plot(data,*args):

    """
    Function takes data file provided by the data_prep function and plots plots a correlation heatmap.
    #Input values: data frame generated by the data_prep function, as well as variables to calculate correlation and plot, e.g. #              "MW" and "TSPA".
                     If user does not select args, the default values will be used: "Atom_number","MW","TSPA","HBD_count","HBA_count","Rotatable_bond_count","MolLogP","Ring_number","AP".
    #Output values: scatter plot for correlation visualisation and a data frame with correlation values.
    """
    if len(args)>0:
        for var in args:
            if var not in data.columns:
                print("%s not in the data frame" % var)
                return data.head()
        values=list(args)

    if len(args)==0:
        values=["Atom_number","MW","TSPA","HBD_count","HBA_count","Rotatable_bond_count","MolLogP","Ring_number","AP"]
    
    #calculate correlation
    df_corr=data[values]
    df_corr=df_corr.astype(float) #to ensure that data is not 'object'

    corr=df_corr.corr()

    
    ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,annot=True,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,)
    ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right')
    plt.show()
    return corr