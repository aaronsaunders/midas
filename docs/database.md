---
layout: default
title: database
---
The publically available databases are an invaluable resource for the scientific community. However, the curation of a taxonomy over all Bacteria and Archaea is a collosal undertaking and we found that many new names were missing from the taxonomy and many of the clades of importance in activated sludge were poorly classified.

![MIDAS taxonomic assignment](../images/workflow.png)

The ambition of the MIDAS database is to deliver the best and most updated taxonomy of organisms found in activated sludge ecosystem. The taxonomy strings used are derived from and compatible with the widely-used Greengenes database but is curated mostly at the lower taxonomic levels to improve classification at family and genus level.

The taxonomy supports a taxfile for the RDP classifier which we use in the Qiime pipeline.

Simply use `midas_taxonomy.txt` as the taxonomy file for running the RDP classifier in conjuction with the `gg_97_otus_4feb2011.fasta` in place of the standard taxfile.