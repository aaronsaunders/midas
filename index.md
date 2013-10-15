---
layout: default
title: index
---
MIDAS is a central resource for information about the microbes in the engineered ecosystem of activated sludge and similar wastewater treatment systems, such as biofilms, granules and membrane-bioreactors. There are over 50 genera of organisms typically abundant (> 0.5%) in the community and a majority of these do not have closely-related cultured relatives. 

Nomenclature in the anarchy outside of the mainstream systematic bacteriological naming has led to considerable confusion; here we propose a provisional naming scheme for the genera in community that can be used as a reference point for linking the most updated naming (taxonomy) and sequence data with functional information about the _in situ_ metabolism of microbes in this habitat.

The data is manually curated by a small team of experts so we [invite contribution](docs/about.html) if you find en error or have something that you think should be in the database.
![MIDAS usecases](images/usecases.png)
## General use cases

#### Genus/species X has been identified in my plant
- Are they typical (core) organisms in activated sludge?
- What function do they typically perform?
- Are these organisms occassional (transient) organisms that may be problematic for plant operation?

#### I have filaments of morphology, eg. Eikelboom type 0092
- Which taxonomic groups are these organisms likely to come from?

#### I am interested in a function in activated sludge
- Which microbes are typically associated with this process?
- How many organisms have been tested for this function?

#### I have a sequence library derived from activated sludge
- Which organisms are present? 
- How can I compare these names to those from other studies?

## Linking taxonomy and function
The *in situ* physiology of many organisms in the activated sludge ecosystem is extensively characterised, in part due to its amenability to *in situ* methods, such as microautoradiography (MAR) and stable-isotope probing (SIP). The ambition of the MiDAS field guide is to summarise all the knowledge about the distribution, ecology and diversity, and metabolism of the important organisms in the ecosystem. 

The [MIDAS name-function table](https://docs.google.com/spreadsheet/ccc?key=0AibK9cdlSmXgdDN5NTRnVkVZUTNfOS1KYVIzWXNZb2c&usp=sharing) begins this task. 

The information will be expanded in the coming months to include detailed *in situ* substrate specificity profiles, and putative capabilites from genomic data.


## Using MiDAS for sequence classification (taxonomic assignment)
The publically available databases are an invaluable resource for the scientific community. However, the curation of a taxonomy over all Bacteria and Archaea is a collosal undertaking and we found that many new names were missing from the taxonomy and many of the clades of importance in activated sludge were poorly classified.

![MIDAS taxonomic assignment](images/workflow.png)

The ambition of the MIDAS database is to deliver the best and most updated taxonomy of organisms found in activated sludge ecosystem. The taxonomy strings used are derived from and compatible with the widely-used Greengenes database but is curated mostly at the lower taxonomic levels to improve classification at family and genus level.



Simply clone or download the [midas database on github](https://github.com/aaronsaunders/midas/releases/). Files are prepared for taxomomic assignment with the RDP classifier in [Qiime](http://qiime.org). With the [assign_taxonomy.py](http://qiime.org/scripts/assign_taxonomy.html) script, use `tax/midas_taxonomy.txt` as the taxonomy file (-t) and `repseqs/gg_97_otus_4feb2011.fasta` as the refences sequences (-r).
