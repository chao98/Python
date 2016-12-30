#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import timezone


def main(n):
    time_a = 2016, 12, 29, 14, 10
    time_b = 2015, 12, 29, 13, 10

    if n == 1:
        # 取得当前时间的 datetime的实例
        now = datetime.now()
        print('now is: ', now)

    if n == 2:
        # 从tuple产生datetime的实例
        # 并生成timestamp
        dt = datetime(*time_a)
        print('time: ', dt)
        print('timestamp: ', dt.timestamp())

    if n == 3:
        # 从timestamp产生datetime
        # 从timestamp产生 utc datetime
        dt = datetime(*time_a)
        ts = dt.timestamp()
        print('time: ', dt)
        print('from ts to time: ', datetime.fromtimestamp(ts))
        print('utc time: ', datetime.utcfromtimestamp(ts))

    if n == 4:
        # 从 str 产生 datetime。注意，要先给出时间格式
        time_4 = '2016-12-29 ** 14:10:00'
        time_f_4 = '%Y-%m-%d ** %H:%M:%S'
        dt = datetime.strptime(time_4, time_f_4)
        print(dt)
        print(dt.timestamp())

    if n == 5:
        # 输出指定格式的时间 str
        time_f_5 = '%Y-%m-%d %H:%M:%S'
        dt = datetime(*time_a)
        print(dt.strftime(time_f_5))

    if n == 6:
        # datetime的加减
        dt = datetime(*time_a)
        dt_a = dt + timedelta(hours=4)
        print(dt, ', ', dt_a)
        dt_b = dt + timedelta(days=1)
        print(dt, ', ', dt_b)
        delta = dt_b - dt
        print(type(delta))
        dt_c = datetime(*time_b)
        print(dt_c - dt)

    if n == 9:
        # 本地时间和utc时间的转换，用datetime来运算
        dt = datetime(*time_a)
        print('local: ', dt)
        ts = dt.timestamp()
        print('utc: ', datetime.utcfromtimestamp(ts))
        tz_utc_8 = timezone(timedelta(hours=9))
        dt_a = dt.replace(tzinfo=tz_utc_8)
        print('local: ', dt_a)
        ts_a = dt_a.timestamp()
        print('utc: ', datetime.utcfromtimestamp(ts_a))

    if n == 10:
        # 用utc时间转换成其它时区的时间
        utc_dt = datetime.utcnow()
        print('orig utc: ', utc_dt)
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
        print('force utc: ', utc_dt)
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
        print('bj time: ', bj_dt)
        jp_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
        print('jp time: ', jp_dt)
        jp_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
        print('from bj to jp: ', jp_dt2)

if __name__ == '__main__':
    main(10)
