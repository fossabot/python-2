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
from kubernetes.client.models.v1_volume import V1Volume


class TestV1Volume(unittest.TestCase):
    """ V1Volume unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Volume(self):
        """
        Test V1Volume
        """
        model = kubernetes.client.models.v1_volume.V1Volume()


if __name__ == '__main__':
    unittest.main()
