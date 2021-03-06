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


class HistoricoEventosResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HistoricoEventosResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_historico': 'int',
            'data_historico': 'str',
            'tipo_historico': 'str',
            'valor_anterior': 'str',
            'valor_atribuido': 'str'
        }

        self.attribute_map = {
            'id_historico': 'idHistorico',
            'data_historico': 'dataHistorico',
            'tipo_historico': 'tipoHistorico',
            'valor_anterior': 'valorAnterior',
            'valor_atribuido': 'valorAtribuido'
        }

        self._id_historico = None
        self._data_historico = None
        self._tipo_historico = None
        self._valor_anterior = None
        self._valor_atribuido = None

    @property
    def id_historico(self):
        """
        Gets the id_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_id_historico_value}}}

        :return: The id_historico of this HistoricoEventosResponse.
        :rtype: int
        """
        return self._id_historico

    @id_historico.setter
    def id_historico(self, id_historico):
        """
        Sets the id_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_id_historico_value}}}

        :param id_historico: The id_historico of this HistoricoEventosResponse.
        :type: int
        """
        self._id_historico = id_historico

    @property
    def data_historico(self):
        """
        Gets the data_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_data_historico_value}}}

        :return: The data_historico of this HistoricoEventosResponse.
        :rtype: str
        """
        return self._data_historico

    @data_historico.setter
    def data_historico(self, data_historico):
        """
        Sets the data_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_data_historico_value}}}

        :param data_historico: The data_historico of this HistoricoEventosResponse.
        :type: str
        """
        self._data_historico = data_historico

    @property
    def tipo_historico(self):
        """
        Gets the tipo_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_tipo_historico_value}}}

        :return: The tipo_historico of this HistoricoEventosResponse.
        :rtype: str
        """
        return self._tipo_historico

    @tipo_historico.setter
    def tipo_historico(self, tipo_historico):
        """
        Sets the tipo_historico of this HistoricoEventosResponse.
        {{{historico_eventos_response_tipo_historico_value}}}

        :param tipo_historico: The tipo_historico of this HistoricoEventosResponse.
        :type: str
        """
        self._tipo_historico = tipo_historico

    @property
    def valor_anterior(self):
        """
        Gets the valor_anterior of this HistoricoEventosResponse.
        {{{historico_eventos_response_valor_anterior_value}}}

        :return: The valor_anterior of this HistoricoEventosResponse.
        :rtype: str
        """
        return self._valor_anterior

    @valor_anterior.setter
    def valor_anterior(self, valor_anterior):
        """
        Sets the valor_anterior of this HistoricoEventosResponse.
        {{{historico_eventos_response_valor_anterior_value}}}

        :param valor_anterior: The valor_anterior of this HistoricoEventosResponse.
        :type: str
        """
        self._valor_anterior = valor_anterior

    @property
    def valor_atribuido(self):
        """
        Gets the valor_atribuido of this HistoricoEventosResponse.
        {{{historico_eventos_response_valor_atribuido_value}}}

        :return: The valor_atribuido of this HistoricoEventosResponse.
        :rtype: str
        """
        return self._valor_atribuido

    @valor_atribuido.setter
    def valor_atribuido(self, valor_atribuido):
        """
        Sets the valor_atribuido of this HistoricoEventosResponse.
        {{{historico_eventos_response_valor_atribuido_value}}}

        :param valor_atribuido: The valor_atribuido of this HistoricoEventosResponse.
        :type: str
        """
        self._valor_atribuido = valor_atribuido

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

