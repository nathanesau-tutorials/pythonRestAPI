from flask import Flask, jsonify, abort, make_response, request
import unittest
import os
import subprocess
import time
import socket

# test functionality using curl
class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.proc = subprocess.Popen(["python3", "app.py"])
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start = time.time()
        while (time.time() - start) < 5: # timeout after 10 seconds
            result_of_check = a_socket.connect_ex(('localhost', 5000))
            if result_of_check == 0:
                return
        raise Exception("Unable to start server on PORT 5000")      

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()

    def run_curl_command(self, curl_command):
        return subprocess.check_output(curl_command, shell=True)

    def test_get_tasks(self):
        output = self.run_curl_command("curl -i http://localhost:5000/todo/api/v1.0/tasks")
        self.assertTrue("200 OK".lower() in output.decode("UTF-8").lower())

    def test_create_task(self):
        output = self.run_curl_command("curl -i -H \"Content-Type: application/json\" -X POST -d '{\"title\": \"Read a book\"}' http://localhost:5000/todo/api/v1.0/tasks")
        self.assertTrue("201 CREATED".lower() in output.decode("UTF-8").lower())

    def test_get_task(self):
        output1 = self.run_curl_command("curl -i http://localhost:5000/todo/api/v1.0/tasks/1")
        output2 = self.run_curl_command("curl -i http://localhost:5000/todo/api/v1.0/tasks/2")
        output3 = self.run_curl_command("curl -i http://localhost:5000/todo/api/v1.0/tasks/123456") # DNE
        self.assertTrue("200 OK".lower() in output1.decode('UTF-8').lower())
        self.assertTrue("200 OK".lower() in output2.decode("UTF-8").lower())
        self.assertTrue("404 NOT FOUND".lower() in output3.decode("UTF-8").lower())
