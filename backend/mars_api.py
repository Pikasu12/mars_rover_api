import requests
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
        details = self._request_image()

        for detail in details['photos']:
            self.image_collections.append({str(f'{detail["id"]}_{detail["camera"]["full_name"]}'): detail["img_src"]})
            self._setup_directory(detail['earth_date'])

        return "Gathering image details done."

    def _download(self):
        for image_details in self.image_collections:
            for image_name, image_url in image_details.items():
                response = requests.get(image_url)
                if response.status_code == 200:
                    file_extention = str(os.path.splitext(image_url)[1])
                    file_path = os.path.join(os.getcwd(), "images",
                                self.api_parameters['earth_date'],
                                self._generate_name(image_name) + file_extention)
                    print(file_path)
                    with open(file_path, 'wb') as f:
                        f.write(response.content) 
        return 'Downloading images done.'
    
    def _setup_directory(self, e_date):
        e_date_path = os.path.join(os.getcwd(),"images",str(e_date))
        if not os.path.exists(e_date_path):
            os.mkdir(e_date_path)


    def _generate_name(self, name):
        new_name = name.replace(' ', '_')
        return str(new_name)

'''
{"photos":[
    {"id":660531,
     "sol":2070,
     "camera":{"id":20,
               "name":"FHAZ","rover_id":5,
               "full_name":"Front Hazard Avoidance Camera"
        },
     "img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/fcam/FLB_581260549EDR_F0701752FHAZ00341M_.JPG",
     "earth_date":"2018-06-02",
     "rover":{
        "id":5,
        "name":"Curiosity",
        "landing_date":"2012-08-06",
        "launch_date":"2011-11-26",
        "status":"active"
        }
    },
    {"id":660532,
     "sol":2070,
     "camera":{"id":20,"name":"FHAZ","rover_id":5,"full_name":"Front Hazard Avoidance Camera"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/fcam/FRB_581260549EDR_F0701752FHAZ00341M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660533,"sol":2070,"camera":{"id":21,"name":"RHAZ","rover_id":5,"full_name":"Rear Hazard Avoidance Camera"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/rcam/RLB_581260590EDR_F0701752RHAZ00341M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660534,"sol":2070,"camera":{"id":21,"name":"RHAZ","rover_id":5,"full_name":"Rear Hazard Avoidance Camera"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/rcam/RRB_581260590EDR_F0701752RHAZ00341M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660535,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/ccam/CR0_581261548EDR_F0701752CCAM02070M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660536,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/ccam/CR0_581261426EDR_F0701752CCAM01070M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660537,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/opgs/edr/ccam/CR0_581260872EDR_F0701752CCAM01070M_.JPG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660538,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/soas/rdr/ccam/CR0_581261548PRC_F0701752CCAM02070L1.PNG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660539,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/soas/rdr/ccam/CR0_581261426PRC_F0701752CCAM01070L1.PNG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}},{"id":660540,"sol":2070,"camera":{"id":23,"name":"CHEMCAM","rover_id":5,"full_name":"Chemistry and Camera Complex"},"img_src":"http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02070/soas/rdr/ccam/CR0_581260872PRC_F0701752CCAM01070L1.PNG","earth_date":"2018-06-02","rover":{"id":5,"name":"Curiosity","landing_date":"2012-08-06","launch_date":"2011-11-26","status":"active"}}]}

'''