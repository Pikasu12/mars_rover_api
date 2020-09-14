import requests
from utils import logger
import os

class MarsPhoto():
    def __init__(self, e_date, key):
        self.e_date = e_date
        self.key = key
        self.nasa_api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        self.api_parameters = {
            'earth_date': self.e_date, 
            'api_key': self.key
        }
        self.image_collections = []

    def _request_image(self):
        r = requests.get(self.nasa_api_url, params=self.api_parameters)
        details = r.json()
        return details

    def _get(self):
        logger.info(f'Gathering image details start dated {self.e_date} please wait. . . .')
        details = self._request_image()

        for detail in details['photos']:
            self.image_collections.append({str(f'{detail["id"]}_{detail["camera"]["full_name"]}'): detail["img_src"]})
            self._setup_directory(detail['earth_date'])
        logger.info(f'Gathering image details on {self.e_date}.')
        return ''

    def _download(self):
        logger.info(f'Downloading images on date: {self.e_date} starts please wait. . . .')
        for image_details in self.image_collections:
            for image_name, image_url in image_details.items():
                response = requests.get(image_url)
                if response.status_code == 200:
                    file_extention = str(os.path.splitext(image_url)[1])
                    file_path = os.path.join(os.getcwd(), "images",
                                self.api_parameters['earth_date'],
                                self._generate_name(image_name) + file_extention)
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
        logger.info(f'Downloading images on date: {self.e_date} complete.')
        return ''
    
    def _setup_directory(self, e_date):
        e_date_path = os.path.join(os.getcwd(),"images",str(e_date))
        if not os.path.exists(e_date_path):
            os.mkdir(e_date_path)


    def _generate_name(self, name):
        new_name = name.replace(' ', '_')
        return str(new_name)