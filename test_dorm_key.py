import unittest
import requests
import json

class TestCherrypyPrimer(unittest.TestCase):

        SITE_URL = 'http://localhost:51027' #'http://student04.cse.nd.edu:510XX' #Replace this your port number and machine
        DORMS_URL = SITE_URL + '/dorms/'

        def reset_data(self):
                r = requests.delete(self.DORMS_URL)

        def is_json(self, resp):
                try:
                        json.loads(resp)
                        return True
                except ValueError:
                        return False

        def test_dorm_get(self):
                #self.reset_data()
                d_id = 5
                r = requests.get(self.DORMS_URL + str(d_id) + '/')
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                
                self.assertEqual(resp['name'], 'Carroll')
                self.assertEqual(resp['year'], 1906)
                self.assertEqual(resp['gender'], 'Male')
                self.assertEqual(resp['quad'], 'South')
                self.assertEqual(resp['mascot'], 'Vermin')

        def test_dorm_delete(self):
                #self.reset_data()

                d_id = 11

                d = {}
                r = requests.delete(self.DORMS_URL + str(d_id) + '/', data = json.dumps(d))
                self.assertTrue(self.is_json(r.content.decode('utf-8')))
                resp = json.loads(r.content.decode('utf-8'))
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DORMS_URL + str(d_id) + '/')
                self.assertTrue(self.is_json(r.content.decode('utf-8')))
                resp = json.loads(r.content.decode('utf-8'))
                self.assertEqual(resp['result'], 'error')

        #def test_dorm_put_key(self):
        #        self.reset_data()
        #        key = 'HarryPotter'

        #        m = {}
        #        m['value'] = 'Gryffindor'
        #        r = requests.put(self.DORMS_URL + key, data = json.dumps(m)) # uses put
        #        self.assertTrue(self.is_json(r.content.decode()))
        #        resp = json.loads(r.content.decode())
        #        self.assertEqual(resp['result'], 'success')

         #       r = requests.get(self.DICT_URL + key)
        #        self.assertTrue(self.is_json(r.content.decode()))
        #        resp = json.loads(r.content.decode())
        #        self.assertEqual(resp['value'], m['value'])

if __name__ == "__main__":
        unittest.main()
