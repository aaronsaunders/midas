#!/usr/bin/python

import sys

infilename = sys.argv[1]
includefilename = sys.argv[2]
outfilename = sys.argv[3]
newtaxfilename = sys.argv[4]

infile = open(infilename, 'r')
newtaxfile = open(newtaxfilename, 'w')
outfile = open(outfilename, 'w')

with open(includefile, 'r') as fh:
    reps = {}
    for line in fh.readlines():
        otu, taxstring = line.strip().split('\t')
        reps[otu] = taxstring

for line in infile:
    line = line.strip()
    otu, taxstring = line.split('\t')
    # only adds taxstrings for current 
    if otu not in reps:
        continue
    # remove taxa without a taxstring
    if taxstring.startswith("Species"):
        continue
    # fix taxstring to be 6 levels
    taxlevels = taxstring.split(';')[:5]
    length = len(taxlevels)
    if length == 1:
	taxlevels.append('p__')
    if length <= 2:
	taxlevels.append('c__')
    if length <= 3:
	taxlevels.append('o__')
    if length <= 4:
	taxlevels.append('f__')
    if length <= 5:
	taxlevels.append('g__')

    taxstring = ';'.join(taxlevels)
    old_taxstring = reps[otu]
    if taxstring != old_taxstring:
        line = '{0}\t{1}\t{2}\n'.format(otu, taxstring, old_taxstring )
        outfile.write(line)
    # write to file
    rec = '{0}\t{1}\n'.format(otu, taxstring)
    newtaxfile.write(rec)

outfile.close()
newtaxfile.close()
infile.close()


