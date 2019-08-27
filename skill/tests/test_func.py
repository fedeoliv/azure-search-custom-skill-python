import unittest
import json
import azure.functions as func
from skill.__init__ import main

class TestFunction(unittest.TestCase):
    TEST_URL = '/api/skill'

    def test_returns_body_in_result(self):
        body = {
            'values': [
                {
                    'recordId': 'a1',
                    'data': { 'contractText': 'This is a sample contract' }
                }
            ]
        }

        request = func.HttpRequest(
            method='POST',
            url= TestFunction.TEST_URL,
            body= bytearray(json.dumps(body), 'utf-8'))

        response = main(request)

        expected = json.dumps({
            'values': []
        })

        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.get_body(), bytearray(expected, 'utf-8'))

    def test_null_request_body(self):
        request = func.HttpRequest(
            method='POST',
            url= TestFunction.TEST_URL,
            body= None)

        response = main(request)

        expected = 'JSON input data not found'

        self.assertEquals(response.status_code, 400)
        self.assertEqual(response.get_body(), bytearray(expected, 'utf-8'))

    def test_invalid_request_body_property_names(self):
        request_bodies = []

        request_bodies.append({
            'values_test': [
                {
                    'recordId': 'a1',
                    'data': { 'contractText': 'This is a sample contract' }
                }
            ]
        })

        request_bodies.append({
            'values': [
                {
                    'recordId_test': 'a1',
                    'data': { 'contractText': 'This is a sample contract' }
                }
            ]
        })

        request_bodies.append({
            'values': [
                {
                    'recordId': 'a1',
                    'data_test': { 'contractText': 'This is a sample contract' }
                }
            ]
        })

        for body in request_bodies:
            request = func.HttpRequest(
                method='POST',
                url= TestFunction.TEST_URL,
                body= bytearray(json.dumps(body), 'utf-8'))

            response = main(request)

            expected = 'Invalid JSON properties'

            self.assertEquals(response.status_code, 400)
            self.assertEqual(response.get_body(), bytearray(expected, 'utf-8'))
