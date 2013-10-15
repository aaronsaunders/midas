#!/usr/bin/env python
 
"""
Copyright (C) 2013 Aaron Saunders
aaron.marc.saunders@gmail.com

functions to reformat the RDP classifer taxfile and refseqs for mothur.

Not complete!!
 
"""
 
import os
import sys
import argparse
import subprocess
from Bio import SeqIO
import re


def reformatTaxfile(taxfname):
    ```must have a ";" at the end of the line
        6 levels not required as with RDP Classifier
    empty categories should be removed
    GOOD
    234  Bacteria;Proteobacteria;
    BAD!
    234  Bacteria;Proteobacteria;;;;;
    ```
    taxprefixes = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    taxfh = open(taxfname, 'r')
    taxfile = taxfh.read()
    
    # run this three times
    taxfile = re.sub(r';;', r';', s)
    
    taxfile = re.sub(r'$', r';', s)
    
    taxfh.close()
    
    return

def reformatFastaReference(fastafh, taxfh):
    tax_ids = [ line.split('\t')[0] for line in taxfh.readlines() ]
    print len(tax_ids)
    recs =  [ rec for rec in SeqIO.parse(fastafh, "fasta")
              if rec.id in tax_ids  ]
    with open(fastafh, 'w') as outfh:
        SeqIO.write(recs, outfh, 'fasta')
    
    
    return


