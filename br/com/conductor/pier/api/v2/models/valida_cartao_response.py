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


class ValidaCartaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ValidaCartaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_status_cartao': 'int',
            'status_cartao': 'str',
            'id_status_conta': 'int',
            'status_conta': 'str',
            'id_conta': 'int',
            'numero_agencia': 'int',
            'numero_conta_corrente': 'str',
            'criptograma_resposta': 'str'
        }

        self.attribute_map = {
            'id_status_cartao': 'idStatusCartao',
            'status_cartao': 'statusCartao',
            'id_status_conta': 'idStatusConta',
            'status_conta': 'statusConta',
            'id_conta': 'idConta',
            'numero_agencia': 'numeroAgencia',
            'numero_conta_corrente': 'numeroContaCorrente',
            'criptograma_resposta': 'criptogramaResposta'
        }

        self._id_status_cartao = None
        self._status_cartao = None
        self._id_status_conta = None
        self._status_conta = None
        self._id_conta = None
        self._numero_agencia = None
        self._numero_conta_corrente = None
        self._criptograma_resposta = None

    @property
    def id_status_cartao(self):
        """
        Gets the id_status_cartao of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status do cart\u00E3o

        :return: The id_status_cartao of this ValidaCartaoResponse.
        :rtype: int
        """
        return self._id_status_cartao

    @id_status_cartao.setter
    def id_status_cartao(self, id_status_cartao):
        """
        Sets the id_status_cartao of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status do cart\u00E3o

        :param id_status_cartao: The id_status_cartao of this ValidaCartaoResponse.
        :type: int
        """
        self._id_status_cartao = id_status_cartao

    @property
    def status_cartao(self):
        """
        Gets the status_cartao of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status do cart\u00E3o

        :return: The status_cartao of this ValidaCartaoResponse.
        :rtype: str
        """
        return self._status_cartao

    @status_cartao.setter
    def status_cartao(self, status_cartao):
        """
        Sets the status_cartao of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status do cart\u00E3o

        :param status_cartao: The status_cartao of this ValidaCartaoResponse.
        :type: str
        """
        self._status_cartao = status_cartao

    @property
    def id_status_conta(self):
        """
        Gets the id_status_conta of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status da conta

        :return: The id_status_conta of this ValidaCartaoResponse.
        :rtype: int
        """
        return self._id_status_conta

    @id_status_conta.setter
    def id_status_conta(self, id_status_conta):
        """
        Sets the id_status_conta of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status da conta

        :param id_status_conta: The id_status_conta of this ValidaCartaoResponse.
        :type: int
        """
        self._id_status_conta = id_status_conta

    @property
    def status_conta(self):
        """
        Gets the status_conta of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status da conta

        :return: The status_conta of this ValidaCartaoResponse.
        :rtype: str
        """
        return self._status_conta

    @status_conta.setter
    def status_conta(self, status_conta):
        """
        Sets the status_conta of this ValidaCartaoResponse.
        Descri\u00E7\u00E3o do status da conta

        :param status_conta: The status_conta of this ValidaCartaoResponse.
        :type: str
        """
        self._status_conta = status_conta

    @property
    def id_conta(self):
        """
        Gets the id_conta of this ValidaCartaoResponse.
        C\u00F3digo identificador da conta.

        :return: The id_conta of this ValidaCartaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this ValidaCartaoResponse.
        C\u00F3digo identificador da conta.

        :param id_conta: The id_conta of this ValidaCartaoResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this ValidaCartaoResponse.
        N\u00FAmero da ag\u00EAncia.

        :return: The numero_agencia of this ValidaCartaoResponse.
        :rtype: int
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this ValidaCartaoResponse.
        N\u00FAmero da ag\u00EAncia.

        :param numero_agencia: The numero_agencia of this ValidaCartaoResponse.
        :type: int
        """
        self._numero_agencia = numero_agencia

    @property
    def numero_conta_corrente(self):
        """
        Gets the numero_conta_corrente of this ValidaCartaoResponse.
        N\u00FAmero da conta corrente.

        :return: The numero_conta_corrente of this ValidaCartaoResponse.
        :rtype: str
        """
        return self._numero_conta_corrente

    @numero_conta_corrente.setter
    def numero_conta_corrente(self, numero_conta_corrente):
        """
        Sets the numero_conta_corrente of this ValidaCartaoResponse.
        N\u00FAmero da conta corrente.

        :param numero_conta_corrente: The numero_conta_corrente of this ValidaCartaoResponse.
        :type: str
        """
        self._numero_conta_corrente = numero_conta_corrente

    @property
    def criptograma_resposta(self):
        """
        Gets the criptograma_resposta of this ValidaCartaoResponse.
        Criptograma de resposta

        :return: The criptograma_resposta of this ValidaCartaoResponse.
        :rtype: str
        """
        return self._criptograma_resposta

    @criptograma_resposta.setter
    def criptograma_resposta(self, criptograma_resposta):
        """
        Sets the criptograma_resposta of this ValidaCartaoResponse.
        Criptograma de resposta

        :param criptograma_resposta: The criptograma_resposta of this ValidaCartaoResponse.
        :type: str
        """
        self._criptograma_resposta = criptograma_resposta

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

