# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_secret_key_selector import V1SecretKeySelector


class TestV1SecretKeySelector(unittest.TestCase):
    """ V1SecretKeySelector unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1SecretKeySelector(self):
        """
        Test V1SecretKeySelector
        """
        model = kubernetes.client.models.v1_secret_key_selector.V1SecretKeySelector()


if __name__ == '__main__':
    unittest.main()
