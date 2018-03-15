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


class TipoFaturamentoPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoFaturamentoPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'descricao': 'str',
            'flag_apenas_demonstrativo': 'bool',
            'id_convenio': 'int'
        }

        self.attribute_map = {
            'descricao': 'descricao',
            'flag_apenas_demonstrativo': 'flagApenasDemonstrativo',
            'id_convenio': 'idConvenio'
        }

        self._descricao = None
        self._flag_apenas_demonstrativo = None
        self._id_convenio = None

    @property
    def descricao(self):
        """
        Gets the descricao of this TipoFaturamentoPersist.
        Desci\u00E7\u00E3o do tipo de faturamento.

        :return: The descricao of this TipoFaturamentoPersist.
        :rtype: str
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        """
        Sets the descricao of this TipoFaturamentoPersist.
        Desci\u00E7\u00E3o do tipo de faturamento.

        :param descricao: The descricao of this TipoFaturamentoPersist.
        :type: str
        """
        self._descricao = descricao

    @property
    def flag_apenas_demonstrativo(self):
        """
        Gets the flag_apenas_demonstrativo of this TipoFaturamentoPersist.
        Flag que representa que o faturamento ser\u00E1 apenas demonstrativo.

        :return: The flag_apenas_demonstrativo of this TipoFaturamentoPersist.
        :rtype: bool
        """
        return self._flag_apenas_demonstrativo

    @flag_apenas_demonstrativo.setter
    def flag_apenas_demonstrativo(self, flag_apenas_demonstrativo):
        """
        Sets the flag_apenas_demonstrativo of this TipoFaturamentoPersist.
        Flag que representa que o faturamento ser\u00E1 apenas demonstrativo.

        :param flag_apenas_demonstrativo: The flag_apenas_demonstrativo of this TipoFaturamentoPersist.
        :type: bool
        """
        self._flag_apenas_demonstrativo = flag_apenas_demonstrativo

    @property
    def id_convenio(self):
        """
        Gets the id_convenio of this TipoFaturamentoPersist.
        C\u00F3digo de identifica\u00E7\u00E3o do convenio relacionado ao tipo de faturamento.

        :return: The id_convenio of this TipoFaturamentoPersist.
        :rtype: int
        """
        return self._id_convenio

    @id_convenio.setter
    def id_convenio(self, id_convenio):
        """
        Sets the id_convenio of this TipoFaturamentoPersist.
        C\u00F3digo de identifica\u00E7\u00E3o do convenio relacionado ao tipo de faturamento.

        :param id_convenio: The id_convenio of this TipoFaturamentoPersist.
        :type: int
        """
        self._id_convenio = id_convenio

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

