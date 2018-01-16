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


class PessoaJuridicaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PessoaJuridicaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'razao_social': 'str',
            'cnpj': 'str',
            'inscricao_estadual': 'str',
            'contato': 'str',
            'banco': 'int',
            'agencia': 'int',
            'digito_verificador_agencia': 'str',
            'conta_corrente': 'str',
            'digito_verificador_conta_corrente': 'str',
            'usuario': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'razao_social': 'razaoSocial',
            'cnpj': 'cnpj',
            'inscricao_estadual': 'inscricaoEstadual',
            'contato': 'contato',
            'banco': 'banco',
            'agencia': 'agencia',
            'digito_verificador_agencia': 'digitoVerificadorAgencia',
            'conta_corrente': 'contaCorrente',
            'digito_verificador_conta_corrente': 'digitoVerificadorContaCorrente',
            'usuario': 'usuario'
        }

        self._id = None
        self._razao_social = None
        self._cnpj = None
        self._inscricao_estadual = None
        self._contato = None
        self._banco = None
        self._agencia = None
        self._digito_verificador_agencia = None
        self._conta_corrente = None
        self._digito_verificador_conta_corrente = None
        self._usuario = None

    @property
    def id(self):
        """
        Gets the id of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo identificador da pessoa jur\u00C3\u00ADdica

        :return: The id of this PessoaJuridicaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo identificador da pessoa jur\u00C3\u00ADdica

        :param id: The id of this PessoaJuridicaResponse.
        :type: int
        """
        self._id = id

    @property
    def razao_social(self):
        """
        Gets the razao_social of this PessoaJuridicaResponse.
        Raz\u00C3\u00A3o social da pessoa jur\u00C3\u00ADdica

        :return: The razao_social of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        """
        Sets the razao_social of this PessoaJuridicaResponse.
        Raz\u00C3\u00A3o social da pessoa jur\u00C3\u00ADdica

        :param razao_social: The razao_social of this PessoaJuridicaResponse.
        :type: str
        """
        self._razao_social = razao_social

    @property
    def cnpj(self):
        """
        Gets the cnpj of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo do Cadastro Nacional de Pessoas Jur\u00C3\u00ADdicas

        :return: The cnpj of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        """
        Sets the cnpj of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo do Cadastro Nacional de Pessoas Jur\u00C3\u00ADdicas

        :param cnpj: The cnpj of this PessoaJuridicaResponse.
        :type: str
        """
        self._cnpj = cnpj

    @property
    def inscricao_estadual(self):
        """
        Gets the inscricao_estadual of this PessoaJuridicaResponse.
        N\u00C3\u00BAmero da inscri\u00C3\u00A7\u00C3\u00A3o estadual

        :return: The inscricao_estadual of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._inscricao_estadual

    @inscricao_estadual.setter
    def inscricao_estadual(self, inscricao_estadual):
        """
        Sets the inscricao_estadual of this PessoaJuridicaResponse.
        N\u00C3\u00BAmero da inscri\u00C3\u00A7\u00C3\u00A3o estadual

        :param inscricao_estadual: The inscricao_estadual of this PessoaJuridicaResponse.
        :type: str
        """
        self._inscricao_estadual = inscricao_estadual

    @property
    def contato(self):
        """
        Gets the contato of this PessoaJuridicaResponse.
        Nome da pessoa para entrar em contato

        :return: The contato of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._contato

    @contato.setter
    def contato(self, contato):
        """
        Sets the contato of this PessoaJuridicaResponse.
        Nome da pessoa para entrar em contato

        :param contato: The contato of this PessoaJuridicaResponse.
        :type: str
        """
        self._contato = contato

    @property
    def banco(self):
        """
        Gets the banco of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo do banco

        :return: The banco of this PessoaJuridicaResponse.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo do banco

        :param banco: The banco of this PessoaJuridicaResponse.
        :type: int
        """
        self._banco = banco

    @property
    def agencia(self):
        """
        Gets the agencia of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo da ag\u00C3\u00AAncia

        :return: The agencia of this PessoaJuridicaResponse.
        :rtype: int
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        """
        Sets the agencia of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo da ag\u00C3\u00AAncia

        :param agencia: The agencia of this PessoaJuridicaResponse.
        :type: int
        """
        self._agencia = agencia

    @property
    def digito_verificador_agencia(self):
        """
        Gets the digito_verificador_agencia of this PessoaJuridicaResponse.
        D\u00C3\u00ADgito verificador da ag\u00C3\u00AAncia

        :return: The digito_verificador_agencia of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._digito_verificador_agencia

    @digito_verificador_agencia.setter
    def digito_verificador_agencia(self, digito_verificador_agencia):
        """
        Sets the digito_verificador_agencia of this PessoaJuridicaResponse.
        D\u00C3\u00ADgito verificador da ag\u00C3\u00AAncia

        :param digito_verificador_agencia: The digito_verificador_agencia of this PessoaJuridicaResponse.
        :type: str
        """
        self._digito_verificador_agencia = digito_verificador_agencia

    @property
    def conta_corrente(self):
        """
        Gets the conta_corrente of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo da Conta Corrente

        :return: The conta_corrente of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        """
        Sets the conta_corrente of this PessoaJuridicaResponse.
        C\u00C3\u00B3digo da Conta Corrente

        :param conta_corrente: The conta_corrente of this PessoaJuridicaResponse.
        :type: str
        """
        self._conta_corrente = conta_corrente

    @property
    def digito_verificador_conta_corrente(self):
        """
        Gets the digito_verificador_conta_corrente of this PessoaJuridicaResponse.
        D\u00C3\u00ADgito Verificador da Conta Corrente

        :return: The digito_verificador_conta_corrente of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._digito_verificador_conta_corrente

    @digito_verificador_conta_corrente.setter
    def digito_verificador_conta_corrente(self, digito_verificador_conta_corrente):
        """
        Sets the digito_verificador_conta_corrente of this PessoaJuridicaResponse.
        D\u00C3\u00ADgito Verificador da Conta Corrente

        :param digito_verificador_conta_corrente: The digito_verificador_conta_corrente of this PessoaJuridicaResponse.
        :type: str
        """
        self._digito_verificador_conta_corrente = digito_verificador_conta_corrente

    @property
    def usuario(self):
        """
        Gets the usuario of this PessoaJuridicaResponse.
        Login do usu\u00C3\u00A1rio para registro da inser\u00C3\u00A7\u00C3\u00A3o

        :return: The usuario of this PessoaJuridicaResponse.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this PessoaJuridicaResponse.
        Login do usu\u00C3\u00A1rio para registro da inser\u00C3\u00A7\u00C3\u00A3o

        :param usuario: The usuario of this PessoaJuridicaResponse.
        :type: str
        """
        self._usuario = usuario

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
