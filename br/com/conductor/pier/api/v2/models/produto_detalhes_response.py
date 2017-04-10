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


class ProdutoDetalhesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProdutoDetalhesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'nome': 'str',
            'status': 'int',
            'id_fantasia_basica': 'int',
            'fantasia_basica': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'nome': 'nome',
            'status': 'status',
            'id_fantasia_basica': 'idFantasiaBasica',
            'fantasia_basica': 'fantasiaBasica'
        }

        self._id = None
        self._nome = None
        self._status = None
        self._id_fantasia_basica = None
        self._fantasia_basica = None

    @property
    def id(self):
        """
        Gets the id of this ProdutoDetalhesResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto (id).

        :return: The id of this ProdutoDetalhesResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProdutoDetalhesResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Produto (id).

        :param id: The id of this ProdutoDetalhesResponse.
        :type: int
        """
        self._id = id

    @property
    def nome(self):
        """
        Gets the nome of this ProdutoDetalhesResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do Nome do Produto.

        :return: The nome of this ProdutoDetalhesResponse.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this ProdutoDetalhesResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do Nome do Produto.

        :param nome: The nome of this ProdutoDetalhesResponse.
        :type: str
        """
        self._nome = nome

    @property
    def status(self):
        """
        Gets the status of this ProdutoDetalhesResponse.
        Representa o Status do Produto, onde: (\"0\": Inativo), (\"1\": Ativo).

        :return: The status of this ProdutoDetalhesResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProdutoDetalhesResponse.
        Representa o Status do Produto, onde: (\"0\": Inativo), (\"1\": Ativo).

        :param status: The status of this ProdutoDetalhesResponse.
        :type: int
        """
        self._status = status

    @property
    def id_fantasia_basica(self):
        """
        Gets the id_fantasia_basica of this ProdutoDetalhesResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Fantasia B\u00C3\u00A1sica (id) a qual o produto pertence.

        :return: The id_fantasia_basica of this ProdutoDetalhesResponse.
        :rtype: int
        """
        return self._id_fantasia_basica

    @id_fantasia_basica.setter
    def id_fantasia_basica(self, id_fantasia_basica):
        """
        Sets the id_fantasia_basica of this ProdutoDetalhesResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Fantasia B\u00C3\u00A1sica (id) a qual o produto pertence.

        :param id_fantasia_basica: The id_fantasia_basica of this ProdutoDetalhesResponse.
        :type: int
        """
        self._id_fantasia_basica = id_fantasia_basica

    @property
    def fantasia_basica(self):
        """
        Gets the fantasia_basica of this ProdutoDetalhesResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o da Fantasia B\u00C3\u00A1sica a qual o produto pertence.

        :return: The fantasia_basica of this ProdutoDetalhesResponse.
        :rtype: str
        """
        return self._fantasia_basica

    @fantasia_basica.setter
    def fantasia_basica(self, fantasia_basica):
        """
        Sets the fantasia_basica of this ProdutoDetalhesResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o da Fantasia B\u00C3\u00A1sica a qual o produto pertence.

        :param fantasia_basica: The fantasia_basica of this ProdutoDetalhesResponse.
        :type: str
        """
        self._fantasia_basica = fantasia_basica

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
