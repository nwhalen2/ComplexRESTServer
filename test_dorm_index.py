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
            resp = resp['11']

            d = {}
            d['name'] = 'Lyons'
            d['year'] = '1927'
            d['gender'] = 'Female'
            d['quad'] = 'South'
            d['mascot'] = 'Lion'
            self.assertEqual(resp['result'], 'success')

            self.assertEqual(resp['name'], d['name'])
            self.assertEqual(resp['year'], d['year'])
            self.assertEqual(resp['gender'], d['gender'])
            self.assertEqual(resp['quad'], d['quad'])
            self.assertEqual(resp['mascot'], d['mascot'])

        def test_index_delete(self):
                self.reset_data()

                d_id = 12
                d = {}
                d['name'] = 'Flaherty'
                d['year'] = 2016
                d['gender'] = 'Female'
                d['quad'] = 'Mod'
                d['mascot'] = 'Bears'
                r = requests.delete(self.DICT_URL + d_id, data = json.dumps(d)) # uses put
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                #key2 = 'GinnyWeasley'
                #m2 = {}
                #m2['value'] = 'Gryffindor'
                #r = requests.put(self.DICT_URL + key2, data = json.dumps(m2)) # uses put
                #self.assertTrue(self.is_json(r.content.decode()))
                #resp = json.loads(r.content.decode())
                #self.assertEqual(resp['result'], 'success')

                r = requests.delete(self.DICT_URL) # delete index
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + d_id) # uses get
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

                #r = requests.get(self.DICT_URL + key2) # uses get
                #self.assertTrue(self.is_json(r.content.decode()))
                #resp = json.loads(r.content.decode())
                #self.assertEqual(resp['result'], 'error')


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
