""" Vowel Identity Support Vector Machine Classifier
Copyright (C) 2015  Alan Zaffetti

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details. """

import re

######################
## Global settings. ##
######################

_use_full_classes        = True
_use_full_data           = True
_f_use_class_toggle      = lambda simp,full:[simp,full][_use_full_classes]
_f_use_data_toggle       = lambda simp,full:[simp,full][_use_full_data]

####################################
## Vowel data schema information. ##
####################################

_full_class_labels       = ['ae','ah','aw','eh','ei','er','ih','iy','oa','oo','uh','uw']
_simp_class_labels       = ['ih','ae','oo']
_class_labels            = _f_use_class_toggle(_simp_class_labels, _full_class_labels)
_n_classes               = _f_use_class_toggle(len(_simp_class_labels), len(_full_class_labels))
_all_data                = {v:[] for v in _class_labels}
_n_samples               = 0

#####################################
## Vector data schema information. ##
#####################################

_full_labels             = ('duration', 'f0', 'F1', 'F2', 'F3', 'F4',
                                              'F110', 'F210', 'F310',
                                              'F120', 'F220', 'F320',
                                              'F130', 'F230', 'F330',
                                              'F140', 'F240', 'F340',
                                              'F150', 'F250', 'F350',
                                              'F160', 'F260', 'F360',
                                              'F170', 'F270', 'F370',
                                              'F180', 'F280', 'F380')
_simp_labels             = ('duration', 'f0', 'F1', 'F2', 'F3', 'F4',
                                              'F120', 'F220', 'F320',
                                              'F150', 'F250', 'F350',
                                              'F180', 'F280', 'F380')
_labels                  = _f_use_data_toggle(_simp_labels, _full_labels)
_n_labels                = _f_use_class_toggle(len(_simp_labels), len(_full_labels))

###########################################
## Expressions for parsing data entries. ##
###########################################

_r_full_entry            = re.compile(r'^[bgmw]\d+(..)\s+((?:\d+\s+){28})(\d+\s+?)$')
_r_simp_entry            = re.compile(r'^[bgmw]\d+(..)\s+((?:\d+\s+){14})(\d+\s+?)$')
_r_entry                 = _f_use_data_toggle(_r_simp_entry, _r_full_entry)

#########################################
## Initialize the data file handle.    ##
## And construct an enumerator object. ##
#########################################

_data_path               = '../data/'
_full_data_file          = _data_path + 'bigdata.dat'
_simp_data_file          = _data_path + 'vowdata.dat'
_data_file               = _f_use_data_toggle(_simp_data_file, _full_data_file)
_file_handle             = open(_data_file, 'r')
_line_enumerator         = enumerate(_file_handle)

#######################################
## Data entries are line-delineated. ##
## Enumerate and parse legal lines.  ##
## Populate the _all_data structure. ##
#######################################

for i, line in _line_enumerator:

	## Parse the line against the expression.
	entry = re.match(_r_entry, line)
	
	## Check if the line is a valid data entry.
	if entry:
		groups                  = entry.groups()
		entry_class             = groups[0]
		entry_data              = tuple( map(int, groups[1].split()) + [int(groups[2])] )
		
		## Test if this entry is relevant, given our classes.
		## If the entry is relevant, append it to the dataset.
		if entry_class in _all_data:
			_all_data[entry_class].append( entry_data )
			_n_samples += 1