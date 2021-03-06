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


class ContaBancariaPortadorPersistValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContaBancariaPortadorPersistValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_conta': 'int',
            'nome_agencia': 'str',
            'banco': 'int',
            'numero_agencia': 'str',
            'digito_agencia': 'str',
            'numero_conta': 'str',
            'digito_conta': 'str',
            'flag_ativo': 'int',
            'flag_conta_origem_doc': 'int',
            'id_pessoa_fisica': 'int',
            'flag_conta_poupanca': 'int',
            'favorecido': 'str',
            'numero_receira_federal': 'str',
            'titularidade': 'int'
        }

        self.attribute_map = {
            'id_conta': 'idConta',
            'nome_agencia': 'nomeAgencia',
            'banco': 'banco',
            'numero_agencia': 'numeroAgencia',
            'digito_agencia': 'digitoAgencia',
            'numero_conta': 'numeroConta',
            'digito_conta': 'digitoConta',
            'flag_ativo': 'flagAtivo',
            'flag_conta_origem_doc': 'flagContaOrigemDoc',
            'id_pessoa_fisica': 'idPessoaFisica',
            'flag_conta_poupanca': 'flagContaPoupanca',
            'favorecido': 'favorecido',
            'numero_receira_federal': 'numeroReceiraFederal',
            'titularidade': 'titularidade'
        }

        self._id_conta = None
        self._nome_agencia = None
        self._banco = None
        self._numero_agencia = None
        self._digito_agencia = None
        self._numero_conta = None
        self._digito_conta = None
        self._flag_ativo = None
        self._flag_conta_origem_doc = None
        self._id_pessoa_fisica = None
        self._flag_conta_poupanca = None
        self._favorecido = None
        self._numero_receira_federal = None
        self._titularidade = None

    @property
    def id_conta(self):
        """
        Gets the id_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_id_conta_value}}}

        :return: The id_conta of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_id_conta_value}}}

        :param id_conta: The id_conta of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def nome_agencia(self):
        """
        Gets the nome_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_nome_agencia_value}}}

        :return: The nome_agencia of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._nome_agencia

    @nome_agencia.setter
    def nome_agencia(self, nome_agencia):
        """
        Sets the nome_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_nome_agencia_value}}}

        :param nome_agencia: The nome_agencia of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._nome_agencia = nome_agencia

    @property
    def banco(self):
        """
        Gets the banco of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_banco_value}}}

        :return: The banco of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_banco_value}}}

        :param banco: The banco of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._banco = banco

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_agencia_value}}}

        :return: The numero_agencia of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_agencia_value}}}

        :param numero_agencia: The numero_agencia of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._numero_agencia = numero_agencia

    @property
    def digito_agencia(self):
        """
        Gets the digito_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_digito_agencia_value}}}

        :return: The digito_agencia of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._digito_agencia

    @digito_agencia.setter
    def digito_agencia(self, digito_agencia):
        """
        Sets the digito_agencia of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_digito_agencia_value}}}

        :param digito_agencia: The digito_agencia of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._digito_agencia = digito_agencia

    @property
    def numero_conta(self):
        """
        Gets the numero_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_conta_value}}}

        :return: The numero_conta of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        """
        Sets the numero_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_conta_value}}}

        :param numero_conta: The numero_conta of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._numero_conta = numero_conta

    @property
    def digito_conta(self):
        """
        Gets the digito_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_digito_conta_value}}}

        :return: The digito_conta of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._digito_conta

    @digito_conta.setter
    def digito_conta(self, digito_conta):
        """
        Sets the digito_conta of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_digito_conta_value}}}

        :param digito_conta: The digito_conta of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._digito_conta = digito_conta

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_ativo_value}}}

        :return: The flag_ativo of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_ativo_value}}}

        :param flag_ativo: The flag_ativo of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._flag_ativo = flag_ativo

    @property
    def flag_conta_origem_doc(self):
        """
        Gets the flag_conta_origem_doc of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_conta_origem_doc_value}}}

        :return: The flag_conta_origem_doc of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._flag_conta_origem_doc

    @flag_conta_origem_doc.setter
    def flag_conta_origem_doc(self, flag_conta_origem_doc):
        """
        Sets the flag_conta_origem_doc of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_conta_origem_doc_value}}}

        :param flag_conta_origem_doc: The flag_conta_origem_doc of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._flag_conta_origem_doc = flag_conta_origem_doc

    @property
    def id_pessoa_fisica(self):
        """
        Gets the id_pessoa_fisica of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_id_pessoa_fisica_value}}}

        :return: The id_pessoa_fisica of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._id_pessoa_fisica

    @id_pessoa_fisica.setter
    def id_pessoa_fisica(self, id_pessoa_fisica):
        """
        Sets the id_pessoa_fisica of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_id_pessoa_fisica_value}}}

        :param id_pessoa_fisica: The id_pessoa_fisica of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._id_pessoa_fisica = id_pessoa_fisica

    @property
    def flag_conta_poupanca(self):
        """
        Gets the flag_conta_poupanca of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_conta_poupanca_value}}}

        :return: The flag_conta_poupanca of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._flag_conta_poupanca

    @flag_conta_poupanca.setter
    def flag_conta_poupanca(self, flag_conta_poupanca):
        """
        Sets the flag_conta_poupanca of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_flag_conta_poupanca_value}}}

        :param flag_conta_poupanca: The flag_conta_poupanca of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._flag_conta_poupanca = flag_conta_poupanca

    @property
    def favorecido(self):
        """
        Gets the favorecido of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_favorecido_value}}}

        :return: The favorecido of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._favorecido

    @favorecido.setter
    def favorecido(self, favorecido):
        """
        Sets the favorecido of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_favorecido_value}}}

        :param favorecido: The favorecido of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._favorecido = favorecido

    @property
    def numero_receira_federal(self):
        """
        Gets the numero_receira_federal of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_receira_federal_value}}}

        :return: The numero_receira_federal of this ContaBancariaPortadorPersistValue.
        :rtype: str
        """
        return self._numero_receira_federal

    @numero_receira_federal.setter
    def numero_receira_federal(self, numero_receira_federal):
        """
        Sets the numero_receira_federal of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_numero_receira_federal_value}}}

        :param numero_receira_federal: The numero_receira_federal of this ContaBancariaPortadorPersistValue.
        :type: str
        """
        self._numero_receira_federal = numero_receira_federal

    @property
    def titularidade(self):
        """
        Gets the titularidade of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_titularidade_value}}}

        :return: The titularidade of this ContaBancariaPortadorPersistValue.
        :rtype: int
        """
        return self._titularidade

    @titularidade.setter
    def titularidade(self, titularidade):
        """
        Sets the titularidade of this ContaBancariaPortadorPersistValue.
        {{{conta_bancaria_portador_persist_titularidade_value}}}

        :param titularidade: The titularidade of this ContaBancariaPortadorPersistValue.
        :type: int
        """
        self._titularidade = titularidade

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

