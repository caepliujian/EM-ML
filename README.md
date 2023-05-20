# **EM-ML Users Guidance** #
Machine learning module of EM-Studio for predicting the properties of energetic molecules. 

## Author: ##
- **Dr. Jian Liu**, liujian-12@caep.cn, Institute of Chemical Materials, CAEP
## Requirements:  ##
1. ananconda
2. python 3.8
2. chemProp 2023
3. descriptastorus 2.6.0
4. rdkit 2022.9.5
5. torch 1.12.0
6. pandas 1.4.3
7. numpy 1.24.3
8. typing
9. pyDes
10. psutil
## Usage: ##
    python EMML_predAll.py -i [input csv file]
*The format of csv file is as follows:*

    ID,smiles
    BNFF,O=[N+]([O-])c1nonc1-c1nonc1-c1nonc1[N+](=O)[O-]
    DNPP,O=[N+]([O-])c1n[nH]c2c([N+](=O)[O-])n[nH]c12
    ...,...
## Example: ##
    python EMML_predAll.py -i Example.csv

*The result will be written to **pred_Example.csv**.*