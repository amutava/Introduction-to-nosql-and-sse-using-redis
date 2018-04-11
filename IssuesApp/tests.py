import unittest
import json

from issues import create_app, db


class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.client = self.app.test_client()
        self.ctx.push()
        db.flushdb

        self.issue = {
            "name": "Why are you so worried."
        }

    def test_create_issue(self):
        resp = self.client.post('/api/issue/',
                                data=json.dumps(self.issue),
                                content_type="application/json"
                                )
        self.assertEqual(resp.status_code, 201)

    def test_get_all_issues(self):
        resp = self.client.post('/api/issue/',
                                data=json.dumps(self.issue),
                                content_type="application/json"
                                )
        self.assertEqual(resp.status_code, 201)
        resp_1 = self.client.get('/api/issue/')
        self.assertEqual(resp_1.status_code, 200)

    def test_delete_an_issue(self):
        resp = self.client.post('/api/issue/',
                                data=json.dumps(self.issue),
                                content_type="application/json"
                                )
        self.assertEqual(resp.status_code, 201)
        resp_1 = self.client.delete('/api/issue/', data=json.dumps(
            self.issue), content_type="application/json")
        self.assertEqual(resp_1.status_code, 204)

    def tearDown(self):
        pass
