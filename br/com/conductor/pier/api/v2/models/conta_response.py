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


class ContaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_produto': 'int',
            'id_origem_comercial': 'int',
            'id_pessoa': 'int',
            'id_status_conta': 'int',
            'dia_vencimento': 'int',
            'melhor_dia_compra': 'int',
            'data_status_conta': 'str',
            'data_cadastro': 'str',
            'data_ultima_alteracao_vencimento': 'str',
            'valor_renda': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'id_produto': 'idProduto',
            'id_origem_comercial': 'idOrigemComercial',
            'id_pessoa': 'idPessoa',
            'id_status_conta': 'idStatusConta',
            'dia_vencimento': 'diaVencimento',
            'melhor_dia_compra': 'melhorDiaCompra',
            'data_status_conta': 'dataStatusConta',
            'data_cadastro': 'dataCadastro',
            'data_ultima_alteracao_vencimento': 'dataUltimaAlteracaoVencimento',
            'valor_renda': 'valorRenda'
        }

        self._id = None
        self._id_produto = None
        self._id_origem_comercial = None
        self._id_pessoa = None
        self._id_status_conta = None
        self._dia_vencimento = None
        self._melhor_dia_compra = None
        self._data_status_conta = None
        self._data_cadastro = None
        self._data_ultima_alteracao_vencimento = None
        self._valor_renda = None

    @property
    def id(self):
        """
        Gets the id of this ContaResponse.
        {{{conta_response_id_value}}}

        :return: The id of this ContaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContaResponse.
        {{{conta_response_id_value}}}

        :param id: The id of this ContaResponse.
        :type: int
        """
        self._id = id

    @property
    def id_produto(self):
        """
        Gets the id_produto of this ContaResponse.
        {{{conta_response_id_produto_value}}}

        :return: The id_produto of this ContaResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this ContaResponse.
        {{{conta_response_id_produto_value}}}

        :param id_produto: The id_produto of this ContaResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def id_origem_comercial(self):
        """
        Gets the id_origem_comercial of this ContaResponse.
        {{{conta_response_id_origem_comercial_value}}}

        :return: The id_origem_comercial of this ContaResponse.
        :rtype: int
        """
        return self._id_origem_comercial

    @id_origem_comercial.setter
    def id_origem_comercial(self, id_origem_comercial):
        """
        Sets the id_origem_comercial of this ContaResponse.
        {{{conta_response_id_origem_comercial_value}}}

        :param id_origem_comercial: The id_origem_comercial of this ContaResponse.
        :type: int
        """
        self._id_origem_comercial = id_origem_comercial

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this ContaResponse.
        {{{conta_response_id_pessoa_value}}}

        :return: The id_pessoa of this ContaResponse.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this ContaResponse.
        {{{conta_response_id_pessoa_value}}}

        :param id_pessoa: The id_pessoa of this ContaResponse.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_status_conta(self):
        """
        Gets the id_status_conta of this ContaResponse.
        {{{conta_response_id_status_conta_value}}}

        :return: The id_status_conta of this ContaResponse.
        :rtype: int
        """
        return self._id_status_conta

    @id_status_conta.setter
    def id_status_conta(self, id_status_conta):
        """
        Sets the id_status_conta of this ContaResponse.
        {{{conta_response_id_status_conta_value}}}

        :param id_status_conta: The id_status_conta of this ContaResponse.
        :type: int
        """
        self._id_status_conta = id_status_conta

    @property
    def dia_vencimento(self):
        """
        Gets the dia_vencimento of this ContaResponse.
        {{{conta_response_dia_vencimento_value}}}

        :return: The dia_vencimento of this ContaResponse.
        :rtype: int
        """
        return self._dia_vencimento

    @dia_vencimento.setter
    def dia_vencimento(self, dia_vencimento):
        """
        Sets the dia_vencimento of this ContaResponse.
        {{{conta_response_dia_vencimento_value}}}

        :param dia_vencimento: The dia_vencimento of this ContaResponse.
        :type: int
        """
        self._dia_vencimento = dia_vencimento

    @property
    def melhor_dia_compra(self):
        """
        Gets the melhor_dia_compra of this ContaResponse.
        {{{conta_response_melhor_dia_compra_value}}}

        :return: The melhor_dia_compra of this ContaResponse.
        :rtype: int
        """
        return self._melhor_dia_compra

    @melhor_dia_compra.setter
    def melhor_dia_compra(self, melhor_dia_compra):
        """
        Sets the melhor_dia_compra of this ContaResponse.
        {{{conta_response_melhor_dia_compra_value}}}

        :param melhor_dia_compra: The melhor_dia_compra of this ContaResponse.
        :type: int
        """
        self._melhor_dia_compra = melhor_dia_compra

    @property
    def data_status_conta(self):
        """
        Gets the data_status_conta of this ContaResponse.
        {{{conta_response_data_status_conta_value}}}

        :return: The data_status_conta of this ContaResponse.
        :rtype: str
        """
        return self._data_status_conta

    @data_status_conta.setter
    def data_status_conta(self, data_status_conta):
        """
        Sets the data_status_conta of this ContaResponse.
        {{{conta_response_data_status_conta_value}}}

        :param data_status_conta: The data_status_conta of this ContaResponse.
        :type: str
        """
        self._data_status_conta = data_status_conta

    @property
    def data_cadastro(self):
        """
        Gets the data_cadastro of this ContaResponse.
        {{{conta_response_data_cadastro_value}}}

        :return: The data_cadastro of this ContaResponse.
        :rtype: str
        """
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        """
        Sets the data_cadastro of this ContaResponse.
        {{{conta_response_data_cadastro_value}}}

        :param data_cadastro: The data_cadastro of this ContaResponse.
        :type: str
        """
        self._data_cadastro = data_cadastro

    @property
    def data_ultima_alteracao_vencimento(self):
        """
        Gets the data_ultima_alteracao_vencimento of this ContaResponse.
        {{{conta_response_data_ultima_alteracao_vencimento_value}}}

        :return: The data_ultima_alteracao_vencimento of this ContaResponse.
        :rtype: str
        """
        return self._data_ultima_alteracao_vencimento

    @data_ultima_alteracao_vencimento.setter
    def data_ultima_alteracao_vencimento(self, data_ultima_alteracao_vencimento):
        """
        Sets the data_ultima_alteracao_vencimento of this ContaResponse.
        {{{conta_response_data_ultima_alteracao_vencimento_value}}}

        :param data_ultima_alteracao_vencimento: The data_ultima_alteracao_vencimento of this ContaResponse.
        :type: str
        """
        self._data_ultima_alteracao_vencimento = data_ultima_alteracao_vencimento

    @property
    def valor_renda(self):
        """
        Gets the valor_renda of this ContaResponse.
        {{{conta_response_valor_renda_value}}}

        :return: The valor_renda of this ContaResponse.
        :rtype: float
        """
        return self._valor_renda

    @valor_renda.setter
    def valor_renda(self, valor_renda):
        """
        Sets the valor_renda of this ContaResponse.
        {{{conta_response_valor_renda_value}}}

        :param valor_renda: The valor_renda of this ContaResponse.
        :type: float
        """
        self._valor_renda = valor_renda

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

