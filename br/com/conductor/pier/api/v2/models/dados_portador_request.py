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


class DadosPortadorRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DadosPortadorRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cartao': 'str',
            'cpf': 'str',
            'nome': 'str',
            'data_nascimento': 'str',
            'cep_residencial': 'str',
            'email': 'str',
            'ddd': 'str',
            'telefone': 'str'
        }

        self.attribute_map = {
            'cartao': 'cartao',
            'cpf': 'cpf',
            'nome': 'nome',
            'data_nascimento': 'dataNascimento',
            'cep_residencial': 'cepResidencial',
            'email': 'email',
            'ddd': 'ddd',
            'telefone': 'telefone'
        }

        self._cartao = None
        self._cpf = None
        self._nome = None
        self._data_nascimento = None
        self._cep_residencial = None
        self._email = None
        self._ddd = None
        self._telefone = None

    @property
    def cartao(self):
        """
        Gets the cartao of this DadosPortadorRequest.
        {{{dados_portador_request_cartao_value}}}

        :return: The cartao of this DadosPortadorRequest.
        :rtype: str
        """
        return self._cartao

    @cartao.setter
    def cartao(self, cartao):
        """
        Sets the cartao of this DadosPortadorRequest.
        {{{dados_portador_request_cartao_value}}}

        :param cartao: The cartao of this DadosPortadorRequest.
        :type: str
        """
        self._cartao = cartao

    @property
    def cpf(self):
        """
        Gets the cpf of this DadosPortadorRequest.
        {{{dados_portador_request_cpf_value}}}

        :return: The cpf of this DadosPortadorRequest.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this DadosPortadorRequest.
        {{{dados_portador_request_cpf_value}}}

        :param cpf: The cpf of this DadosPortadorRequest.
        :type: str
        """
        self._cpf = cpf

    @property
    def nome(self):
        """
        Gets the nome of this DadosPortadorRequest.
        {{{dados_portador_request_nome_value}}}

        :return: The nome of this DadosPortadorRequest.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this DadosPortadorRequest.
        {{{dados_portador_request_nome_value}}}

        :param nome: The nome of this DadosPortadorRequest.
        :type: str
        """
        self._nome = nome

    @property
    def data_nascimento(self):
        """
        Gets the data_nascimento of this DadosPortadorRequest.
        {{{dados_portador_request_data_nascimento_value}}}

        :return: The data_nascimento of this DadosPortadorRequest.
        :rtype: str
        """
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        """
        Sets the data_nascimento of this DadosPortadorRequest.
        {{{dados_portador_request_data_nascimento_value}}}

        :param data_nascimento: The data_nascimento of this DadosPortadorRequest.
        :type: str
        """
        self._data_nascimento = data_nascimento

    @property
    def cep_residencial(self):
        """
        Gets the cep_residencial of this DadosPortadorRequest.
        {{{dados_portador_request_cep_residencial_value}}}

        :return: The cep_residencial of this DadosPortadorRequest.
        :rtype: str
        """
        return self._cep_residencial

    @cep_residencial.setter
    def cep_residencial(self, cep_residencial):
        """
        Sets the cep_residencial of this DadosPortadorRequest.
        {{{dados_portador_request_cep_residencial_value}}}

        :param cep_residencial: The cep_residencial of this DadosPortadorRequest.
        :type: str
        """
        self._cep_residencial = cep_residencial

    @property
    def email(self):
        """
        Gets the email of this DadosPortadorRequest.
        {{{dados_portador_request_email_value}}}

        :return: The email of this DadosPortadorRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this DadosPortadorRequest.
        {{{dados_portador_request_email_value}}}

        :param email: The email of this DadosPortadorRequest.
        :type: str
        """
        self._email = email

    @property
    def ddd(self):
        """
        Gets the ddd of this DadosPortadorRequest.
        {{{dados_portador_request_ddd_value}}}

        :return: The ddd of this DadosPortadorRequest.
        :rtype: str
        """
        return self._ddd

    @ddd.setter
    def ddd(self, ddd):
        """
        Sets the ddd of this DadosPortadorRequest.
        {{{dados_portador_request_ddd_value}}}

        :param ddd: The ddd of this DadosPortadorRequest.
        :type: str
        """
        self._ddd = ddd

    @property
    def telefone(self):
        """
        Gets the telefone of this DadosPortadorRequest.
        {{{dados_portador_request_telefone_value}}}

        :return: The telefone of this DadosPortadorRequest.
        :rtype: str
        """
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        """
        Sets the telefone of this DadosPortadorRequest.
        {{{dados_portador_request_telefone_value}}}

        :param telefone: The telefone of this DadosPortadorRequest.
        :type: str
        """
        self._telefone = telefone

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
