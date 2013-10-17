# MIDAS: Field guide to the microbes of activated sludge

## This is a short version of the full information found at http://midasfieldguide.org

The publically available databases are an invaluable resource for the scientific 
community. However, the curation of a taxonomy over all Bacteria and Archaea is a 
collosal undertaking we found that many new names were missing from the taxonomy 
and many of the clades of importance in activated sludge were poorly classified.

The ambition of the MIDAS database is to deliver the best and most updated taxonomy 
of organisms found in activated sludge ecosystem. The taxonomy strings used are derived
from and compatible with the widely-used [Greengenes](http://greengenes.lbl.gov/) 
database but is curated mostly at the lower taxonomic levels to improve classification 
at family and genus level. 

## Use

**The stable releases of the database can be downloaded from the [release page](https://github.com/aaronsaunders/midas/releases).**

Initially, the MIDAS taxonomy supports a taxfile for the [RDP classifier](http://sourceforge.net/projects/rdp-classifier/)
which we use in the [Qiime](http://qiime.org/) pipeline.

Simply use `midas_taxonomy.txt` found in the [tax folder](https://github.com/aaronsaunders/midas/archive/master.zip) as the taxonomy file for running the RDP classifier in place of the standard taxfile
in conjuction with the `gg_97_otus_4feb2011.fasta` refseq file from [Greengenes Feb 2011 release](http://greengenes.lbl.gov/Download/Sequence_Data/Fasta_data_files/Caporaso_Reference_OTUs/gg_otus_4feb2011.tgz)
.

## Source

The original database came from the Greengenes [Feb 2011 release](http://greengenes.lbl.gov/Download/Sequence_Data/Fasta_data_files/Caporaso_Reference_OTUs/gg_otus_4feb2011.tgz)

A 16S rRNA gene library was made using V1-V3 primers and sequenced with 454 FLX the 
400 bp products analysed with [Qiime](qiime.org) and the the PyNAST aligned 97% OTU 
representative sequences imported into the [ARB](http://www.arb-home.de) database. 
The sequences were inserted into the reference tree using parsimony insertion.  The 
placement of the short reads was used as a guide for the manual curation of the 
taxonomy.

Details of the curations are in changelog.txt (in preparation...)

The curated taxonomy was exported from ARB using NDS export of the MSA_id (arb
"name" field) and taxonomy fields. The file was reformated to comply with the
formatting of the RDP classifier, using the [check_rdp_taxfile.py](https://github.com/aaronsaunders/midas/blob/master/scr/check_rdp_taxfile.py) script.

-----

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">MIDAS: field guide to the microbes of activated sludge</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.midasfieldguide.org" property="cc:attributionName" rel="cc:attributionURL">Aaron Saunders, Mads Albertsen, Per Nielsen</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="http://greengenes.secondgenome.com/" rel="dct:source">http://greengenes.secondgenome.com/</a>.
