# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Message(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, description: str=None):  # noqa: E501
        """Message - a model defined in Swagger

        :param code: The code of this Message.  # noqa: E501
        :type code: str
        :param description: The description of this Message.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'code': str,
            'description': str
        }

        self.attribute_map = {
            'code': 'code',
            'description': 'description'
        }

        self._code = code
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Message':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.  # noqa: E501
        :rtype: Message
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this Message.


        :return: The code of this Message.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Message.


        :param code: The code of this Message.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def description(self) -> str:
        """Gets the description of this Message.


        :return: The description of this Message.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Message.


        :param description: The description of this Message.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description
