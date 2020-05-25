#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from kavalkilu.tools import Paths, Log
from kavalkilu.tools.databases import CSVHelper

p = Paths()
logg = Log('obd_compacter', 'obd_compacter', log_lvl="DEBUG")
logg.debug('Log initiated')

csvhelp = CSVHelper()

# Set path to compact csv files to
compact_path = os.path.join(p.data_dir, 'obd_results_main.csv')
file_glob = os.path.join(p.data_dir, 'obd_results_201*.csv')

# Compact the csv files
csvhelp.csv_compacter(compact_path, file_glob, sort_column='TIMESTAMP')

logg.debug('File compaction completed.')

logg.close()
