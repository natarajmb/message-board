import sys
from glob import glob

workers = 1
loglevel = 'info'
reload = True
reload_extra_files = glob('board/**/*.html', recursive=True) + glob('board/**/*.css', recursive=True)
errorlog = '-'
accesslog = '-'


def worker_int(worker):
    print('Exit because of worker failure')
    sys.exit(1)
