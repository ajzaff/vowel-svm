Vowel Identity Support Vector Machine Classifier
Copyright (C) 2015  Alan Zaffetti

ATTRIBUTIONS

	Thanks to the following:
	
	- James Hillenbrand (vowel data) <homepages.wmich.edu/~hillenbr/voweldata/>
	- NLTK Team <nltk.org/>
	- scikit-learn Team <scikit-learn.org/>
	- numPy Team <numpy.org/>
	- matplotlib Team <matplotlib.org/>
	- PIP Team <pip.pypa.io/>
	
CONTENTS

	+ data/               [DIR] vowel data and importing tools.
	|-- vowdata.dat       the Hillenbrand vowel data.
	+ figures/            [DIR] figures (.png).
	+ src/                [DIR] contains classifier code, scripts, and misc. sources.
	|-- svc.py            trains an SVC model.
	|-- data.py           vowel data and schema.
	install.sh            installs python libraries.
	uninstall.sh          uninstalls python libraries.
	LICENSE.txt           GNU GPLv2 text.
	README.txt            this document.

INSTALLING LIBRARIES

	This project depends on a few python libraries.  I have enclosed a simple script for installing these.  The installer program relies on pip and setuptools to download packages.
	To run it, execute the following command (you may be asked for a password):
	
	chmod +x install.sh;./install.sh
	
UNINSTALLING LIBRARIES

	If you do not wish to keep one or more dependencies after installing, you may remove them with this command (you may be asked for a password):
	
	chmod +x uninstall.sh;./uninstall.sh
	
	** NOTE: You will be prompted before removal of each library.  Please mind these prompts!