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


class CodigoSegurancaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CodigoSegurancaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_emissor': 'int',
            'modo_envio': 'str',
            'contato': 'str',
            'ativo': 'bool',
            'data_validade': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_emissor': 'idEmissor',
            'modo_envio': 'modoEnvio',
            'contato': 'contato',
            'ativo': 'ativo',
            'data_validade': 'dataValidade'
        }

        self._id = None
        self._id_emissor = None
        self._modo_envio = None
        self._contato = None
        self._ativo = None
        self._data_validade = None

    @property
    def id(self):
        """
        Gets the id of this CodigoSegurancaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do c\u00F3digo de seguranca (id).

        :return: The id of this CodigoSegurancaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CodigoSegurancaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do c\u00F3digo de seguranca (id).

        :param id: The id of this CodigoSegurancaResponse.
        :type: int
        """
        self._id = id

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this CodigoSegurancaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Emissor (idEmissor).

        :return: The id_emissor of this CodigoSegurancaResponse.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this CodigoSegurancaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Emissor (idEmissor).

        :param id_emissor: The id_emissor of this CodigoSegurancaResponse.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def modo_envio(self):
        """
        Gets the modo_envio of this CodigoSegurancaResponse.
        Apresenta o Modo de Envio do C\u00F3digo de Seguran\u00E7a.

        :return: The modo_envio of this CodigoSegurancaResponse.
        :rtype: str
        """
        return self._modo_envio

    @modo_envio.setter
    def modo_envio(self, modo_envio):
        """
        Sets the modo_envio of this CodigoSegurancaResponse.
        Apresenta o Modo de Envio do C\u00F3digo de Seguran\u00E7a.

        :param modo_envio: The modo_envio of this CodigoSegurancaResponse.
        :type: str
        """
        self._modo_envio = modo_envio

    @property
    def contato(self):
        """
        Gets the contato of this CodigoSegurancaResponse.
        Apresenta o contato do c\u00F3digo de seguran\u00E7a.

        :return: The contato of this CodigoSegurancaResponse.
        :rtype: str
        """
        return self._contato

    @contato.setter
    def contato(self, contato):
        """
        Sets the contato of this CodigoSegurancaResponse.
        Apresenta o contato do c\u00F3digo de seguran\u00E7a.

        :param contato: The contato of this CodigoSegurancaResponse.
        :type: str
        """
        self._contato = contato

    @property
    def ativo(self):
        """
        Gets the ativo of this CodigoSegurancaResponse.
        Apresenta o status do c\u00F3digo de seguran\u00E7a.

        :return: The ativo of this CodigoSegurancaResponse.
        :rtype: bool
        """
        return self._ativo

    @ativo.setter
    def ativo(self, ativo):
        """
        Sets the ativo of this CodigoSegurancaResponse.
        Apresenta o status do c\u00F3digo de seguran\u00E7a.

        :param ativo: The ativo of this CodigoSegurancaResponse.
        :type: bool
        """
        self._ativo = ativo

    @property
    def data_validade(self):
        """
        Gets the data_validade of this CodigoSegurancaResponse.
        Apresenta a data de validade do c\u00F3digo de seguran\u00E7a gerado.

        :return: The data_validade of this CodigoSegurancaResponse.
        :rtype: str
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this CodigoSegurancaResponse.
        Apresenta a data de validade do c\u00F3digo de seguran\u00E7a gerado.

        :param data_validade: The data_validade of this CodigoSegurancaResponse.
        :type: str
        """
        self._data_validade = data_validade

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

