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
from kubernetes.client.models.v1beta1_cluster_role_binding import V1beta1ClusterRoleBinding


class TestV1beta1ClusterRoleBinding(unittest.TestCase):
    """ V1beta1ClusterRoleBinding unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1ClusterRoleBinding(self):
        """
        Test V1beta1ClusterRoleBinding
        """
        model = kubernetes.client.models.v1beta1_cluster_role_binding.V1beta1ClusterRoleBinding()


if __name__ == '__main__':
    unittest.main()
