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
from kubernetes.client.models.v1_label_selector import V1LabelSelector


class TestV1LabelSelector(unittest.TestCase):
    """ V1LabelSelector unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1LabelSelector(self):
        """
        Test V1LabelSelector
        """
        model = kubernetes.client.models.v1_label_selector.V1LabelSelector()


if __name__ == '__main__':
    unittest.main()
