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
    if line.count('\t') > 1:
        return 'too many columns', accs, line

    acc = get_acc(line)
    if not acc:
        return 'no id', accs, line
    if acc:
    	if acc in accs:
            return ('duplicate id #%s' % acc), accs, line
        else:
            accs.append(acc)

    newline = fix_taxstring(line)
    result = check_taxstring(newline)

    return (result, accs, newline)


def get_acc(line):
    exp = '^\d+'
    acc_mobj = re.match(exp, line)
    if not acc_mobj:
        return
    acc = acc_mobj.group()

    return acc

def check_taxstring(line):
    result = 'good'

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
    acc, taxstring = line.split('\t')

    # replaces ARB NDS export "/" with ";"
    taxstring = taxstring.replace('/', ';')

    # must have 6 levels
    taxstring = taxstring + ';' * (5 - taxstring.count(';'))

    # truncates tax levels at 6
    taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    taxprefixes = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__'  ]
    for level, taxname in zip(range(6), taxstrings):
        # empty levels are filled with the taxlevel placeholder
        # checks that all taxlevel prefixes have 2 underscores
        if taxname[:4] != taxprefixes[level]:
            taxstrings[level] = taxprefixes[level] + taxname[3:]

    newline =  '{0}\t{1}\n'.format( acc, ';'.join(taxstrings) )

    return newline

def main():
    filename = sys.argv[1]
    outfilename = sys.argv[2]

    with open(filename, 'r') as taxfile:
        lines = taxfile.readlines()

    errors = []
    corrected = []
    accs = []
    newlines = []
    for n, line in enumerate(lines):
        line = line.rstrip('\n')
        if line.startswith("#"):
            print line
            continue
        (result, accs, newline) = check_taxfile_line(line, accs)
        if result != 'good':
            errors.append( 'error in line {0}: {1} "{2}"'.format( n, result, newline[:-1] ) )
        else:
            if line != newline:
                corrected.append('corrected error in line {0}: "{1}" to "{2}"'.format( n, line, newline[:-1] ))
            newlines.append(newline)


    with open(outfilename, 'w') as outfile:
        outfile.writelines(newlines)

    print "finished with:"
    print "{0} corrected errors\n".format(len(corrected))
    for error in corrected:
        print error
    print
    print "{0} uncorrected errors\n".format(len(errors))
    for error in errors:
        print error

if __name__ == '__main__':
    main()
