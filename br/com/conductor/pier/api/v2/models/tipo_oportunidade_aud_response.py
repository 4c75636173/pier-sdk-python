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


class TipoOportunidadeAUDResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoOportunidadeAUDResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rev': 'int',
            'rev_type': 'int',
            'rev_date': 'str',
            'id': 'int',
            'descricao': 'str',
            'flag_ativo': 'bool'
        }

        self.attribute_map = {
            'rev': 'rev',
            'rev_type': 'revType',
            'rev_date': 'revDate',
            'id': 'id',
            'descricao': 'descricao',
            'flag_ativo': 'flagAtivo'
        }

        self._rev = None
        self._rev_type = None
        self._rev_date = None
        self._id = None
        self._descricao = None
        self._flag_ativo = None

    @property
    def rev(self):
        """
        Gets the rev of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_value}}}

        :return: The rev of this TipoOportunidadeAUDResponse.
        :rtype: int
        """
        return self._rev

    @rev.setter
    def rev(self, rev):
        """
        Sets the rev of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_value}}}

        :param rev: The rev of this TipoOportunidadeAUDResponse.
        :type: int
        """
        self._rev = rev

    @property
    def rev_type(self):
        """
        Gets the rev_type of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_type_value}}}

        :return: The rev_type of this TipoOportunidadeAUDResponse.
        :rtype: int
        """
        return self._rev_type

    @rev_type.setter
    def rev_type(self, rev_type):
        """
        Sets the rev_type of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_type_value}}}

        :param rev_type: The rev_type of this TipoOportunidadeAUDResponse.
        :type: int
        """
        self._rev_type = rev_type

    @property
    def rev_date(self):
        """
        Gets the rev_date of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_date_value}}}

        :return: The rev_date of this TipoOportunidadeAUDResponse.
        :rtype: str
        """
        return self._rev_date

    @rev_date.setter
    def rev_date(self, rev_date):
        """
        Sets the rev_date of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_rev_date_value}}}

        :param rev_date: The rev_date of this TipoOportunidadeAUDResponse.
        :type: str
        """
        self._rev_date = rev_date

    @property
    def id(self):
        """
        Gets the id of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_id_value}}}

        :return: The id of this TipoOportunidadeAUDResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_id_value}}}

        :param id: The id of this TipoOportunidadeAUDResponse.
        :type: int
        """
        self._id = id

    @property
    def descricao(self):
        """
        Gets the descricao of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_descricao_value}}}

        :return: The descricao of this TipoOportunidadeAUDResponse.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_descricao_value}}}

        :param descricao: The descricao of this TipoOportunidadeAUDResponse.
        :type: str
        """
        self._descricao = descricao

    @property
    def flag_ativo(self):
        """
        Gets the flag_ativo of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_flag_ativo_value}}}

        :return: The flag_ativo of this TipoOportunidadeAUDResponse.
        :rtype: bool
        """
        return self._flag_ativo

    @flag_ativo.setter
    def flag_ativo(self, flag_ativo):
        """
        Sets the flag_ativo of this TipoOportunidadeAUDResponse.
        {{{tipo_oportunidade_a_u_d_response_flag_ativo_value}}}

        :param flag_ativo: The flag_ativo of this TipoOportunidadeAUDResponse.
        :type: bool
        """
        self._flag_ativo = flag_ativo

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

