# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class WebHookResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WebHookResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'tipo_evento': 'str',
            'metodo': 'str',
            'url': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'tipo_evento': 'tipoEvento',
            'metodo': 'metodo',
            'url': 'url',
            'status': 'status'
        }

        self._id = None
        self._tipo_evento = None
        self._metodo = None
        self._url = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this WebHookResponse.
        Id do WebHook

        :return: The id of this WebHookResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebHookResponse.
        Id do WebHook

        :param id: The id of this WebHookResponse.
        :type: int
        """
        self._id = id

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this WebHookResponse.
        TipoEvento a ser chamado pelo WebHook

        :return: The tipo_evento of this WebHookResponse.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this WebHookResponse.
        TipoEvento a ser chamado pelo WebHook

        :param tipo_evento: The tipo_evento of this WebHookResponse.
        :type: str
        """
        allowed_values = ["RISCO_FRAUDE", "CODIGO_SEGURANCA", "OUTROS"]
        if tipo_evento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_evento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_evento = tipo_evento

    @property
    def metodo(self):
        """
        Gets the metodo of this WebHookResponse.
        M\u00E9todo que a ser chamado pelo WebHook

        :return: The metodo of this WebHookResponse.
        :rtype: str
        """
        return self._metodo

    @metodo.setter
    def metodo(self, metodo):
        """
        Sets the metodo of this WebHookResponse.
        M\u00E9todo que a ser chamado pelo WebHook

        :param metodo: The metodo of this WebHookResponse.
        :type: str
        """
        allowed_values = ["GET", "POST", "PUT", "DELETE"]
        if metodo not in allowed_values:
            raise ValueError(
                "Invalid value for `metodo`, must be one of {0}"
                .format(allowed_values)
            )
        self._metodo = metodo

    @property
    def url(self):
        """
        Gets the url of this WebHookResponse.
        URL que a ser consumida pelo WebHook

        :return: The url of this WebHookResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WebHookResponse.
        URL que a ser consumida pelo WebHook

        :param url: The url of this WebHookResponse.
        :type: str
        """
        self._url = url

    @property
    def status(self):
        """
        Gets the status of this WebHookResponse.
        Status do WebHook

        :return: The status of this WebHookResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WebHookResponse.
        Status do WebHook

        :param status: The status of this WebHookResponse.
        :type: str
        """
        allowed_values = ["INATIVO", "ATIVO"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

