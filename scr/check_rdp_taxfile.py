#!/usr/bin/python

import re, sys


def check_taxfile_line(line, accs):

    acc = get_acc(line)
    if not acc:
        return ('no id'), accs
    if acc:
    	if acc in accs:
            return ('duplicate id #%s' % acc), accs
        else:
            accs.append(acc) 
    newline = fix_taxstring(line)
    result = check_taxstring(newline)

    return result, accs, newline


def get_acc(line):
    exp = '^\d+'
    acc_mobj = re.match(exp, line)
    if not acc_mobj:
        return 
    acc = acc_mobj.group()

    return acc

def check_taxstring(line):
    result = None
    
    columns = line.split('\t')
    if len(columns) != 2:
        return 'error with number of columns'
    taxstring = columns[1]
    # must contain 6 tax levels
    taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    # levels must be in order and correct
    taxlevels = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    for level, taxname in enumerate(taxstrings):
        if taxname[:3] != taxlevels[level]:
            result = 'wrong order of taxlevels'

    return result

def fix_taxstring(line):
    """
    takes a taxstring and truncates it at 6 levels and 
    replaces missing data with placeholders (eg. 'p__')
    """
    columns = line.split('\t')
    if len(columns) != 2:
        return None
    acc = columns[0]
    taxstring = columns[1]
    taxstring = taxstring.replace('/', ';')
    # must contain 6 tax levels
    taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    taxlevels = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    for level, taxname in enumerate(taxstrings):
        if taxname is '':
            taxstrings[level] = taxlevels[level]

    length = len(taxstrings)
    if length == 1:
	taxstrings.append('p__')
    if length <= 2:
	taxstrings.append('c__')
    if length <= 3:
	taxstrings.append('o__')
    if length <= 4:
	taxstrings.append('f__')
    if length <= 5:
	taxstrings.append('g__')

    for taxlevel in taxlevels:
       if taxlevel[1:2] == '_':
            if taxlevel[2:3] != '_':
                taxlevel = taxlevel[:2] + '_' + taxlevel[3:]
                
    newline =  '{0}\t{1}'.format( acc, ';'.join(taxlevels) )
    
    return newline

def main():
    filename = sys.argv[1]
    outfilename = sys.argv[2]
    
    with open(filename, 'r') as taxfile:
        lines = taxfile.readlines()

    accs = []
    newlines = []
    for n, line in enumerate(lines):
        line = line.rstrip('\n')
        result, accs, newline = check_taxfile_line(line, accs)
        if result:
            print 'line {0}: {1}: {2}'.format( n, result, newline )
        else:
            newlines.append(newline)


    with open(outfilename, 'w') as outfile:
        outfile.writelines(newlines)
    

if __name__ == '__main__':
    # 1. must have 6 levels
    # 2. each rank must have a name
    # 3. Check Capitalisation
    # 4. check that each rank is only used once
    # 5. check the order of ranks
    #error1 = r'123\tk__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae'
    #error2 = r'123\tk__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;'
    #error3 = r'123\tk__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__comamonadaceae;g__'
    #error4 = r'123\tk__Bacteria;p__Proteobacteria;k__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;g__'
    #error5 = r'123\tk__Bacteria;c__Proteobacteria;p__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;g__,'
    #error6 = r'123\tk__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;g__'
    #error7 = r'k__Bacteria;p__Proteobacteria;c__Betaproteobacteria;o__Burkholderiales;f__Comamonadaceae;g__'
    #tests = [ error1, error2, error3, error4, error5, error6, error7 ]
    #accs = []
    #for n, test in enumerate(tests):
    #    result = check_taxfile_line(test, accs)
    #    if result:
    #        print 'error{0}: {1}: {2}'.format( n, result, test )

    main()
