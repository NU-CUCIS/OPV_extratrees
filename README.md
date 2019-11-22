# OPV_extratrees
Organic solar cells are an inexpensive, flexible alternative to traditional silicon-based solar cells. In this work, extremely randomized tree learning models are employed for the prediction of HOMO values for donor molecules in organic solar cells. The proposed model outperform neural networks trained on molecular fingerprints as well as SMILES, as well as other state-of-the-art architectures such as Chemception and Molecular Graph Convolution on two datasets of varying sizes.

Requirements: 
1. Keras 2.0 or higher
2. Tensorflow 1.7 
1. RDKit 2017.09.1
2. Scikit-Learn 0.19.1
5. Numpy 1.14
6. Pandas 0.22

## Files

#### Core Files
- ml_util.py: Utility file for basic machine learning methods
- rdkit_util.py: Utility file for RDKit methods (for fingerprint generation/transformation etc)

#### Notebooks 
- analyzeMonomers.ipynb: Explore the molecules that are best and worst predicted as well as with least and highest HOMO values
- ml_1024bit_fingerprints.ipynb: Explore ML models on 1024 bit compressed fingerprints  
- ml_reduced_fingerprints.ipynb: Explore ML models on reduced fingerprints (after feature selection on original uncompressed fingerprints)
- correlation.ipynb: Explore the correlation among top predictors (features) and target variable (HOMO) 
- ml_experimental_OPV.ipynb: Explore ML on the experimental part of the HOPV dataset 
- gridsearch.ipynb: Grid Search models 
- ml_calculate_boltzmann.ipynb: Explore ML models after calculating boltzmann average for the conformers of each molecule (other models are based on arithmetic average) 

## Data 
HOPV_15.data contains the DFT (for all conformers) and experimental values for the HOPV dataset 

## Developer Team

The code was developed by the <a href="http://cucis.ece.northwestern.edu/">CUCIS</a> group at the Electrical and Computer Engineering Department at Northwestern University. 

1. Arindam Paul (arindam.paul@eecs.northwestern.edu)
2. Ankit Agrawal (ankitag@eecs.northwestern.edu)
3. Wei-keng Liao (wkliao@eecs.northwestern.edu)
4. Alok Choudhary (choudhar@eecs.northwestern.edu)


The development team would like thank our collaborator <a href="https://www.feinberg.northwestern.edu/faculty-profiles/az/profile.html?xid=40386">Prof. Alona Furmanchuk</a> from <a href="https://www.feinberg.northwestern.edu/">Northwestern Feinberg School of Medicine</a>. 

## Citation

If you use this code or data, please cite:

Arindam Paul, Alona Furmanchuk, Wei-keng Liao, Alok Choudhary, Ankit Agrawal. Property Prediction of Organic Donor Molecules for Photovoltaic Applications using Extremely Randomized Trees. Journal of Molecular Informatics, 2019

## Questions/Comments:

email: arindam.paul@eecs.northwestern.edu or ankitag@eecs.northwestern.edu</br>
Copyright (C) 2019, Northwestern University.<br/>
See COPYRIGHT notice in top-level directory.

## Funding Support

This work was performed under the following financial assistance awards 70NANB14H012 and 70NANB19H005 from U.S. Department of Commerce, National Institute of Standards and Technology as part of the Center for Hierarchical Materials Design (CHiMaD). Partial support is also acknowledged from DOE awards DE-SC0014330, DE-SC0019358.
