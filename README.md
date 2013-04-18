# MIDAS: The microbial database of activated sludge

A database and taxonomy of microbes in activated sludge


The MIDAS taxonomy is a manual curation of the Greengenes database and taxonomy that focuses on accurate naming 
and utility for the activated sludge ecosystem.

The original database came from:

http://greengenes.lbl.gov/Download/Sequence_Data/Fasta_data_files/Caporaso_Reference_OTUs/gg_otus_4feb2011.tgz

A 16S rRNA gene library was made using V1-V3 primers and the 400 bp products
analysed with Qiime (qiime.org) and the the PyNAST aligned 97% OTU representative sequences
imported into the ARB database. The sequences were inserted into the reference
tree using parsimony insertion.  The placement of the short reads was used as
a guide for the manual curation of the taxonomy. 

The curated taxonomy was exported from ARB using NDS export of the MSA_id (arb
"name" field) and taxonomy fields. The file was reformated to comply with the
formatting of the RDP classifier, using the check_rdp_taxfile.py script.

Details of the curations are in changelog.txt

