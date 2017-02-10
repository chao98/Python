import os
import json
import pprint
import matplotlib.pylab as plt
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
# https://github.com/wesm/pydata-book

pp = pprint.PrettyPrinter(indent=2)


def get_count(sequence):
    counts = defaultdict(int)
    for elem in sequence:
        counts[elem] += 1
    return counts


def analysis1(records):
    print('\nHard way analysis >>')
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print(time_zones[:10])

    counts = get_count(time_zones)
    pp.pprint(counts)

    counts = Counter(time_zones)
    pp.pprint(counts.most_common(10))


def analysis2(records):
    print('\nPandas analysis >>')
    frame = DataFrame(records)
    # pp.pprint(frame)
    # tz_counts = frame['tz'].value_counts()
    # pp.pprint(tz_counts[:10])
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()
    print('\n>> Time zones')
    pp.pprint(tz_counts[:10])

    # plt.figure(figsize=(10, 4))
    # tz_counts[:10].plot(kind='barh', rot=0)
    # plt.show()

    clean_url = frame.a.fillna('Missing')
    clean_url[clean_url == ''] = 'Unknown'
    urls = Series([x.split()[0] for x in clean_url])
    urls_counts = urls.value_counts()
    print('\n >> URLs')
    pp.pprint(urls_counts[:10])

    cframe = frame[frame.a.notnull()]
    operation_system = np.where(cframe.a.str.contains('Windows'),
                                'Windows', 'Not Windows')
    print('\n>> OS')
    # print(operation_system[:5])
    by_tz_os = cframe.groupby(['tz', operation_system])
    agg_counts = by_tz_os.size().unstack().fillna(0)
    indexer = agg_counts.sum(1).argsort()
    count_subset = agg_counts.take(indexer)[-10:]
    pp.pprint(count_subset)

    plt.figure(figsize=(10, 4))
    count_subset.plot(kind='barh', rot=0, stacked=True)
    plt.show()


def main(n):
    datafile = r'usagov_bitly_data2012-03-16-1331923249.txt'
    dir = r'data'
    path = os.path.join(dir, datafile)
    records = [json.loads(line) for line in open(path)]
    # pp.pprint(records[0])

    if n == 1:
        analysis1(records)
    elif n == 2:
        analysis2(records)

if __name__ == '__main__':
    main(2)
