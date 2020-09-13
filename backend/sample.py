import progressbar
from utils.logger import logger
from time import sleep

def display_progress(start_msg, ending_msg):
    bar = progressbar.ProgressBar(maxval=20, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    logger.info(str(start_msg))
    bar.start()
    for i in range(20):
        bar.update(i+1)
        sleep(0.1)
    bar.finish()
    logger.info(ending_msg)