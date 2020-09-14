import os
import requests
from manager.mars_api import MarsPhoto
import pyfiglet
from utils.settings import DEFAULT_API_KEY, earth_dates
from utils.date_formatter import DateFormatter
from utils.logger import logger


def main():
    for earth_date, earth_date_format in earth_dates.items():
        temp_date = DateFormatter(earth_date, earth_date_format)
        e_date = temp_date._date()
        if not e_date == 'Error':
            mars_image = MarsPhoto(e_date, DEFAULT_API_KEY)
            mars_image._get()
            mars_image._download()
        else:
            logger.warning(f'The "{e_date}" is invalid date value. Please verify')

def _banner():
    program_banner = pyfiglet.figlet_format("WELCOME TO MARS ROVER API!")
    logger.info(program_banner)
    logger.info("This simple program will let you download exclusive NASA photos in mars dated : ")
    for earth_date, earth_url in earth_dates.items():
        logger.info(f'>  {earth_date}')
    logger.info("Now downloading please wait. . . .")

if __name__ == '__main__':
    _banner()
    main()
