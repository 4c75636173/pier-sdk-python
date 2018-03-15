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


class StatusOportunidade(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatusOportunidade - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nome': 'str',
            'descricao': 'str',
            'flag_ativo': 'bool'
        }

        self.attribute_map = {
            'nome': 'nome',
            'descricao': 'descricao',
            'flag_ativo': 'flagAtivo'
        }

        self._nome = None
        self._descricao = None
        self._flag_ativo = None

    @property
    def nome(self):
        """
        Gets the nome of this StatusOportunidade.
        Nome do status oportunidade

        :return: The nome of this StatusOportunidade.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this StatusOportunidade.
        Nome do status oportunidade

        :param nome: The nome of this StatusOportunidade.
        :type: str
        """
        self._nome = nome

    @property
    def descricao(self):
        """
        Gets the descricao of this StatusOportunidade.
        Descri\u00E7\u00E3o do status oportunidade

        :return: The descricao of this StatusOportunidade.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this StatusOportunidade.
        Descri\u00E7\u00E3o do status oportunidade

        :param descricao: The descricao of this StatusOportunidade.
        :type: str
        """
        self._descricao = descricao

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this StatusOportunidade.
        Flag de verifica\u00E7\u00E3o se o status oportunidade est\u00E1 ativo

        :return: The flag_ativo of this StatusOportunidade.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this StatusOportunidade.
        Flag de verifica\u00E7\u00E3o se o status oportunidade est\u00E1 ativo

        :param flag_ativo: The flag_ativo of this StatusOportunidade.
        :type: bool
        """
        self._flag_ativo = flag_ativo

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

