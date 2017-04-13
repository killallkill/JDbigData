import time
import datetime

from astropy.version import timestamp


def main():
    s = "2013-01-03 23:34"
    t = time.strptime(s, "%Y-%m-%d %H:%M")
    y, m, d, h, M = t[:5]
    print t

if __name__ == '__main__':
    main()