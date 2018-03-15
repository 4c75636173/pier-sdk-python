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


class TipoFaturamentoPorContaPersist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TipoFaturamentoPorContaPersist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'bool',
            'id_conta': 'int',
            'id_tipo_faturamento': 'int',
            'data_hora_inclusao': 'str',
            'data_hora_cancelamento': 'str',
            'modificado_por': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'id_conta': 'idConta',
            'id_tipo_faturamento': 'idTipoFaturamento',
            'data_hora_inclusao': 'dataHoraInclusao',
            'data_hora_cancelamento': 'dataHoraCancelamento',
            'modificado_por': 'modificadoPor'
        }

        self._status = None
        self._id_conta = None
        self._id_tipo_faturamento = None
        self._data_hora_inclusao = None
        self._data_hora_cancelamento = None
        self._modificado_por = None

    @property
    def status(self):
        """
        Gets the status of this TipoFaturamentoPorContaPersist.
        Representa se a configura\u00E7\u00E3o est\u00E1 ativada ou desativada para a conta.

        :return: The status of this TipoFaturamentoPorContaPersist.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TipoFaturamentoPorContaPersist.
        Representa se a configura\u00E7\u00E3o est\u00E1 ativada ou desativada para a conta.

        :param status: The status of this TipoFaturamentoPorContaPersist.
        :type: bool
        """
        self._status = status

    @property
    def id_conta(self):
        """
        Gets the id_conta of this TipoFaturamentoPorContaPersist.
        C\u00F3digo de identifica\u00E7\u00E3o da conta relacionada.

        :return: The id_conta of this TipoFaturamentoPorContaPersist.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this TipoFaturamentoPorContaPersist.
        C\u00F3digo de identifica\u00E7\u00E3o da conta relacionada.

        :param id_conta: The id_conta of this TipoFaturamentoPorContaPersist.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_tipo_faturamento(self):
        """
        Gets the id_tipo_faturamento of this TipoFaturamentoPorContaPersist.
        C\u00F3digo de identifica\u00E7\u00E3o do tipo de faturamento relacionada.

        :return: The id_tipo_faturamento of this TipoFaturamentoPorContaPersist.
        :rtype: int
        """
        return self._id_tipo_faturamento

    @id_tipo_faturamento.setter
    def id_tipo_faturamento(self, id_tipo_faturamento):
        """
        Sets the id_tipo_faturamento of this TipoFaturamentoPorContaPersist.
        C\u00F3digo de identifica\u00E7\u00E3o do tipo de faturamento relacionada.

        :param id_tipo_faturamento: The id_tipo_faturamento of this TipoFaturamentoPorContaPersist.
        :type: int
        """
        self._id_tipo_faturamento = id_tipo_faturamento

    @property
    def data_hora_inclusao(self):
        """
        Gets the data_hora_inclusao of this TipoFaturamentoPorContaPersist.
        Data da inclus\u00E3o da configura\u00E7\u00E3o, deve ser informada no formato yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.

        :return: The data_hora_inclusao of this TipoFaturamentoPorContaPersist.
        :rtype: str
        """
        return self._data_hora_inclusao

    @data_hora_inclusao.setter
    def data_hora_inclusao(self, data_hora_inclusao):
        """
        Sets the data_hora_inclusao of this TipoFaturamentoPorContaPersist.
        Data da inclus\u00E3o da configura\u00E7\u00E3o, deve ser informada no formato yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.

        :param data_hora_inclusao: The data_hora_inclusao of this TipoFaturamentoPorContaPersist.
        :type: str
        """
        self._data_hora_inclusao = data_hora_inclusao

    @property
    def data_hora_cancelamento(self):
        """
        Gets the data_hora_cancelamento of this TipoFaturamentoPorContaPersist.
        Data do cancelamento da configura\u00E7\u00E3o, deve ser informada no formato yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.

        :return: The data_hora_cancelamento of this TipoFaturamentoPorContaPersist.
        :rtype: str
        """
        return self._data_hora_cancelamento

    @data_hora_cancelamento.setter
    def data_hora_cancelamento(self, data_hora_cancelamento):
        """
        Sets the data_hora_cancelamento of this TipoFaturamentoPorContaPersist.
        Data do cancelamento da configura\u00E7\u00E3o, deve ser informada no formato yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.

        :param data_hora_cancelamento: The data_hora_cancelamento of this TipoFaturamentoPorContaPersist.
        :type: str
        """
        self._data_hora_cancelamento = data_hora_cancelamento

    @property
    def modificado_por(self):
        """
        Gets the modificado_por of this TipoFaturamentoPorContaPersist.
        Identificador do respons\u00E1vel pela modifica\u00E7\u00E3o do registro.

        :return: The modificado_por of this TipoFaturamentoPorContaPersist.
        :rtype: str
        """
        return self._modificado_por

    @modificado_por.setter
    def modificado_por(self, modificado_por):
        """
        Sets the modificado_por of this TipoFaturamentoPorContaPersist.
        Identificador do respons\u00E1vel pela modifica\u00E7\u00E3o do registro.

        :param modificado_por: The modificado_por of this TipoFaturamentoPorContaPersist.
        :type: str
        """
        self._modificado_por = modificado_por

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

