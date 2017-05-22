# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ProjectedVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, default_mode=None, sources=None):
        """
        V1ProjectedVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_mode': 'int',
            'sources': 'list[V1VolumeProjection]'
        }

        self.attribute_map = {
            'default_mode': 'defaultMode',
            'sources': 'sources'
        }

        self._default_mode = default_mode
        self._sources = sources

    @property
    def default_mode(self):
        """
        Gets the default_mode of this V1ProjectedVolumeSource.
        Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :return: The default_mode of this V1ProjectedVolumeSource.
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """
        Sets the default_mode of this V1ProjectedVolumeSource.
        Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :param default_mode: The default_mode of this V1ProjectedVolumeSource.
        :type: int
        """

        self._default_mode = default_mode

    @property
    def sources(self):
        """
        Gets the sources of this V1ProjectedVolumeSource.
        list of volume projections

        :return: The sources of this V1ProjectedVolumeSource.
        :rtype: list[V1VolumeProjection]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this V1ProjectedVolumeSource.
        list of volume projections

        :param sources: The sources of this V1ProjectedVolumeSource.
        :type: list[V1VolumeProjection]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")

        self._sources = sources

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ProjectedVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
