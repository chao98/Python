from datetime import datetime
from collections import namedtuple

config = {'SOURCE': None,
          'Source sht': None,
          'TARGET': None,
          'Raw sht': None,
          'Trend sht': None,
          'Statistics sht': None,
          'Log sht': None}


trend_check_items = {'In': [0 for i in range(12)],
                     'Out': [0 for i in range(12)],
                     'Open': [0 for i in range(12)],
                     'BDC': [0 for i in range(12)],
                     'BMC': [0 for i in range(12)],
                     'Low': [0 for i in range(12)],
                     'Medium': [0 for i in range(12)],
                     'High': [0 for i in range(12)],
                     'Hot': [0 for i in range(12)],
                     'Emergency': [0 for i in range(12)],
                     'Consultation': [0 for i in range(12)],
                     'Internal': [0 for i in range(12)],
                     'Problem': [0 for i in range(12)],
                     'Project': [0 for i in range(12)],
                     'Total': [0 for i in range(12)]}

trend_required_analysis_row = {'In': 2,
                               'Out': 3,
                               'Open': 4,
                               'BDC': 5,
                               'BMC': 6,
                               'Low': 7,
                               'Medium': 8,
                               'High': 9,
                               'Hot': 10,
                               'Emergency': 11,
                               'Consultation': 12,
                               'Internal': 13,
                               'Problem': 14,
                               'Project': 15,
                               'Total': 16}
