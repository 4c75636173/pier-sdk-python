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


class EmprestimoPessoalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EmprestimoPessoalResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'planos_parcelamentos': 'list[PlanoParcelamentoEmprestimoResponse]',
            'valor_solicitado': 'float',
            'valor_maximo_solicitacao': 'float',
            'numero_parcelas': 'int',
            'valor_maximo_parcela': 'float',
            'data_primeira_parcela': 'str',
            'periodo_taxa': 'str',
            'sistema_amortizacao': 'str',
            'taxa_juros': 'float'
        }

        self.attribute_map = {
            'planos_parcelamentos': 'planosParcelamentos',
            'valor_solicitado': 'valorSolicitado',
            'valor_maximo_solicitacao': 'valorMaximoSolicitacao',
            'numero_parcelas': 'numeroParcelas',
            'valor_maximo_parcela': 'valorMaximoParcela',
            'data_primeira_parcela': 'dataPrimeiraParcela',
            'periodo_taxa': 'periodoTaxa',
            'sistema_amortizacao': 'sistemaAmortizacao',
            'taxa_juros': 'taxaJuros'
        }

        self._planos_parcelamentos = None
        self._valor_solicitado = None
        self._valor_maximo_solicitacao = None
        self._numero_parcelas = None
        self._valor_maximo_parcela = None
        self._data_primeira_parcela = None
        self._periodo_taxa = None
        self._sistema_amortizacao = None
        self._taxa_juros = None

    @property
    def planos_parcelamentos(self):
        """
        Gets the planos_parcelamentos of this EmprestimoPessoalResponse.


        :return: The planos_parcelamentos of this EmprestimoPessoalResponse.
        :rtype: list[PlanoParcelamentoEmprestimoResponse]
        """
        return self._planos_parcelamentos

    @planos_parcelamentos.setter
    def planos_parcelamentos(self, planos_parcelamentos):
        """
        Sets the planos_parcelamentos of this EmprestimoPessoalResponse.


        :param planos_parcelamentos: The planos_parcelamentos of this EmprestimoPessoalResponse.
        :type: list[PlanoParcelamentoEmprestimoResponse]
        """
        self._planos_parcelamentos = planos_parcelamentos

    @property
    def valor_solicitado(self):
        """
        Gets the valor_solicitado of this EmprestimoPessoalResponse.
        Valor solicitado do empr\u00E9stimo/financiamento

        :return: The valor_solicitado of this EmprestimoPessoalResponse.
        :rtype: float
        """
        return self._valor_solicitado

    @valor_solicitado.setter
    def valor_solicitado(self, valor_solicitado):
        """
        Sets the valor_solicitado of this EmprestimoPessoalResponse.
        Valor solicitado do empr\u00E9stimo/financiamento

        :param valor_solicitado: The valor_solicitado of this EmprestimoPessoalResponse.
        :type: float
        """
        self._valor_solicitado = valor_solicitado

    @property
    def valor_maximo_solicitacao(self):
        """
        Gets the valor_maximo_solicitacao of this EmprestimoPessoalResponse.
        Valor m\u00E1ximo de empr\u00E9stimo pelo valor limite de parcela

        :return: The valor_maximo_solicitacao of this EmprestimoPessoalResponse.
        :rtype: float
        """
        return self._valor_maximo_solicitacao

    @valor_maximo_solicitacao.setter
    def valor_maximo_solicitacao(self, valor_maximo_solicitacao):
        """
        Sets the valor_maximo_solicitacao of this EmprestimoPessoalResponse.
        Valor m\u00E1ximo de empr\u00E9stimo pelo valor limite de parcela

        :param valor_maximo_solicitacao: The valor_maximo_solicitacao of this EmprestimoPessoalResponse.
        :type: float
        """
        self._valor_maximo_solicitacao = valor_maximo_solicitacao

    @property
    def numero_parcelas(self):
        """
        Gets the numero_parcelas of this EmprestimoPessoalResponse.
        N\u00FAmero de parcelas solicitado

        :return: The numero_parcelas of this EmprestimoPessoalResponse.
        :rtype: int
        """
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas):
        """
        Sets the numero_parcelas of this EmprestimoPessoalResponse.
        N\u00FAmero de parcelas solicitado

        :param numero_parcelas: The numero_parcelas of this EmprestimoPessoalResponse.
        :type: int
        """
        self._numero_parcelas = numero_parcelas

    @property
    def valor_maximo_parcela(self):
        """
        Gets the valor_maximo_parcela of this EmprestimoPessoalResponse.
        Limite m\u00E1ximo de parcela permitido

        :return: The valor_maximo_parcela of this EmprestimoPessoalResponse.
        :rtype: float
        """
        return self._valor_maximo_parcela

    @valor_maximo_parcela.setter
    def valor_maximo_parcela(self, valor_maximo_parcela):
        """
        Sets the valor_maximo_parcela of this EmprestimoPessoalResponse.
        Limite m\u00E1ximo de parcela permitido

        :param valor_maximo_parcela: The valor_maximo_parcela of this EmprestimoPessoalResponse.
        :type: float
        """
        self._valor_maximo_parcela = valor_maximo_parcela

    @property
    def data_primeira_parcela(self):
        """
        Gets the data_primeira_parcela of this EmprestimoPessoalResponse.
        Data do desconto da primeira parcela

        :return: The data_primeira_parcela of this EmprestimoPessoalResponse.
        :rtype: str
        """
        return self._data_primeira_parcela

    @data_primeira_parcela.setter
    def data_primeira_parcela(self, data_primeira_parcela):
        """
        Sets the data_primeira_parcela of this EmprestimoPessoalResponse.
        Data do desconto da primeira parcela

        :param data_primeira_parcela: The data_primeira_parcela of this EmprestimoPessoalResponse.
        :type: str
        """
        self._data_primeira_parcela = data_primeira_parcela

    @property
    def periodo_taxa(self):
        """
        Gets the periodo_taxa of this EmprestimoPessoalResponse.
        Per\u00EDodo de aplica da taxa de juros

        :return: The periodo_taxa of this EmprestimoPessoalResponse.
        :rtype: str
        """
        return self._periodo_taxa

    @periodo_taxa.setter
    def periodo_taxa(self, periodo_taxa):
        """
        Sets the periodo_taxa of this EmprestimoPessoalResponse.
        Per\u00EDodo de aplica da taxa de juros

        :param periodo_taxa: The periodo_taxa of this EmprestimoPessoalResponse.
        :type: str
        """
        self._periodo_taxa = periodo_taxa

    @property
    def sistema_amortizacao(self):
        """
        Gets the sistema_amortizacao of this EmprestimoPessoalResponse.
        Sistema para amortiza\u00E7\u00E3o do valor das parcelas

        :return: The sistema_amortizacao of this EmprestimoPessoalResponse.
        :rtype: str
        """
        return self._sistema_amortizacao

    @sistema_amortizacao.setter
    def sistema_amortizacao(self, sistema_amortizacao):
        """
        Sets the sistema_amortizacao of this EmprestimoPessoalResponse.
        Sistema para amortiza\u00E7\u00E3o do valor das parcelas

        :param sistema_amortizacao: The sistema_amortizacao of this EmprestimoPessoalResponse.
        :type: str
        """
        self._sistema_amortizacao = sistema_amortizacao

    @property
    def taxa_juros(self):
        """
        Gets the taxa_juros of this EmprestimoPessoalResponse.
        Valor percentual da taxa de juros a ser aplicada

        :return: The taxa_juros of this EmprestimoPessoalResponse.
        :rtype: float
        """
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        """
        Sets the taxa_juros of this EmprestimoPessoalResponse.
        Valor percentual da taxa de juros a ser aplicada

        :param taxa_juros: The taxa_juros of this EmprestimoPessoalResponse.
        :type: float
        """
        self._taxa_juros = taxa_juros

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

