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

        def test_index_get(self):

            r = requests.get(self.DORMS_URL)
            print(self.DORMS_URL)
            self.assertTrue(self.is_json(r.content.decode()))
            resp = json.loads(r.content.decode())
            print(resp)
            resp = resp['19']

            self.assertEqual(resp['result'], 'success')

            self.assertEqual(resp['name'], 'Lyons')
            self.assertEqual(resp['year'], '1927')
            self.assertEqual(resp['gender'], 'Female')
            self.assertEqual(resp['quad'], 'South')
            self.assertEqual(resp['mascot'], 'Lion')

        def test_index_delete(self):

                d_id = 12
                d = {}

                r = requests.delete(self.DORMS_URL, data = json.dumps(d)) # uses put
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.delete(self.DORMS_URL + str(d_id) + '/') # delete index
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

                r = requests.get(self.DORMS_URL + str(d_id) + '/') # uses get
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')


        #def test_dict_index_post(self):
        #        self.reset_data()

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
