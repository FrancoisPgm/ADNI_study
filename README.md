# ADNI_study

TO properly merge csv files from ADNI, one must combine different csv files while matching two columns:
- RID (the ID of the subject, regardless of the centre they were evaluated)
- VISODE (the time point in which they were assessed: sc=screening, m12= 1year, m24=2 years, etc)

This code will help you achieve that for each ADNI phase at the time point you want and can be easily modified for different csv files and variables

- [Dependencies](#dependencies)
- [Dataset structure](#dataset-structure)
- [How to run](#how-to-run)

## Dependencies

Python

## Dataset structure

csv files containing the variables of interest

## How to run

download the Github repo
~~~
cd ADNI_study-master
~~~
run the following:
~~~
python merge_csv.py -o OUTPUT_FILE_NAME.csv -p PHASE -v VISCODE.
~~~

Note: VISCODE and VISCODE are not the same. VISCODE is cohort specific and gets initialized with the initialization of a new ADNI project.
merge_csv.py is using VISCODE (not VISCODE2). This i fine as loong as the datasets merged will be done only for one ADNI phase (e.g ADNI1)