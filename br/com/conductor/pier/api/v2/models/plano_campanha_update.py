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


class PlanoCampanhaUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PlanoCampanhaUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'parcelas': 'int',
            'taxa': 'float',
            'usuario': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'parcelas': 'parcelas',
            'taxa': 'taxa',
            'usuario': 'usuario'
        }

        self._id = None
        self._parcelas = None
        self._taxa = None
        self._usuario = None

    @property
    def id(self):
        """
        Gets the id of this PlanoCampanhaUpdate.
        C\u00C3\u00B3digo identificador do plano campanha

        :return: The id of this PlanoCampanhaUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PlanoCampanhaUpdate.
        C\u00C3\u00B3digo identificador do plano campanha

        :param id: The id of this PlanoCampanhaUpdate.
        :type: int
        """
        self._id = id

    @property
    def parcelas(self):
        """
        Gets the parcelas of this PlanoCampanhaUpdate.
        Quantidade de parcelas

        :return: The parcelas of this PlanoCampanhaUpdate.
        :rtype: int
        """
        return self._parcelas

    @parcelas.setter
    def parcelas(self, parcelas):
        """
        Sets the parcelas of this PlanoCampanhaUpdate.
        Quantidade de parcelas

        :param parcelas: The parcelas of this PlanoCampanhaUpdate.
        :type: int
        """
        self._parcelas = parcelas

    @property
    def taxa(self):
        """
        Gets the taxa of this PlanoCampanhaUpdate.
        Taxa de juros

        :return: The taxa of this PlanoCampanhaUpdate.
        :rtype: float
        """
        return self._taxa

    @taxa.setter
    def taxa(self, taxa):
        """
        Sets the taxa of this PlanoCampanhaUpdate.
        Taxa de juros

        :param taxa: The taxa of this PlanoCampanhaUpdate.
        :type: float
        """
        self._taxa = taxa

    @property
    def usuario(self):
        """
        Gets the usuario of this PlanoCampanhaUpdate.
        Nome do usu\u00C3\u00A1rio

        :return: The usuario of this PlanoCampanhaUpdate.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """
        Sets the usuario of this PlanoCampanhaUpdate.
        Nome do usu\u00C3\u00A1rio

        :param usuario: The usuario of this PlanoCampanhaUpdate.
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

