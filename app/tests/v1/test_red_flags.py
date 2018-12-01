import unittest

import json



from app import create_app



app = create_app()

class RedFlagTestCase(unittest.TestCase):

    def setUp(self):

        app.testing = True

        self.app = app.test_client()

        self.data = {

            "id": 1,

            "createdOn" : "Tue, 27 Nov 2018 21:18:13 GMT",

            "createdBy" : "Admin",

            'type' : 'red-flags',

            "location" : "kayole",

            "status" : "draft",

            "images" : "",

            "videos" : "",

            "title" : "Police taking bribe",

            "comment" : "this case should be seriously handled."

        }



    def test_get_all_redflags(self):

        """Test all redflags"""

        response = self.app.get("/api/v1/red-flags")

        result = json.loads(response.data)

        self.assertEqual(response.status_code, 200)



    def test_post_redflag(self):

        """Test post a redflag"""

        result = self.app.post("/api/v1/red-flags",

                    headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))

        self.assertEqual(result.status_code, 201)

        self.assertIn('Thank You for Creating a Red-Flag', str(result.data))



    def test_get_specific_redflag(self):

        """Test get a specific redflag"""

        response = self.app.post("/api/v1/red-flags",

                    headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))

        result = self.app.get("/api/v1/red-flags/1")

        self.assertEqual(result.status_code, 200)   



    def test_update_location_of_specific_redflag(self):

        """Test update location of a specific redflag"""

        result = self.app.patch("/api/v1/red-flags/1/location",

                    headers={'Content-Type': 'application/json'}, data=json.dumps({"location" : "kayole"}))

        self.assertEqual(result.status_code, 200)    

        self.assertIn("Updated red-flag records location", str(result.data))



    def test_update_comment_of_specific_redflag(self):

        """Test update comment of a specific redflag"""

        result = self.app.patch("/api/v1/red-flags/1/comment",

                    headers={'Content-Type': 'application/json'}, data=json.dumps({"comment" : "Cartels are taking over Kenya"}))

        self.assertEqual(result.status_code, 200) 

        self.assertIn("Updated red-flag records comment", str(result.data)) 





    def test_delete_specific_redflag(self):

        """Test delete a specific redflag"""

        response = self.app.post("/api/v1/red-flags",

                    headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))

        result = self.app.delete("/api/v1/red-flags/1")

        self.assertEqual(result.status_code, 200)

        self.assertIn('red-flag record has been deleted', str(result.data))  



    def test_redflag_not_found(self):

        """Test a redflag not found"""

        result = self.app.get("/api/v1/red-flags/10")

        self.assertEqual(result.status_code, 404) 

        self.assertIn('Red flag does not exist', str(result.data))                          



if __name__ == "__main__":

    unittest.main() 


