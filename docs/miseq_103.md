---
layout: default
title: miseq_103
---
# MiSeq 16S Amplicon Sequencing
Version 1.03 - [download as pdf](link)

## Introduction
This protocol has been optimized to sequence V1-3 16S amplicon libraries. The protocol is designed to sequence 2x301 + 8 bp (index) by using hacked MiSeq Reagent kit v2 (500 cycles).

## Input Sample Libraries
Input sample libraries should have a concentration of > 4 nM

## Preparation of MiSeq Instrument and Reagents

### 1. Instrument Washing
* If the instrument has been put in standby mode a maintenance wash is required before  sequencing can commence. Washing takes around 60 min.
* Press ‘Sequencing’ on the welcome screen. If washing is required the machine will let you know. NB: For detailed help press the question mark and an illustrated tutorial will start.
* When washing is complete leave the MiSeq idle until you are ready to load the reagents.

### 2. Thaw reagents
* Thaw HT1 buffer at room T and place reagent cartridge in water bath at room T for an hour. After thawing place at 4C until use.
* Invert reagent cartridge 10 times.
* Visually inspect position 1 well for precipitates.
* Gently tap cartridge on table top to reduce amount of bubbles.
* Thaw sequencing primers (read 1, read 2 and index), 2N NaOH and PhiX control library at room T and then place on ice.

### 3. Prepare Sample Sheet
* Open the MiSeq sample sheet template in Notepad++ (NOT in excel!!!).
* Only change sample specific info under `Data`.
* Important fields to change according to samples: “Sample_Name” and “index”.
* Check Sample Sheet compatibility by loading it into the Illumina ‘Experimental Manager’ (installed on the MiSeq). If the sheet can be loaded it is compatible with the MiSeq.

## Prepare Sequencing Library
### 1. Multiplex sample libraries 
* Pool libraries so final library contains equimolar concentrations of all libraries.
* Measure DNA concentration of Pooled amplicon library with Quibit DNA HS assay, convert ng/uL to nM (see calculation example at the end of the protocol) and dilute to a final concentration of 4 nM with DNA H2O. NB: We haven’t had good experience with using tapestation.

### 2. Dilute PhiX control library (10 nM) to 4 nM
* Take 2 uL Phix Control library and 3 uL DNA H2O.

### 3. Store on ice. Before use adjust to ambient temperature

### 4. Prepare 0.2 N NaOH solution
* 225 ul DNA H2O and 25 ul 2.0 N NaOH (use Illumina NaOH).

### 5. Denature multiplexed amplicon library (4 nM) and a PhiX control library (4 nM) separately 
* NB: Denatured Phix control libraries can be reused for up to 3 weeks. So only prepare a new Phix Library if the old one has expired. Phix Control library is expensive.
* Mix 5 μL library + 5 uL 0.2 N NaOH. Final concentration is 2 nM
* Pipette up and down 10 times
* Incubate for 5 min at room temperature.

### 6. Dilute multiplexed amplicon library (2 nM) to 15 pM and PhiX control library (2 nM) to 12 pM
* Mix 10 uL denatured library with 990 Pre-chilled HT1. Concentration is 20 pM.
* Mix 450 uL multiplexed amplicon library (20 pM) with 150 uL Pre-chilled HT1 buffer. Concentration is 15 pM.
* Mix 360 uL PhiX control library (20 pM) with 240 uL Pre-chilled HT1. Final concentration is 12 pM

### 7. Mix PhiX library (12 pM) with multiplexed amplicon library (15 pM) in a 10% to 90% ratio
* Mix 60 ul PhiX library with 540 ul multiplexed amplicon library.
* Place the library on ice until use.
* NB: with these concentrations we usually get a cluster density in the range 800-900 K/mm2.

## Load sample and primers on reagent cartridge
### 1. Adding custom primers to reagent cartridge
* Pierce well 13 and transfer 100 ul of primer solution to a tube. Add 3.4 ul index sequencing primer (100 uM) to the solution in the tube, and transfer it all back into the well and mix with well content by pipetting slowly up and down.
* Pierce well 12 and transfer 100 ul of primer solution to a tube. Add 3.4 ul Read 1 sequencing primer (100 uM) to the solution in the tube, and transfer it all back into the well and mix with well content by pipetting slowly up and down.
* Pierce well 14 and transfer 100 ul of primer solution to a tube. Add 3.4 ul Read 2 sequencing primer (100 uM) to the solution in the tube, and transfer it all back into the well and mix with well content by pipetting slowly up and down.

### 2. Adding sample to reagent cartridge
* Pierce sample chamber with a tip.
* Add 600 ul mixed PhiX/pooled amplicon library.

### 3. Add extra reagent to cartridge
* Pierce well 1 and add 5 mL solution from well 1 of a spare reagent cartridge (incorporation buffer).
* Pierce well 2 and add 7 mL solution from well 2 of a spare reagent cartridge (scan mix).
* Pierce well 4 and add 6.8 mL solution from well 4 of a spare reagent cartridge (cleavage mix).
* Open Incorporation buffer bottle and add 80 mL incorporation buffer from a spare incorporation buffer bottle.

## Start sequencing run
### 1. Follow instructions in MiSeq manual for preparing/loading the flow cell, loading the reagents, referring to the sample sheet and starting the sequencing run.
### 2. When the MiSeq warns not to run 610 cycles, do it any way.

## Example of converting ng/uL to nM
* Average length of V1-3 library amplicon: 615 bp
* Average molecule weight of nucleotide: 607g/(mol x bp) x # nt + 158 g/mol


## Literature
* Caporaso, J. G., Lauber, C. L., Walters, W. A., Berg-Lyons, D., Lozupone, C. A., Turnbaugh, P. J., et. al., (2011). Global patterns of 16S rRNA diversity at a depth of millions of sequences per sample. Proceedings of the National Academy of Sciences of the United States of America, 108 Suppl , 4516–22. doi:10.1073/pnas.1000080107
* Caporaso, J. G., Lauber, C. L., Walters, W. a, Berg-Lyons, D., Huntley, J., Fierer, N., et. al., (2012). Ultra-high-throughput microbial community analysis on the Illumina HiSeq and MiSeq platforms. The ISME journal, 6(8), 1621–4. doi:10.1038/ismej.2012.8

## Revision History
### V1.01 2013-3-19
* Protocol created based on numerous journals, the ‘MiSeq System User Guide - Part # 15027617 Rev. D July 2012’, Caporaso, J.G. et al., 2010. Global patterns of 16S rRNA diversity at a depth of millions of sequences per sample. and Caporaso, J.G. et. al., 2012. Ultra-high-throughput microbial community analysis on the Illumina HiSeq and MiSeq platforms. The ISME journal, 6(8), pp.1621–1624.

### V1.02 2013-4-15
* Minor additions and elaborations.

### V1.03 2013-8-21
* Changed input concentration from 10 nM to 4 nM and revamped the dilution scheme to be in line with the Illumina guidelines in Part # 15039740 Rev. B
* Included reference to example sample sheet
* Added hack to increase number of possible cycles from 500 to 610
* Added example of converting ng/uL to nM
