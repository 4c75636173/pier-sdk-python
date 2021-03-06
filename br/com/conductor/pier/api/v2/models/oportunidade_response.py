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


class OportunidadeResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OportunidadeResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_tipo_oportunidade': 'int',
            'id_status_oportunidade': 'int',
            'data_cadastro': 'str',
            'data_atualizacao': 'str',
            'numero_receita_federal': 'str',
            'data_inicio_vigencia': 'str',
            'data_fim_vigencia': 'str',
            'flag_ativo': 'bool',
            'detalhes': 'list[DetalheOportunidadeResponse]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_tipo_oportunidade': 'idTipoOportunidade',
            'id_status_oportunidade': 'idStatusOportunidade',
            'data_cadastro': 'dataCadastro',
            'data_atualizacao': 'dataAtualizacao',
            'numero_receita_federal': 'numeroReceitaFederal',
            'data_inicio_vigencia': 'dataInicioVigencia',
            'data_fim_vigencia': 'dataFimVigencia',
            'flag_ativo': 'flagAtivo',
            'detalhes': 'detalhes'
        }

        self._id = None
        self._id_tipo_oportunidade = None
        self._id_status_oportunidade = None
        self._data_cadastro = None
        self._data_atualizacao = None
        self._numero_receita_federal = None
        self._data_inicio_vigencia = None
        self._data_fim_vigencia = None
        self._flag_ativo = None
        self._detalhes = None

    @property
    def id(self):
        """
        Gets the id of this OportunidadeResponse.
        {{{oportunidade_response_id_value}}}

        :return: The id of this OportunidadeResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OportunidadeResponse.
        {{{oportunidade_response_id_value}}}

        :param id: The id of this OportunidadeResponse.
        :type: int
        """
        self._id = id

    @property
    def id_tipo_oportunidade(self):
        """
        Gets the id_tipo_oportunidade of this OportunidadeResponse.
        {{{oportunidade_response_id_tipo_oportunidade_value}}}

        :return: The id_tipo_oportunidade of this OportunidadeResponse.
        :rtype: int
        """
        return self._id_tipo_oportunidade

    @id_tipo_oportunidade.setter
    def id_tipo_oportunidade(self, id_tipo_oportunidade):
        """
        Sets the id_tipo_oportunidade of this OportunidadeResponse.
        {{{oportunidade_response_id_tipo_oportunidade_value}}}

        :param id_tipo_oportunidade: The id_tipo_oportunidade of this OportunidadeResponse.
        :type: int
        """
        self._id_tipo_oportunidade = id_tipo_oportunidade

    @property
    def id_status_oportunidade(self):
        """
        Gets the id_status_oportunidade of this OportunidadeResponse.
        {{{oportunidade_response_id_status_oportunidade_value}}}

        :return: The id_status_oportunidade of this OportunidadeResponse.
        :rtype: int
        """
        return self._id_status_oportunidade

    @id_status_oportunidade.setter
    def id_status_oportunidade(self, id_status_oportunidade):
        """
        Sets the id_status_oportunidade of this OportunidadeResponse.
        {{{oportunidade_response_id_status_oportunidade_value}}}

        :param id_status_oportunidade: The id_status_oportunidade of this OportunidadeResponse.
        :type: int
        """
        self._id_status_oportunidade = id_status_oportunidade

    @property
    def data_cadastro(self):
        """
        Gets the data_cadastro of this OportunidadeResponse.
        {{{oportunidade_response_data_cadastro_value}}}

        :return: The data_cadastro of this OportunidadeResponse.
        :rtype: str
        """
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro):
        """
        Sets the data_cadastro of this OportunidadeResponse.
        {{{oportunidade_response_data_cadastro_value}}}

        :param data_cadastro: The data_cadastro of this OportunidadeResponse.
        :type: str
        """
        self._data_cadastro = data_cadastro

    @property
    def data_atualizacao(self):
        """
        Gets the data_atualizacao of this OportunidadeResponse.
        {{{oportunidade_response_data_atualizacao_value}}}

        :return: The data_atualizacao of this OportunidadeResponse.
        :rtype: str
        """
        return self._data_atualizacao

    @data_atualizacao.setter
    def data_atualizacao(self, data_atualizacao):
        """
        Sets the data_atualizacao of this OportunidadeResponse.
        {{{oportunidade_response_data_atualizacao_value}}}

        :param data_atualizacao: The data_atualizacao of this OportunidadeResponse.
        :type: str
        """
        self._data_atualizacao = data_atualizacao

    @property
    def numero_receita_federal(self):
        """
        Gets the numero_receita_federal of this OportunidadeResponse.
        {{{oportunidade_response_numero_receita_federal_value}}}

        :return: The numero_receita_federal of this OportunidadeResponse.
        :rtype: str
        """
        return self._numero_receita_federal

    @numero_receita_federal.setter
    def numero_receita_federal(self, numero_receita_federal):
        """
        Sets the numero_receita_federal of this OportunidadeResponse.
        {{{oportunidade_response_numero_receita_federal_value}}}

        :param numero_receita_federal: The numero_receita_federal of this OportunidadeResponse.
        :type: str
        """
        self._numero_receita_federal = numero_receita_federal

    @property
    def data_inicio_vigencia(self):
        """
        Gets the data_inicio_vigencia of this OportunidadeResponse.
        {{{oportunidade_response_data_inicio_vigencia_value}}}

        :return: The data_inicio_vigencia of this OportunidadeResponse.
        :rtype: str
        """
        return self._data_inicio_vigencia

    @data_inicio_vigencia.setter
    def data_inicio_vigencia(self, data_inicio_vigencia):
        """
        Sets the data_inicio_vigencia of this OportunidadeResponse.
        {{{oportunidade_response_data_inicio_vigencia_value}}}

        :param data_inicio_vigencia: The data_inicio_vigencia of this OportunidadeResponse.
        :type: str
        """
        self._data_inicio_vigencia = data_inicio_vigencia

    @property
    def data_fim_vigencia(self):
        """
        Gets the data_fim_vigencia of this OportunidadeResponse.
        {{{oportunidade_response_data_fim_vigencia_value}}}

        :return: The data_fim_vigencia of this OportunidadeResponse.
        :rtype: str
        """
        return self._data_fim_vigencia

    @data_fim_vigencia.setter
    def data_fim_vigencia(self, data_fim_vigencia):
        """
        Sets the data_fim_vigencia of this OportunidadeResponse.
        {{{oportunidade_response_data_fim_vigencia_value}}}

        :param data_fim_vigencia: The data_fim_vigencia of this OportunidadeResponse.
        :type: str
        """
        self._data_fim_vigencia = data_fim_vigencia

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this OportunidadeResponse.
        {{{oportunidade_response_flag_ativo_value}}}

        :return: The flag_ativo of this OportunidadeResponse.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this OportunidadeResponse.
        {{{oportunidade_response_flag_ativo_value}}}

        :param flag_ativo: The flag_ativo of this OportunidadeResponse.
        :type: bool
        """
        self._flag_ativo = flag_ativo

    @property
    def detalhes(self):
        """
        Gets the detalhes of this OportunidadeResponse.
        {{{oportunidade_response_detalhes_value}}}

        :return: The detalhes of this OportunidadeResponse.
        :rtype: list[DetalheOportunidadeResponse]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this OportunidadeResponse.
        {{{oportunidade_response_detalhes_value}}}

        :param detalhes: The detalhes of this OportunidadeResponse.
        :type: list[DetalheOportunidadeResponse]
        """
        self._detalhes = detalhes

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

