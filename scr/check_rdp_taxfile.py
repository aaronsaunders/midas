#!/usr/bin/python

import re, sys

"""
check_rdp_taxfile.py taxfilename outfilename

takes a text file that ostensibly formatted for RDP classifier
writes a corrected file to outfile

Reformats the output of ARB NDS export (name, taxonomy) for RDP classifier

- accepts only 6 levels with prefixes: k__, p__, c__, o__, f__, g__
- other levels are removed

"""

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
    taxprefixes = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    for level, taxname in enumerate(taxstrings):
        if taxname[:3] != taxprefixes[level]:
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

    # replaces ARB NDS export "/" with ";"
    taxstring = taxstring.replace('/', ';')

    # truncates tax levels at 6
    taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    taxprefixes = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    for level, taxname in enumerate(taxstrings):
        # empty levels are filled with the taxlevel placeholder
        if taxname is '':
            taxstrings[level] = taxprefixes[level]
        # checks that all taxlevel prefixes have 2 underscores
        if taxname[:4] != taxprefixes[level]
            taxname[:4] = taxprefixes[level]

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

    newline =  '{0}\t{1}'.format( acc, ';'.join(taxlevels) )

    return newline

def main():
    filename = sys.argv[1]
    outfilename = sys.argv[2]

    with open(filename, 'r') as taxfile:
        lines = taxfile.readlines()

    error_counter = 0
    accs = []
    newlines = []
    for n, line in enumerate(lines):
        line = line.rstrip('\n')
        result, accs, newline = check_taxfile_line(line, accs)
        if result:
            print 'error: {0}: {1}: {2}'.format( n, result, newline )
            error_counter += 1
        else:
            newlines.append(newline)


    with open(outfilename, 'w') as outfile:
        outfile.writelines(newlines)

    print "finished with {0} errors".format(error_counter)

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
