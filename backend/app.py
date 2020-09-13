from date_formatter import DateFormatter
from mars_api import MarsPhoto
import requests
import os
import pyfiglet


earth_dates = {'02/27/17': '%m/%d/%y', 
    'June 2, 2018': '%B %d, %Y',
    'Jul-13-2016': '%b-%d-%Y',
    'April 31, 2018': '%B %d, %Y'}

DEFAULT_API_KEY = 'nQrON5s7zDYObo9x7xaM1UX5hKBstlGdD5g3AdHX'

def main():
    for earth_date, earth_date_format in earth_dates.items():
        temp_date = DateFormatter(earth_date, earth_date_format)
        e_date = temp_date._date()
        if not e_date == 'Error':
            mars_image = MarsPhoto(e_date, DEFAULT_API_KEY)
            #print(mars_image._get())
            #print(mars_image._download())
        else:
            print(f'The "{e_date}" is invalid date value. Please verify')

def _banner():
    program_banner = pyfiglet.figlet_format("WELCOME TO MARS ROVER API!")
    print(program_banner)
    print("This simple program will let you download exclusive NASA photos in mars dated : ")
    for earth_date, earth_url in earth_dates.items():
        print(f'>  {earth_date}')

if __name__ == '__main__':
    _banner()
    user_action = input("If you wish to download the image now, please enter 'yes' :")
    if user_action == "yes":
        main()
