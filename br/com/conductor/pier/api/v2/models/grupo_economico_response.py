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


class GrupoEconomicoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GrupoEconomicoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'razao_social': 'str',
            'nome_credor': 'str',
            'numero_receita_federal': 'str',
            'inscricao_estadual': 'str',
            'contato': 'str',
            'banco': 'int',
            'agencia': 'int',
            'digito_agencia': 'str',
            'conta_corrente': 'str',
            'digito_conta_corrente': 'str',
            'usuario': 'str',
            'periodicidade': 'str',
            'pagamento_semanal': 'str',
            'pagamento_mensal': 'int',
            'pagamento_decendial_primeiro': 'int',
            'pagamento_decendial_segundo': 'int',
            'pagamento_decendial_terceiro': 'int',
            'pagamento_quinzenal_primeiro': 'int',
            'pagamento_quinzenal_segundo': 'int',
            'id_credor_rav': 'int',
            'percentual_rav': 'float',
            'recebe_rav': 'str',
            'percentual_multiplica': 'float',
            'taxa_adm': 'float',
            'taxa_banco': 'float',
            'limite_rav': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'razao_social': 'razaoSocial',
            'nome_credor': 'nomeCredor',
            'numero_receita_federal': 'numeroReceitaFederal',
            'inscricao_estadual': 'inscricaoEstadual',
            'contato': 'contato',
            'banco': 'banco',
            'agencia': 'agencia',
            'digito_agencia': 'digitoAgencia',
            'conta_corrente': 'contaCorrente',
            'digito_conta_corrente': 'digitoContaCorrente',
            'usuario': 'usuario',
            'periodicidade': 'periodicidade',
            'pagamento_semanal': 'pagamentoSemanal',
            'pagamento_mensal': 'pagamentoMensal',
            'pagamento_decendial_primeiro': 'pagamentoDecendialPrimeiro',
            'pagamento_decendial_segundo': 'pagamentoDecendialSegundo',
            'pagamento_decendial_terceiro': 'pagamentoDecendialTerceiro',
            'pagamento_quinzenal_primeiro': 'pagamentoQuinzenalPrimeiro',
            'pagamento_quinzenal_segundo': 'pagamentoQuinzenalSegundo',
            'id_credor_rav': 'idCredorRAV',
            'percentual_rav': 'percentualRAV',
            'recebe_rav': 'recebeRAV',
            'percentual_multiplica': 'percentualMultiplica',
            'taxa_adm': 'taxaAdm',
            'taxa_banco': 'taxaBanco',
            'limite_rav': 'limiteRAV'
        }

        self._id = None
        self._razao_social = None
        self._nome_credor = None
        self._numero_receita_federal = None
        self._inscricao_estadual = None
        self._contato = None
        self._banco = None
        self._agencia = None
        self._digito_agencia = None
        self._conta_corrente = None
        self._digito_conta_corrente = None
        self._usuario = None
        self._periodicidade = None
        self._pagamento_semanal = None
        self._pagamento_mensal = None
        self._pagamento_decendial_primeiro = None
        self._pagamento_decendial_segundo = None
        self._pagamento_decendial_terceiro = None
        self._pagamento_quinzenal_primeiro = None
        self._pagamento_quinzenal_segundo = None
        self._id_credor_rav = None
        self._percentual_rav = None
        self._recebe_rav = None
        self._percentual_multiplica = None
        self._taxa_adm = None
        self._taxa_banco = None
        self._limite_rav = None

    @property
    def id(self):
        """
        Gets the id of this GrupoEconomicoResponse.
        {{{grupo_economico_response_id_value}}}

        :return: The id of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GrupoEconomicoResponse.
        {{{grupo_economico_response_id_value}}}

        :param id: The id of this GrupoEconomicoResponse.
        :type: int
        """
        self._id = id

    @property
    def razao_social(self):
        """
        Gets the razao_social of this GrupoEconomicoResponse.
        {{{grupo_economico_response_razao_social_value}}}

        :return: The razao_social of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        """
        Sets the razao_social of this GrupoEconomicoResponse.
        {{{grupo_economico_response_razao_social_value}}}

        :param razao_social: The razao_social of this GrupoEconomicoResponse.
        :type: str
        """
        self._razao_social = razao_social

    @property
    def nome_credor(self):
        """
        Gets the nome_credor of this GrupoEconomicoResponse.
        {{{grupo_economico_response_nome_credor_value}}}

        :return: The nome_credor of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._nome_credor

    @nome_credor.setter
    def nome_credor(self, nome_credor):
        """
        Sets the nome_credor of this GrupoEconomicoResponse.
        {{{grupo_economico_response_nome_credor_value}}}

        :param nome_credor: The nome_credor of this GrupoEconomicoResponse.
        :type: str
        """
        self._nome_credor = nome_credor

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_numero_receita_federal_value}}}

        :return: The numero_receita_federal of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_numero_receita_federal_value}}}

        :param numero_receita_federal: The numero_receita_federal of this GrupoEconomicoResponse.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def inscricao_estadual(self):
        """
        Gets the inscricao_estadual of this GrupoEconomicoResponse.
        {{{grupo_economico_response_inscricao_estadual_value}}}

        :return: The inscricao_estadual of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._inscricao_estadual

    @inscricao_estadual.setter
    def inscricao_estadual(self, inscricao_estadual):
        """
        Sets the inscricao_estadual of this GrupoEconomicoResponse.
        {{{grupo_economico_response_inscricao_estadual_value}}}

        :param inscricao_estadual: The inscricao_estadual of this GrupoEconomicoResponse.
        :type: str
        """
        self._inscricao_estadual = inscricao_estadual

    @property
    def contato(self):
        """
        Gets the contato of this GrupoEconomicoResponse.
        {{{grupo_economico_response_contato_value}}}

        :return: The contato of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._contato

    @contato.setter
    def contato(self, contato):
        """
        Sets the contato of this GrupoEconomicoResponse.
        {{{grupo_economico_response_contato_value}}}

        :param contato: The contato of this GrupoEconomicoResponse.
        :type: str
        """
        self._contato = contato

    @property
    def banco(self):
        """
        Gets the banco of this GrupoEconomicoResponse.
        {{{grupo_economico_response_banco_value}}}

        :return: The banco of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this GrupoEconomicoResponse.
        {{{grupo_economico_response_banco_value}}}

        :param banco: The banco of this GrupoEconomicoResponse.
        :type: int
        """
        self._banco = banco

    @property
    def agencia(self):
        """
        Gets the agencia of this GrupoEconomicoResponse.
        {{{grupo_economico_response_agencia_value}}}

        :return: The agencia of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        """
        Sets the agencia of this GrupoEconomicoResponse.
        {{{grupo_economico_response_agencia_value}}}

        :param agencia: The agencia of this GrupoEconomicoResponse.
        :type: int
        """
        self._agencia = agencia

    @property
    def digito_agencia(self):
        """
        Gets the digito_agencia of this GrupoEconomicoResponse.
        {{{grupo_economico_response_digito_agencia_value}}}

        :return: The digito_agencia of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._digito_agencia

    @digito_agencia.setter
    def digito_agencia(self, digito_agencia):
        """
        Sets the digito_agencia of this GrupoEconomicoResponse.
        {{{grupo_economico_response_digito_agencia_value}}}

        :param digito_agencia: The digito_agencia of this GrupoEconomicoResponse.
        :type: str
        """
        self._digito_agencia = digito_agencia

    @property
    def conta_corrente(self):
        """
        Gets the conta_corrente of this GrupoEconomicoResponse.
        {{{grupo_economico_response_conta_corrente_value}}}

        :return: The conta_corrente of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        """
        Sets the conta_corrente of this GrupoEconomicoResponse.
        {{{grupo_economico_response_conta_corrente_value}}}

        :param conta_corrente: The conta_corrente of this GrupoEconomicoResponse.
        :type: str
        """
        self._conta_corrente = conta_corrente

    @property
    def digito_conta_corrente(self):
        """
        Gets the digito_conta_corrente of this GrupoEconomicoResponse.
        {{{grupo_economico_response_digito_conta_corrente_value}}}

        :return: The digito_conta_corrente of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._digito_conta_corrente

    @digito_conta_corrente.setter
    def digito_conta_corrente(self, digito_conta_corrente):
        """
        Sets the digito_conta_corrente of this GrupoEconomicoResponse.
        {{{grupo_economico_response_digito_conta_corrente_value}}}

        :param digito_conta_corrente: The digito_conta_corrente of this GrupoEconomicoResponse.
        :type: str
        """
        self._digito_conta_corrente = digito_conta_corrente

    @property
    def usuario(self):
        """
        Gets the usuario of this GrupoEconomicoResponse.
        {{{grupo_economico_response_usuario_value}}}

        :return: The usuario of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this GrupoEconomicoResponse.
        {{{grupo_economico_response_usuario_value}}}

        :param usuario: The usuario of this GrupoEconomicoResponse.
        :type: str
        """
        self._usuario = usuario

    @property
    def periodicidade(self):
        """
        Gets the periodicidade of this GrupoEconomicoResponse.
        {{{grupo_economico_response_periodicidade_value}}}

        :return: The periodicidade of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._periodicidade

    @periodicidade.setter
    def periodicidade(self, periodicidade):
        """
        Sets the periodicidade of this GrupoEconomicoResponse.
        {{{grupo_economico_response_periodicidade_value}}}

        :param periodicidade: The periodicidade of this GrupoEconomicoResponse.
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
    def pagamento_semanal(self):
        """
        Gets the pagamento_semanal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_semanal_value}}}

        :return: The pagamento_semanal of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._pagamento_semanal

    @pagamento_semanal.setter
    def pagamento_semanal(self, pagamento_semanal):
        """
        Sets the pagamento_semanal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_semanal_value}}}

        :param pagamento_semanal: The pagamento_semanal of this GrupoEconomicoResponse.
        :type: str
        """
        allowed_values = ["SEGUNDA", "TERCA", "QUARTA", "QUINTA", "SEXTA", "SABADO", "DOMINGO"]
        if pagamento_semanal not in allowed_values:
            raise ValueError(
                "Invalid value for `pagamento_semanal`, must be one of {0}"
                .format(allowed_values)
            )
        self._pagamento_semanal = pagamento_semanal

    @property
    def pagamento_mensal(self):
        """
        Gets the pagamento_mensal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_mensal_value}}}

        :return: The pagamento_mensal of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_mensal

    @pagamento_mensal.setter
    def pagamento_mensal(self, pagamento_mensal):
        """
        Sets the pagamento_mensal of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_mensal_value}}}

        :param pagamento_mensal: The pagamento_mensal of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_mensal = pagamento_mensal

    @property
    def pagamento_decendial_primeiro(self):
        """
        Gets the pagamento_decendial_primeiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_primeiro_value}}}

        :return: The pagamento_decendial_primeiro of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_decendial_primeiro

    @pagamento_decendial_primeiro.setter
    def pagamento_decendial_primeiro(self, pagamento_decendial_primeiro):
        """
        Sets the pagamento_decendial_primeiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_primeiro_value}}}

        :param pagamento_decendial_primeiro: The pagamento_decendial_primeiro of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_decendial_primeiro = pagamento_decendial_primeiro

    @property
    def pagamento_decendial_segundo(self):
        """
        Gets the pagamento_decendial_segundo of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_segundo_value}}}

        :return: The pagamento_decendial_segundo of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_decendial_segundo

    @pagamento_decendial_segundo.setter
    def pagamento_decendial_segundo(self, pagamento_decendial_segundo):
        """
        Sets the pagamento_decendial_segundo of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_segundo_value}}}

        :param pagamento_decendial_segundo: The pagamento_decendial_segundo of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_decendial_segundo = pagamento_decendial_segundo

    @property
    def pagamento_decendial_terceiro(self):
        """
        Gets the pagamento_decendial_terceiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_terceiro_value}}}

        :return: The pagamento_decendial_terceiro of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_decendial_terceiro

    @pagamento_decendial_terceiro.setter
    def pagamento_decendial_terceiro(self, pagamento_decendial_terceiro):
        """
        Sets the pagamento_decendial_terceiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_decendial_terceiro_value}}}

        :param pagamento_decendial_terceiro: The pagamento_decendial_terceiro of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_decendial_terceiro = pagamento_decendial_terceiro

    @property
    def pagamento_quinzenal_primeiro(self):
        """
        Gets the pagamento_quinzenal_primeiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_quinzenal_primeiro_value}}}

        :return: The pagamento_quinzenal_primeiro of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_quinzenal_primeiro

    @pagamento_quinzenal_primeiro.setter
    def pagamento_quinzenal_primeiro(self, pagamento_quinzenal_primeiro):
        """
        Sets the pagamento_quinzenal_primeiro of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_quinzenal_primeiro_value}}}

        :param pagamento_quinzenal_primeiro: The pagamento_quinzenal_primeiro of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_quinzenal_primeiro = pagamento_quinzenal_primeiro

    @property
    def pagamento_quinzenal_segundo(self):
        """
        Gets the pagamento_quinzenal_segundo of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_quinzenal_segundo_value}}}

        :return: The pagamento_quinzenal_segundo of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._pagamento_quinzenal_segundo

    @pagamento_quinzenal_segundo.setter
    def pagamento_quinzenal_segundo(self, pagamento_quinzenal_segundo):
        """
        Sets the pagamento_quinzenal_segundo of this GrupoEconomicoResponse.
        {{{grupo_economico_response_pagamento_quinzenal_segundo_value}}}

        :param pagamento_quinzenal_segundo: The pagamento_quinzenal_segundo of this GrupoEconomicoResponse.
        :type: int
        """
        self._pagamento_quinzenal_segundo = pagamento_quinzenal_segundo

    @property
    def id_credor_rav(self):
        """
        Gets the id_credor_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_id_credor_r_a_v_value}}}

        :return: The id_credor_rav of this GrupoEconomicoResponse.
        :rtype: int
        """
        return self._id_credor_rav

    @id_credor_rav.setter
    def id_credor_rav(self, id_credor_rav):
        """
        Sets the id_credor_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_id_credor_r_a_v_value}}}

        :param id_credor_rav: The id_credor_rav of this GrupoEconomicoResponse.
        :type: int
        """
        self._id_credor_rav = id_credor_rav

    @property
    def percentual_rav(self):
        """
        Gets the percentual_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_percentual_r_a_v_value}}}

        :return: The percentual_rav of this GrupoEconomicoResponse.
        :rtype: float
        """
        return self._percentual_rav

    @percentual_rav.setter
    def percentual_rav(self, percentual_rav):
        """
        Sets the percentual_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_percentual_r_a_v_value}}}

        :param percentual_rav: The percentual_rav of this GrupoEconomicoResponse.
        :type: float
        """
        self._percentual_rav = percentual_rav

    @property
    def recebe_rav(self):
        """
        Gets the recebe_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_recebe_r_a_v_value}}}

        :return: The recebe_rav of this GrupoEconomicoResponse.
        :rtype: str
        """
        return self._recebe_rav

    @recebe_rav.setter
    def recebe_rav(self, recebe_rav):
        """
        Sets the recebe_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_recebe_r_a_v_value}}}

        :param recebe_rav: The recebe_rav of this GrupoEconomicoResponse.
        :type: str
        """
        allowed_values = ["NAO_TEM_PERMISSAO_RAV", "CREDITO_RAV", "DEBITO_RAV"]
        if recebe_rav not in allowed_values:
            raise ValueError(
                "Invalid value for `recebe_rav`, must be one of {0}"
                .format(allowed_values)
            )
        self._recebe_rav = recebe_rav

    @property
    def percentual_multiplica(self):
        """
        Gets the percentual_multiplica of this GrupoEconomicoResponse.
        {{{grupo_economico_response_percentual_multiplica_value}}}

        :return: The percentual_multiplica of this GrupoEconomicoResponse.
        :rtype: float
        """
        return self._percentual_multiplica

    @percentual_multiplica.setter
    def percentual_multiplica(self, percentual_multiplica):
        """
        Sets the percentual_multiplica of this GrupoEconomicoResponse.
        {{{grupo_economico_response_percentual_multiplica_value}}}

        :param percentual_multiplica: The percentual_multiplica of this GrupoEconomicoResponse.
        :type: float
        """
        self._percentual_multiplica = percentual_multiplica

    @property
    def taxa_adm(self):
        """
        Gets the taxa_adm of this GrupoEconomicoResponse.
        {{{grupo_economico_response_taxa_adm_value}}}

        :return: The taxa_adm of this GrupoEconomicoResponse.
        :rtype: float
        """
        return self._taxa_adm

    @taxa_adm.setter
    def taxa_adm(self, taxa_adm):
        """
        Sets the taxa_adm of this GrupoEconomicoResponse.
        {{{grupo_economico_response_taxa_adm_value}}}

        :param taxa_adm: The taxa_adm of this GrupoEconomicoResponse.
        :type: float
        """
        self._taxa_adm = taxa_adm

    @property
    def taxa_banco(self):
        """
        Gets the taxa_banco of this GrupoEconomicoResponse.
        {{{grupo_economico_response_taxa_banco_value}}}

        :return: The taxa_banco of this GrupoEconomicoResponse.
        :rtype: float
        """
        return self._taxa_banco

    @taxa_banco.setter
    def taxa_banco(self, taxa_banco):
        """
        Sets the taxa_banco of this GrupoEconomicoResponse.
        {{{grupo_economico_response_taxa_banco_value}}}

        :param taxa_banco: The taxa_banco of this GrupoEconomicoResponse.
        :type: float
        """
        self._taxa_banco = taxa_banco

    @property
    def limite_rav(self):
        """
        Gets the limite_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_limite_r_a_v_value}}}

        :return: The limite_rav of this GrupoEconomicoResponse.
        :rtype: float
        """
        return self._limite_rav

    @limite_rav.setter
    def limite_rav(self, limite_rav):
        """
        Sets the limite_rav of this GrupoEconomicoResponse.
        {{{grupo_economico_response_limite_r_a_v_value}}}

        :param limite_rav: The limite_rav of this GrupoEconomicoResponse.
        :type: float
        """
        self._limite_rav = limite_rav

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
