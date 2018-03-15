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


class IntegrarDocumentoRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IntegrarDocumentoRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_template': 'int',
            'arquivo': 'str',
            'nome': 'str',
            'propriedades': 'list[PropriedadeDocumentoRequest]'
        }

        self.attribute_map = {
            'id_template': 'idTemplate',
            'arquivo': 'arquivo',
            'nome': 'nome',
            'propriedades': 'propriedades'
        }

        self._id_template = None
        self._arquivo = None
        self._nome = None
        self._propriedades = None

    @property
    def id_template(self):
        """
        Gets the id_template of this IntegrarDocumentoRequest.
        Identificador do template de documento

        :return: The id_template of this IntegrarDocumentoRequest.
        :rtype: int
        """
        return self._id_template

    @id_template.setter
    def id_template(self, id_template):
        """
        Sets the id_template of this IntegrarDocumentoRequest.
        Identificador do template de documento

        :param id_template: The id_template of this IntegrarDocumentoRequest.
        :type: int
        """
        self._id_template = id_template

    @property
    def arquivo(self):
        """
        Gets the arquivo of this IntegrarDocumentoRequest.
        Conte\u00FAdo do arquivo convertido em Base 64

        :return: The arquivo of this IntegrarDocumentoRequest.
        :rtype: str
        """
        return self._arquivo

    @arquivo.setter
    def arquivo(self, arquivo):
        """
        Sets the arquivo of this IntegrarDocumentoRequest.
        Conte\u00FAdo do arquivo convertido em Base 64

        :param arquivo: The arquivo of this IntegrarDocumentoRequest.
        :type: str
        """
        self._arquivo = arquivo

    @property
    def nome(self):
        """
        Gets the nome of this IntegrarDocumentoRequest.
        Nome do arquivo.

        :return: The nome of this IntegrarDocumentoRequest.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this IntegrarDocumentoRequest.
        Nome do arquivo.

        :param nome: The nome of this IntegrarDocumentoRequest.
        :type: str
        """
        self._nome = nome

    @property
    def propriedades(self):
        """
        Gets the propriedades of this IntegrarDocumentoRequest.
        Lista de par\u00E2metros para montagem do documento.

        :return: The propriedades of this IntegrarDocumentoRequest.
        :rtype: list[PropriedadeDocumentoRequest]
        """
        return self._propriedades

    @propriedades.setter
    def propriedades(self, propriedades):
        """
        Sets the propriedades of this IntegrarDocumentoRequest.
        Lista de par\u00E2metros para montagem do documento.

        :param propriedades: The propriedades of this IntegrarDocumentoRequest.
        :type: list[PropriedadeDocumentoRequest]
        """
        self._propriedades = propriedades

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

