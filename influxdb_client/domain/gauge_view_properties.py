# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.view_properties import ViewProperties


class GaugeViewProperties(ViewProperties):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'queries': 'list[DashboardQuery]',
        'colors': 'list[DashboardColor]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'prefix': 'str',
        'tick_prefix': 'str',
        'suffix': 'str',
        'tick_suffix': 'str',
        'legend': 'Legend',
        'decimal_places': 'DecimalPlaces'
    }

    attribute_map = {
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'prefix': 'prefix',
        'tick_prefix': 'tickPrefix',
        'suffix': 'suffix',
        'tick_suffix': 'tickSuffix',
        'legend': 'legend',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, prefix=None, tick_prefix=None, suffix=None, tick_suffix=None, legend=None, decimal_places=None):  # noqa: E501,D401,D403
        """GaugeViewProperties - a model defined in OpenAPI."""  # noqa: E501
        ViewProperties.__init__(self)  # noqa: E501

        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._prefix = None
        self._tick_prefix = None
        self._suffix = None
        self._tick_suffix = None
        self._legend = None
        self._decimal_places = None
        self.discriminator = None

        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.prefix = prefix
        self.tick_prefix = tick_prefix
        self.suffix = suffix
        self.tick_suffix = tick_suffix
        self.legend = legend
        self.decimal_places = decimal_places

    @property
    def type(self):
        """Get the type of this GaugeViewProperties.

        :return: The type of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this GaugeViewProperties.

        :param type: The type of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def queries(self):
        """Get the queries of this GaugeViewProperties.

        :return: The queries of this GaugeViewProperties.
        :rtype: list[DashboardQuery]
        """  # noqa: E501
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Set the queries of this GaugeViewProperties.

        :param queries: The queries of this GaugeViewProperties.
        :type: list[DashboardQuery]
        """  # noqa: E501
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501
        self._queries = queries

    @property
    def colors(self):
        """Get the colors of this GaugeViewProperties.

        Colors define color encoding of data into a visualization

        :return: The colors of this GaugeViewProperties.
        :rtype: list[DashboardColor]
        """  # noqa: E501
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Set the colors of this GaugeViewProperties.

        Colors define color encoding of data into a visualization

        :param colors: The colors of this GaugeViewProperties.
        :type: list[DashboardColor]
        """  # noqa: E501
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501
        self._colors = colors

    @property
    def shape(self):
        """Get the shape of this GaugeViewProperties.

        :return: The shape of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Set the shape of this GaugeViewProperties.

        :param shape: The shape of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501
        self._shape = shape

    @property
    def note(self):
        """Get the note of this GaugeViewProperties.

        :return: The note of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._note

    @note.setter
    def note(self, note):
        """Set the note of this GaugeViewProperties.

        :param note: The note of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501
        self._note = note

    @property
    def show_note_when_empty(self):
        """Get the show_note_when_empty of this GaugeViewProperties.

        If true, will display note when empty

        :return: The show_note_when_empty of this GaugeViewProperties.
        :rtype: bool
        """  # noqa: E501
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Set the show_note_when_empty of this GaugeViewProperties.

        If true, will display note when empty

        :param show_note_when_empty: The show_note_when_empty of this GaugeViewProperties.
        :type: bool
        """  # noqa: E501
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501
        self._show_note_when_empty = show_note_when_empty

    @property
    def prefix(self):
        """Get the prefix of this GaugeViewProperties.

        :return: The prefix of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Set the prefix of this GaugeViewProperties.

        :param prefix: The prefix of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if prefix is None:
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501
        self._prefix = prefix

    @property
    def tick_prefix(self):
        """Get the tick_prefix of this GaugeViewProperties.

        :return: The tick_prefix of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._tick_prefix

    @tick_prefix.setter
    def tick_prefix(self, tick_prefix):
        """Set the tick_prefix of this GaugeViewProperties.

        :param tick_prefix: The tick_prefix of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if tick_prefix is None:
            raise ValueError("Invalid value for `tick_prefix`, must not be `None`")  # noqa: E501
        self._tick_prefix = tick_prefix

    @property
    def suffix(self):
        """Get the suffix of this GaugeViewProperties.

        :return: The suffix of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Set the suffix of this GaugeViewProperties.

        :param suffix: The suffix of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if suffix is None:
            raise ValueError("Invalid value for `suffix`, must not be `None`")  # noqa: E501
        self._suffix = suffix

    @property
    def tick_suffix(self):
        """Get the tick_suffix of this GaugeViewProperties.

        :return: The tick_suffix of this GaugeViewProperties.
        :rtype: str
        """  # noqa: E501
        return self._tick_suffix

    @tick_suffix.setter
    def tick_suffix(self, tick_suffix):
        """Set the tick_suffix of this GaugeViewProperties.

        :param tick_suffix: The tick_suffix of this GaugeViewProperties.
        :type: str
        """  # noqa: E501
        if tick_suffix is None:
            raise ValueError("Invalid value for `tick_suffix`, must not be `None`")  # noqa: E501
        self._tick_suffix = tick_suffix

    @property
    def legend(self):
        """Get the legend of this GaugeViewProperties.

        :return: The legend of this GaugeViewProperties.
        :rtype: Legend
        """  # noqa: E501
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Set the legend of this GaugeViewProperties.

        :param legend: The legend of this GaugeViewProperties.
        :type: Legend
        """  # noqa: E501
        if legend is None:
            raise ValueError("Invalid value for `legend`, must not be `None`")  # noqa: E501
        self._legend = legend

    @property
    def decimal_places(self):
        """Get the decimal_places of this GaugeViewProperties.

        :return: The decimal_places of this GaugeViewProperties.
        :rtype: DecimalPlaces
        """  # noqa: E501
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Set the decimal_places of this GaugeViewProperties.

        :param decimal_places: The decimal_places of this GaugeViewProperties.
        :type: DecimalPlaces
        """  # noqa: E501
        if decimal_places is None:
            raise ValueError("Invalid value for `decimal_places`, must not be `None`")  # noqa: E501
        self._decimal_places = decimal_places

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, GaugeViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
