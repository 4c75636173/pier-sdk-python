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


class OperacaoCredorPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OperacaoCredorPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_operacao': 'int',
            'id_credor': 'int',
            'ids_produto': 'list[int]',
            'remuneracao_percentual': 'float',
            'remuneracao_fixa': 'float',
            'periodicidade': 'str',
            'vencimento_primeira_parcela': 'int',
            'dias_afastamento': 'int',
            'fator_multiplicador': 'str',
            'flag_taxa_fixada': 'bool',
            'plano_minimo': 'int',
            'plano_maximo': 'int'
        }

        self.attribute_map = {
            'id_operacao': 'idOperacao',
            'id_credor': 'idCredor',
            'ids_produto': 'idsProduto',
            'remuneracao_percentual': 'remuneracaoPercentual',
            'remuneracao_fixa': 'remuneracaoFixa',
            'periodicidade': 'periodicidade',
            'vencimento_primeira_parcela': 'vencimentoPrimeiraParcela',
            'dias_afastamento': 'diasAfastamento',
            'fator_multiplicador': 'fatorMultiplicador',
            'flag_taxa_fixada': 'flagTaxaFixada',
            'plano_minimo': 'planoMinimo',
            'plano_maximo': 'planoMaximo'
        }

        self._id_operacao = None
        self._id_credor = None
        self._ids_produto = None
        self._remuneracao_percentual = None
        self._remuneracao_fixa = None
        self._periodicidade = None
        self._vencimento_primeira_parcela = None
        self._dias_afastamento = None
        self._fator_multiplicador = None
        self._flag_taxa_fixada = None
        self._plano_minimo = None
        self._plano_maximo = None

    @property
    def id_operacao(self):
        """
        Gets the id_operacao of this OperacaoCredorPersist.
        Apresenta o id da Opera\u00E7\u00E3o.

        :return: The id_operacao of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._id_operacao

    @id_operacao.setter
    def id_operacao(self, id_operacao):
        """
        Sets the id_operacao of this OperacaoCredorPersist.
        Apresenta o id da Opera\u00E7\u00E3o.

        :param id_operacao: The id_operacao of this OperacaoCredorPersist.
        :type: int
        """
        self._id_operacao = id_operacao

    @property
    def id_credor(self):
        """
        Gets the id_credor of this OperacaoCredorPersist.
        Apresenta o id do Credor.

        :return: The id_credor of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._id_credor

    @id_credor.setter
    def id_credor(self, id_credor):
        """
        Sets the id_credor of this OperacaoCredorPersist.
        Apresenta o id do Credor.

        :param id_credor: The id_credor of this OperacaoCredorPersist.
        :type: int
        """
        self._id_credor = id_credor

    @property
    def ids_produto(self):
        """
        Gets the ids_produto of this OperacaoCredorPersist.
        Apresenta a lista de ids produtos que v\u00E3o ter regras cadastradas.

        :return: The ids_produto of this OperacaoCredorPersist.
        :rtype: list[int]
        """
        return self._ids_produto

    @ids_produto.setter
    def ids_produto(self, ids_produto):
        """
        Sets the ids_produto of this OperacaoCredorPersist.
        Apresenta a lista de ids produtos que v\u00E3o ter regras cadastradas.

        :param ids_produto: The ids_produto of this OperacaoCredorPersist.
        :type: list[int]
        """
        self._ids_produto = ids_produto

    @property
    def remuneracao_percentual(self):
        """
        Gets the remuneracao_percentual of this OperacaoCredorPersist.
        Remunera\u00E7\u00E3o Percentual.

        :return: The remuneracao_percentual of this OperacaoCredorPersist.
        :rtype: float
        """
        return self._remuneracao_percentual

    @remuneracao_percentual.setter
    def remuneracao_percentual(self, remuneracao_percentual):
        """
        Sets the remuneracao_percentual of this OperacaoCredorPersist.
        Remunera\u00E7\u00E3o Percentual.

        :param remuneracao_percentual: The remuneracao_percentual of this OperacaoCredorPersist.
        :type: float
        """
        self._remuneracao_percentual = remuneracao_percentual

    @property
    def remuneracao_fixa(self):
        """
        Gets the remuneracao_fixa of this OperacaoCredorPersist.
        Remunera\u00E7\u00E3o Fixa.

        :return: The remuneracao_fixa of this OperacaoCredorPersist.
        :rtype: float
        """
        return self._remuneracao_fixa

    @remuneracao_fixa.setter
    def remuneracao_fixa(self, remuneracao_fixa):
        """
        Sets the remuneracao_fixa of this OperacaoCredorPersist.
        Remunera\u00E7\u00E3o Fixa.

        :param remuneracao_fixa: The remuneracao_fixa of this OperacaoCredorPersist.
        :type: float
        """
        self._remuneracao_fixa = remuneracao_fixa

    @property
    def periodicidade(self):
        """
        Gets the periodicidade of this OperacaoCredorPersist.
        Periodicidade (DIARIO(1), SEMANAL(2), MENSAL(3), DECENDIAL(4), QUINZENAL(5)).

        :return: The periodicidade of this OperacaoCredorPersist.
        :rtype: str
        """
        return self._periodicidade

    @periodicidade.setter
    def periodicidade(self, periodicidade):
        """
        Sets the periodicidade of this OperacaoCredorPersist.
        Periodicidade (DIARIO(1), SEMANAL(2), MENSAL(3), DECENDIAL(4), QUINZENAL(5)).

        :param periodicidade: The periodicidade of this OperacaoCredorPersist.
        :type: str
        """
        allowed_values = ["DIARIO", "SEMANAL", "MENSAL", "DECENDIAL", "QUINZENAL"]
        if periodicidade not in allowed_values:
            raise ValueError(
                "Invalid value for `periodicidade`, must be one of {0}"
                .format(allowed_values)
            )
        self._periodicidade = periodicidade

    @property
    def vencimento_primeira_parcela(self):
        """
        Gets the vencimento_primeira_parcela of this OperacaoCredorPersist.
        Vencimento da primeira parcela.

        :return: The vencimento_primeira_parcela of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._vencimento_primeira_parcela

    @vencimento_primeira_parcela.setter
    def vencimento_primeira_parcela(self, vencimento_primeira_parcela):
        """
        Sets the vencimento_primeira_parcela of this OperacaoCredorPersist.
        Vencimento da primeira parcela.

        :param vencimento_primeira_parcela: The vencimento_primeira_parcela of this OperacaoCredorPersist.
        :type: int
        """
        self._vencimento_primeira_parcela = vencimento_primeira_parcela

    @property
    def dias_afastamento(self):
        """
        Gets the dias_afastamento of this OperacaoCredorPersist.
        Dias afastamento.

        :return: The dias_afastamento of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._dias_afastamento

    @dias_afastamento.setter
    def dias_afastamento(self, dias_afastamento):
        """
        Sets the dias_afastamento of this OperacaoCredorPersist.
        Dias afastamento.

        :param dias_afastamento: The dias_afastamento of this OperacaoCredorPersist.
        :type: int
        """
        self._dias_afastamento = dias_afastamento

    @property
    def fator_multiplicador(self):
        """
        Gets the fator_multiplicador of this OperacaoCredorPersist.
        Fator multiplicador (FORA_AGENDA(0), AGENDA(1)).

        :return: The fator_multiplicador of this OperacaoCredorPersist.
        :rtype: str
        """
        return self._fator_multiplicador

    @fator_multiplicador.setter
    def fator_multiplicador(self, fator_multiplicador):
        """
        Sets the fator_multiplicador of this OperacaoCredorPersist.
        Fator multiplicador (FORA_AGENDA(0), AGENDA(1)).

        :param fator_multiplicador: The fator_multiplicador of this OperacaoCredorPersist.
        :type: str
        """
        allowed_values = ["FORA_AGENDA", "AGENDA", "AGENDA_NEGATIVA"]
        if fator_multiplicador not in allowed_values:
            raise ValueError(
                "Invalid value for `fator_multiplicador`, must be one of {0}"
                .format(allowed_values)
            )
        self._fator_multiplicador = fator_multiplicador

    @property
    def flag_taxa_fixada(self):
        """
        Gets the flag_taxa_fixada of this OperacaoCredorPersist.
        Flag taxa fixada.

        :return: The flag_taxa_fixada of this OperacaoCredorPersist.
        :rtype: bool
        """
        return self._flag_taxa_fixada

    @flag_taxa_fixada.setter
    def flag_taxa_fixada(self, flag_taxa_fixada):
        """
        Sets the flag_taxa_fixada of this OperacaoCredorPersist.
        Flag taxa fixada.

        :param flag_taxa_fixada: The flag_taxa_fixada of this OperacaoCredorPersist.
        :type: bool
        """
        self._flag_taxa_fixada = flag_taxa_fixada

    @property
    def plano_minimo(self):
        """
        Gets the plano_minimo of this OperacaoCredorPersist.
        Plano m\u00EDnimo da regra.

        :return: The plano_minimo of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._plano_minimo

    @plano_minimo.setter
    def plano_minimo(self, plano_minimo):
        """
        Sets the plano_minimo of this OperacaoCredorPersist.
        Plano m\u00EDnimo da regra.

        :param plano_minimo: The plano_minimo of this OperacaoCredorPersist.
        :type: int
        """
        self._plano_minimo = plano_minimo

    @property
    def plano_maximo(self):
        """
        Gets the plano_maximo of this OperacaoCredorPersist.
        Plano m\u00E1ximo da regra.

        :return: The plano_maximo of this OperacaoCredorPersist.
        :rtype: int
        """
        return self._plano_maximo

    @plano_maximo.setter
    def plano_maximo(self, plano_maximo):
        """
        Sets the plano_maximo of this OperacaoCredorPersist.
        Plano m\u00E1ximo da regra.

        :param plano_maximo: The plano_maximo of this OperacaoCredorPersist.
        :type: int
        """
        self._plano_maximo = plano_maximo

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

