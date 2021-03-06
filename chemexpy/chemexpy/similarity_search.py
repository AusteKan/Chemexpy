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



#Similarity analysis----------------------------------------------------------------------

def similarity_search(data, target=None):

    """
    Function takes the data file provided by the data_prep function and searches for similar structures based on the target molecule.
    Fingerprinting is based on Morgan fingerprints and similarity search is based on Tanimoto Similarity.
    #Input: data frame generated by the data_prep function, as well as a SMILE string (e.g., "target" variable) for a molecule to search the database. 
    #Output: data frame of similar structures.
    """
    if target is None:
        print("Please provide a SMILES string for a target molecule.")


    radius=2
    nBits=1024

    #generate fingerprints for database of compounds
    ECFP6_data = [AllChem.GetMorganFingerprintAsBitVect(mol,radius=radius, nBits=nBits) for mol in data['Rdkit_mol']]

    #generate fingerprints for the target
    target_mol = Chem.MolFromSmiles(target)
    target_ECFP4_fps = AllChem.GetMorganFingerprintAsBitVect(target_mol,2)

    #calculate similarity
    similarity_efcp4 = [DataStructs.FingerprintSimilarity(target_ECFP4_fps,mol) for mol in ECFP6_data]
    
    #add a new column to data file
    data['Tanimoto_Similarity_ECFP4'] = similarity_efcp4
    #sort values from highest to lowest similarity
    data = data.sort_values(['Tanimoto_Similarity_ECFP4'], ascending=False)

    #visualise the ouput
    PandasTools.FrameToGridImage(data.head(8), column= 'Rdkit_mol', legendsCol='Tanimoto_Similarity_ECFP4', molsPerRow=4)


    return (data)