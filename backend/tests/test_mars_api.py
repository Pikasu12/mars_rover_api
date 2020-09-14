import unittest
from manager.mars_api import MarsPhoto
from unittest.mock import patch

class MarsPhotoDownloadTestCase(unittest.TestCase):

    def setUp(self):
        self.test_key = "TEST_API_KEY"
        self.test_e_date = "2017-06-02"
        self.test_api_response = {
            "photos":[
                {"id":10001,
                "camera":{"full_name":"Test full name"},
                "img_src":"http://test_url_image.JPG",
                "earth_date":"2017-06-02",
                }]
        }
        
    @patch('manager.mars_api.MarsPhoto')
    def test_getting_image_details(self, mock_get_request):
        mock_mars_photo = mock_get_request()
        mock_mars_photo._request_image.return_value = self.test_api_response

        mock_response = mock_mars_photo._request_image()

        self.assertIsNotNone(mock_response)
        self.assertEqual(mock_response, self.test_api_response)

    @patch('manager.mars_api.MarsPhoto')
    def test_downloading_image(self, mock_get_request):
        mock_mars_photo = mock_get_request()
        mock_mars_photo._download.return_value = "Downloading images done."

        mock_response = mock_mars_photo._download()
        self.assertIsNotNone(mock_response)
        self.assertEqual(mock_response, "Downloading images done.")