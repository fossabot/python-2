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
from kubernetes.client.models.v1beta1_policy_rule import V1beta1PolicyRule


class TestV1beta1PolicyRule(unittest.TestCase):
    """ V1beta1PolicyRule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1PolicyRule(self):
        """
        Test V1beta1PolicyRule
        """
        model = kubernetes.client.models.v1beta1_policy_rule.V1beta1PolicyRule()


if __name__ == '__main__':
    unittest.main()
