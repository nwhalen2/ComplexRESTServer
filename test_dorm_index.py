import unittest
import requests
import json

class TestCherrypyPrimer(unittest.TestCase):

        SITE_URL = 'http://localhost:51027' #'http://student04.cse.nd.edu:510XX' #Replace this your port number and machine
        DORMS_URL = SITE_URL + '/dorms/'
        RESET_URL = SITE_URL + '/reset/'

        def reset_data(self):
            d = {}
            r = requests.put(self.RESET_URL, data = json.dumps(d))

        def is_json(self, resp):
                try:
                        json.loads(resp)
                        return True
                except ValueError:
                        return False

        def test_index_get(self):
            self.reset_data()

            r = requests.get(self.DORMS_URL)
            print(self.DORMS_URL)
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp['result'], 'success')

            for key in resp:
                if key == '19':
                    resp2 = resp[key]

            self.assertEqual(resp2['name'], 'Lyons')
            self.assertEqual(resp2['year'], 1927)
            self.assertEqual(resp2['gender'], 'Female')
            self.assertEqual(resp2['quad'], 'South')
            self.assertEqual(resp2['mascot'], 'Lion')

        def test_index_delete(self):
            self.reset_data()

            d_id = 12
            d = {}

            r = requests.get(self.DORMS_URL) # get before delete
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())

            r = requests.delete(self.DORMS_URL, data = json.dumps(d)) # deletes all data
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            #print("delete output: " + str(resp))
            self.assertEqual(resp['result'], 'success')

            r = requests.delete(self.DORMS_URL + str(d_id) + '/') # attempt to delete already deleted key
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp['result'], 'error')

            r = requests.get(self.DORMS_URL + str(d_id) + '/') # attempt to get deleted key
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp['result'], 'error')

            self.reset_data()


        def test_index_post(self):
            self.reset_data()

            d = {}
            d['name'] = 'McKenna'
            d['year'] = 2021
            d['gender'] = 'Male'
            d['quad'] = 'East'
            d['mascot'] = 'Eagles'

            r = requests.post(self.DORMS_URL, data = json.dumps(d))
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            self.assertEqual(resp['result'], 'success')
            self.assertEqual(resp['id'], 34)

            r = requests.get(self.DORMS_URL + str(resp['id']) + '/')
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            print(resp)
            # !!!!! POST DOES NOT WORK YET !!!!!!!!!!!!!!!!!!!!
            # ALWAYS TREATS BODY AS "name": "name"... etc !!!!!



            #r = requests.get(self.DORMS_URL + str())

         #       m = {}
         #       m['key'] = 'HarryPotter'
        #        m['value'] = 'Gryffindor'

        #        r = requests.post(self.DICT_URL, data = json.dumps(m)) # performing post
        #        self.assertTrue(self.is_json(r.content.decode()))
        #        resp = json.loads(r.content.decode())
        #        self.assertEqual(resp['result'], 'success')

        #        r = requests.get(self.DICT_URL) # uses get
        #        self.assertTrue(self.is_json(r.content.decode()))
        #        resp = json.loads(r.content.decode())
        #        self.assertEqual(resp['result'], 'success')

        #        entries = resp['entries']
        #        mkv = entries[0]
        #        self.assertEqual(mkv['key'], m['key'])
        #        self.assertEqual(mkv['value'], m['value'])

if __name__ == "__main__":
        unittest.main()
