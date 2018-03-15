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


class TransferenciaDetalheResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransferenciaDetalheResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'data_transferencia': 'str',
            'id_conta_origem': 'int',
            'nome_pessoa_origem': 'str',
            'id_conta_destino': 'int',
            'nome_pessoa_destino': 'str',
            'valor_transferencia': 'float',
            'valor_tarifa': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'data_transferencia': 'dataTransferencia',
            'id_conta_origem': 'idContaOrigem',
            'nome_pessoa_origem': 'nomePessoaOrigem',
            'id_conta_destino': 'idContaDestino',
            'nome_pessoa_destino': 'nomePessoaDestino',
            'valor_transferencia': 'valorTransferencia',
            'valor_tarifa': 'valorTarifa'
        }

        self._id = None
        self._data_transferencia = None
        self._id_conta_origem = None
        self._nome_pessoa_origem = None
        self._id_conta_destino = None
        self._nome_pessoa_destino = None
        self._valor_transferencia = None
        self._valor_tarifa = None

    @property
    def id(self):
        """
        Gets the id of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da transfer\u00EAncia (id).

        :return: The id of this TransferenciaDetalheResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da transfer\u00EAncia (id).

        :param id: The id of this TransferenciaDetalheResponse.
        :type: int
        """
        self._id = id

    @property
    def data_transferencia(self):
        """
        Gets the data_transferencia of this TransferenciaDetalheResponse.
        Data estabelecida para ocorrer a transfer\u00EAncia.

        :return: The data_transferencia of this TransferenciaDetalheResponse.
        :rtype: str
        """
        return self._data_transferencia

    @data_transferencia.setter
    def data_transferencia(self, data_transferencia):
        """
        Sets the data_transferencia of this TransferenciaDetalheResponse.
        Data estabelecida para ocorrer a transfer\u00EAncia.

        :param data_transferencia: The data_transferencia of this TransferenciaDetalheResponse.
        :type: str
        """
        self._data_transferencia = data_transferencia

    @property
    def id_conta_origem(self):
        """
        Gets the id_conta_origem of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da conta em que o valor ser\u00E1 debitado para a transfer\u00EAncia. (id).

        :return: The id_conta_origem of this TransferenciaDetalheResponse.
        :rtype: int
        """
        return self._id_conta_origem

    @id_conta_origem.setter
    def id_conta_origem(self, id_conta_origem):
        """
        Sets the id_conta_origem of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da conta em que o valor ser\u00E1 debitado para a transfer\u00EAncia. (id).

        :param id_conta_origem: The id_conta_origem of this TransferenciaDetalheResponse.
        :type: int
        """
        self._id_conta_origem = id_conta_origem

    @property
    def nome_pessoa_origem(self):
        """
        Gets the nome_pessoa_origem of this TransferenciaDetalheResponse.
        Apresenta o nome completo da pessoa que realizou a Transfer\u00EAncia.

        :return: The nome_pessoa_origem of this TransferenciaDetalheResponse.
        :rtype: str
        """
        return self._nome_pessoa_origem

    @nome_pessoa_origem.setter
    def nome_pessoa_origem(self, nome_pessoa_origem):
        """
        Sets the nome_pessoa_origem of this TransferenciaDetalheResponse.
        Apresenta o nome completo da pessoa que realizou a Transfer\u00EAncia.

        :param nome_pessoa_origem: The nome_pessoa_origem of this TransferenciaDetalheResponse.
        :type: str
        """
        self._nome_pessoa_origem = nome_pessoa_origem

    @property
    def id_conta_destino(self):
        """
        Gets the id_conta_destino of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da conta em que o valor ser\u00E1 creditado para a transfer\u00EAncia. (id).

        :return: The id_conta_destino of this TransferenciaDetalheResponse.
        :rtype: int
        """
        return self._id_conta_destino

    @id_conta_destino.setter
    def id_conta_destino(self, id_conta_destino):
        """
        Sets the id_conta_destino of this TransferenciaDetalheResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da conta em que o valor ser\u00E1 creditado para a transfer\u00EAncia. (id).

        :param id_conta_destino: The id_conta_destino of this TransferenciaDetalheResponse.
        :type: int
        """
        self._id_conta_destino = id_conta_destino

    @property
    def nome_pessoa_destino(self):
        """
        Gets the nome_pessoa_destino of this TransferenciaDetalheResponse.
        Apresenta o nome completo da pessoa que recebeu a Transfer\u00EAncia.

        :return: The nome_pessoa_destino of this TransferenciaDetalheResponse.
        :rtype: str
        """
        return self._nome_pessoa_destino

    @nome_pessoa_destino.setter
    def nome_pessoa_destino(self, nome_pessoa_destino):
        """
        Sets the nome_pessoa_destino of this TransferenciaDetalheResponse.
        Apresenta o nome completo da pessoa que recebeu a Transfer\u00EAncia.

        :param nome_pessoa_destino: The nome_pessoa_destino of this TransferenciaDetalheResponse.
        :type: str
        """
        self._nome_pessoa_destino = nome_pessoa_destino

    @property
    def valor_transferencia(self):
        """
        Gets the valor_transferencia of this TransferenciaDetalheResponse.
        Valor estabelecido para ser transferido.

        :return: The valor_transferencia of this TransferenciaDetalheResponse.
        :rtype: float
        """
        return self._valor_transferencia

    @valor_transferencia.setter
    def valor_transferencia(self, valor_transferencia):
        """
        Sets the valor_transferencia of this TransferenciaDetalheResponse.
        Valor estabelecido para ser transferido.

        :param valor_transferencia: The valor_transferencia of this TransferenciaDetalheResponse.
        :type: float
        """
        self._valor_transferencia = valor_transferencia

    @property
    def valor_tarifa(self):
        """
        Gets the valor_tarifa of this TransferenciaDetalheResponse.
        Valor estabelecido da tarifa para a transfer\u00EAncia.

        :return: The valor_tarifa of this TransferenciaDetalheResponse.
        :rtype: float
        """
        return self._valor_tarifa

    @valor_tarifa.setter
    def valor_tarifa(self, valor_tarifa):
        """
        Sets the valor_tarifa of this TransferenciaDetalheResponse.
        Valor estabelecido da tarifa para a transfer\u00EAncia.

        :param valor_tarifa: The valor_tarifa of this TransferenciaDetalheResponse.
        :type: float
        """
        self._valor_tarifa = valor_tarifa

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

