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


class PlanoParcelamentoEmprestimoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PlanoParcelamentoEmprestimoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'numero_parcelas': 'int',
            'valor_parcelas': 'float',
            'taxa_juros': 'float',
            'valor_tributos_iof': 'float',
            'valor_percentual_cet': 'float'
        }

        self.attribute_map = {
            'numero_parcelas': 'numeroParcelas',
            'valor_parcelas': 'valorParcelas',
            'taxa_juros': 'taxaJuros',
            'valor_tributos_iof': 'valorTributosIOF',
            'valor_percentual_cet': 'valorPercentualCET'
        }

        self._numero_parcelas = None
        self._valor_parcelas = None
        self._taxa_juros = None
        self._valor_tributos_iof = None
        self._valor_percentual_cet = None

    @property
    def numero_parcelas(self):
        """
        Gets the numero_parcelas of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_numero_parcelas_value}}}

        :return: The numero_parcelas of this PlanoParcelamentoEmprestimoResponse.
        :rtype: int
        """
        return self._numero_parcelas

    @numero_parcelas.setter
    def numero_parcelas(self, numero_parcelas):
        """
        Sets the numero_parcelas of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_numero_parcelas_value}}}

        :param numero_parcelas: The numero_parcelas of this PlanoParcelamentoEmprestimoResponse.
        :type: int
        """
        self._numero_parcelas = numero_parcelas

    @property
    def valor_parcelas(self):
        """
        Gets the valor_parcelas of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_parcelas_value}}}

        :return: The valor_parcelas of this PlanoParcelamentoEmprestimoResponse.
        :rtype: float
        """
        return self._valor_parcelas

    @valor_parcelas.setter
    def valor_parcelas(self, valor_parcelas):
        """
        Sets the valor_parcelas of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_parcelas_value}}}

        :param valor_parcelas: The valor_parcelas of this PlanoParcelamentoEmprestimoResponse.
        :type: float
        """
        self._valor_parcelas = valor_parcelas

    @property
    def taxa_juros(self):
        """
        Gets the taxa_juros of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_taxa_juros_value}}}

        :return: The taxa_juros of this PlanoParcelamentoEmprestimoResponse.
        :rtype: float
        """
        return self._taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        """
        Sets the taxa_juros of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_taxa_juros_value}}}

        :param taxa_juros: The taxa_juros of this PlanoParcelamentoEmprestimoResponse.
        :type: float
        """
        self._taxa_juros = taxa_juros

    @property
    def valor_tributos_iof(self):
        """
        Gets the valor_tributos_iof of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_tributos_i_o_f_value}}}

        :return: The valor_tributos_iof of this PlanoParcelamentoEmprestimoResponse.
        :rtype: float
        """
        return self._valor_tributos_iof

    @valor_tributos_iof.setter
    def valor_tributos_iof(self, valor_tributos_iof):
        """
        Sets the valor_tributos_iof of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_tributos_i_o_f_value}}}

        :param valor_tributos_iof: The valor_tributos_iof of this PlanoParcelamentoEmprestimoResponse.
        :type: float
        """
        self._valor_tributos_iof = valor_tributos_iof

    @property
    def valor_percentual_cet(self):
        """
        Gets the valor_percentual_cet of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_percentual_c_e_t_value}}}

        :return: The valor_percentual_cet of this PlanoParcelamentoEmprestimoResponse.
        :rtype: float
        """
        return self._valor_percentual_cet

    @valor_percentual_cet.setter
    def valor_percentual_cet(self, valor_percentual_cet):
        """
        Sets the valor_percentual_cet of this PlanoParcelamentoEmprestimoResponse.
        {{{plano_parcelamento_emprestimo_response_valor_percentual_c_e_t_value}}}

        :param valor_percentual_cet: The valor_percentual_cet of this PlanoParcelamentoEmprestimoResponse.
        :type: float
        """
        self._valor_percentual_cet = valor_percentual_cet

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

