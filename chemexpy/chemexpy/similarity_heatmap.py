#Libraries----------------------------------------------------------------------

"""
Dependencies and modules necessary for analytical functions to work
"""

#Cheminformatics
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Descriptors
from rdkit.Chem import PandasTools
from rdkit import DataStructs

#Data processing
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt





#Similarity analysis----------------------------------------------------------------------


def similarity_heatmap(data):

    """
    Function takes the data file provided by the data_prep function and plots a heatmap based on compound similarity.
    Fingerprinting is based on Morgan fingerprints and similarity search is based on Tanimoto Similarity.
    #Input: data frame generated by the data_prep function.
    #Output: heatmap and a data frame with similarity values.
    """

    radius=2
    nBits=1024

    #generate fingerprints for database of compounds
    ECFP6_data = [AllChem.GetMorganFingerprintAsBitVect(mol,radius=radius, nBits=nBits) for mol in data['Rdkit_mol']]
    data["Morgan_fpt"]=ECFP6_data


    #build array with similarity scores
    length=len(ECFP6_data)
    array=pd.DataFrame(index=range(length),columns=range(length))
    data['CID']=data.CID.apply(str)
    array.columns=list(data.CID)
    array.index=list(data.CID)

    for i in range(length):
        var1=list(data.CID)[i]
        mol1=list(data.Morgan_fpt)[i]
        for j in range(length):
            #calculate similarity
            var2=list(data.CID)[j]
            mol2=list(data.Morgan_fpt)[j]
            similarity=DataStructs.FingerprintSimilarity(mol1,mol2)
            array.loc[var1,var2]=similarity
         
    

    array=array.astype(float)


    #plot heatmap and dendogram
   
    sns.clustermap(array, metric="euclidean", method="single", cmap='mako')


    plt.show()



    return (array)