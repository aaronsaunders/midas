---
layout: default
title: database
---
The publically available databases are an invaluable resource for the scientific community. However, the curation of a taxonomy over all Bacteria and Archaea is a collosal undertaking and we found that many new names were missing from the taxonomy and many of the clades of importance in activated sludge were poorly classified.

![MIDAS taxonomic assignment](../images/workflow.png)

The ambition of the MIDAS database is to deliver the best and most updated taxonomy of organisms found in activated sludge ecosystem. The taxonomy strings used are derived from and compatible with the widely-used Greengenes database but is curated mostly at the lower taxonomic levels to improve classification at family and genus level.

To use MIDAS for your taxonomic assignment simply clone or download the [midas database on github](https://github.com/aaronsaunders/midas/). Files are prepared for taxomomic assignment with the RDP classifier in [Qiime](http://qiime.org). With the [assign_taxonomy.py](http://qiime.org/scripts/assign_taxonomy.html) script, use `tax/midas_taxonomy.txt` as the taxonomy file (-t) and `repseqs/gg_97_otus_4feb2011.fasta` as the refences sequences (-r).
