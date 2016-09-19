import sys
import time


def countdown(from_time):
    for i in xrange(from_time, 0, -1):
        m, s = divmod(i, 60)
        sys.stdout.write('\r' + str(int(m)) + ':' + str(int(s)))
        time.sleep(1)
        sys.stdout.flush()

    sys.stdout.write('\r' + '')
