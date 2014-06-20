#!/usr/bin/python

import re, sys
import argparse
__author__ = 'aaron.marc.saunders@gmail.com'



def check_taxfile_line(line, accs, includespecies):
    line = line.strip()
    
    acc = 'missing'
    if line.count('\t') > 1:
        return ('too many columns', acc, accs, line)
    if line.count('\t') == 0:
        return ('Missing accession or taxstring?', acc, accs, line)

    acc = get_acc(line)
    if not acc:
        return 'no id', accs, line
    if acc:
        if acc in accs:
            return ('duplicate id removed', acc, accs, line)
        else:
            accs.append(acc)

    newline = fix_taxstring(line, includespecies)

    result  = check_taxstring(newline, includespecies)

    return (result, acc, accs, newline)


def get_acc(line):
    exp = '^[\w\.]+'
    acc_mobj = re.match(exp, line)
    if not acc_mobj:
        return
    acc = str(acc_mobj.group())

    return acc

def check_taxstring(line, includespecies):
    result = 'good'

    columns = line.split('\t')
    if len(columns) != 2:
        return 'error with number of columns'
    taxstring = columns[1]

    # must contain 6 tax levels
    taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    # levels must be in order and correct
    taxprefixes = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__'  ]
    
    if not includespecies:
        taxprefixes = taxprefixes[:6]

    for level, taxname in enumerate(taxstrings):
        if taxname[:3] != taxprefixes[level]:
            result = 'wrong order of taxlevels'

    return result


def fix_taxstring(line, includespecies):
    """
    takes a taxstring and truncates it at 6 or 7 levels and
    replaces missing data with placeholders (eg. 'p__')
    """
    acc, taxstring = line.split('\t')

    # replaces ARB NDS export "/" with ";"
    taxstring = taxstring.replace('/', ';')

    # must have 6 levels
    if includespecies:
        taxstring = taxstring + ';' * (6 - taxstring.count(';'))
    else:
        taxstring = taxstring + ';' * (5 - taxstring.count(';'))
    
    # truncates tax levels at 6
    if includespecies:
        taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:7] ]
    else:  
        taxstrings = [ taxname.strip() for taxname in taxstring.split(';')[:6] ]

    taxprefixes   = [ 'k__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__' ]
    shortprefixes = [ 'k_',  'p_' , 'c_',  'o_',  'f_',  'g_', 's_' ]
    silvaprefixes = [ '__k',  '__p' , '__c',  '__o',  '__f',  '__g', '__s' ]

    if not includespecies:
        taxprefixes   = taxprefixes[:6]
        shortprefixes = shortprefixes[:6]
        silvaprefixes = silvaprefixes[:6]

    for level, taxname in enumerate(taxstrings):
        # empty levels are filled with the taxlevel placeholder
        # checks that all taxlevel prefixes have 2 underscores
        if taxname[:3] != taxprefixes[level]:
            # remove silva prefix
            if taxname.startswith(silvaprefixes[level]):
                taxname = taxname[3:]
            if taxname.startswith('__'):
                taxname = taxname[2:]
            if taxname.startswith('_'):
                taxname = taxname[1:]
            # remove if prefixes in wrong order
            if taxname[:3] in taxprefixes:
                taxname = taxname[3:]
            # remove if prefixes lack a "_"
            if taxname[:2] == shortprefixes[level]:
                taxname = taxname[2:]
            # add the right prefix
            taxstrings[level] = taxprefixes[level] + taxname
        if taxname[3:] == "uncultured":
            taxname = taxname[:3]
    
    newline =  '{0}\t{1}\n'.format( acc, ';'.join(taxstrings) )

    return newline

def main():
    parser = argparse.ArgumentParser(description = """checks and corrects a text file formatted for RDP classifier.
        Writes a corrected file to outfile and details to logfile.
        - accepts only 6 levels with prefixes: k__, p__, c__, o__, f__, g__.
        - unless the --includespecies flag is added
        - other levels are removed
        - greengenes prefixes are added if not present
        - dupicate ids are removed (first retained)""")
    parser.add_argument('-i','--input', 
                            help='Input taxonomy filename', required=True)
    parser.add_argument('-o','--output',
                        help='Cleaned taxonomy filename', required=True)
    parser.add_argument('-l','--log',
                        help='Log filename. The default is stdout')
    parser.add_argument('-s', '--includespecies', default= False,
                        help='include species.', action='store_true')
    args = parser.parse_args()

    taxfile = open(args.input, 'r')
    outfile = open(args.output, 'w')
    if args.log and args.log != '-':
        sys.stdout = open(args.log, 'w')
    print __doc__
    
    uncorrected = 0
    corrected   = 0
    accs        = []   # collects accs to ceck for dups
    print 'acc\tresult\tline in\tline out' #logfile header

    for n, line in enumerate(taxfile.readlines()):
        line = line.rstrip('\n')
        if line.startswith("#"):
            print line
            continue

        (result, acc, accs, newline) = check_taxfile_line(line, accs, args.includespecies)
        
        if result != 'good':
            print '{0}\tuncorrected: {1}\t{2}\tNA'.format(
            	acc, result, line.split('\t')[-1] )
            uncorrected += 1
        if result == 'good' and line != newline.strip():
            print '{0}\tcorrected\t{1}\t{2}'.format(
            	acc, line.split('\t')[1], newline.strip().split('\t')[-1] )
            corrected += 1

        outfile.write(newline)

    print
    print "{0} corrected errors".format(corrected)
    print "{0} uncorrected errors".format(uncorrected)

    outfile.close()
    taxfile.close()

if __name__ == '__main__':
    main()
