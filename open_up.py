import os
from multiprocessing import Pool


processes = ('open_slack.py', 'open_webstorm.py', 'open_urls.py', 'open_github.py')


def run_process(process):
    os.system(f'python apps/{process}')


pool = Pool(processes=3)
pool.map(run_process, processes)




