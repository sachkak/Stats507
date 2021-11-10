# Stats507

[PS2Q3.py](./PS2Q3.py) is a part of HW 6 for Stats 507.

The script uses Pandas to read, clean, and append data files spanning the years 2011-2018 for the National Health and Nutrition Examination Survey NHANES, and for the oral health and dentition data.

For the National Health and Nutrition Examination Survey NHANES, the following variables are kept: the unique ids (SEQN), age (RIDAGEYR), race and ethnicity (RIDRETH3), education (DMDEDUC2), marital status (DMDMARTL), and survey weighting variables (RIDSTATR, SDMVPSU, SDMVSTRA, WTMEC2YR, WTINT2YR). 

For the oral health and dentition data (OHXDEN_*.XPT), the following variables are kept: SEQN, OHDDESTS, tooth counts (OHXxxTC), and coronal cavities (OHXxxCTC).
