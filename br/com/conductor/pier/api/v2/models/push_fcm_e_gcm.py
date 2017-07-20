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


class PushFCMEGCM(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PushFCMEGCM - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_pessoa': 'int',
            'id_conta': 'int',
            'token_dispositivo': 'str',
            'token_servidor': 'str',
            'titulo': 'str',
            'conteudo': 'str',
            'tipo_evento': 'str',
            'icone': 'str',
            'som': 'str',
            'cor': 'str'
        }

        self.attribute_map = {
            'id_pessoa': 'idPessoa',
            'id_conta': 'idConta',
            'token_dispositivo': 'tokenDispositivo',
            'token_servidor': 'tokenServidor',
            'titulo': 'titulo',
            'conteudo': 'conteudo',
            'tipo_evento': 'tipoEvento',
            'icone': 'icone',
            'som': 'som',
            'cor': 'cor'
        }

        self._id_pessoa = None
        self._id_conta = None
        self._token_dispositivo = None
        self._token_servidor = None
        self._titulo = None
        self._conteudo = None
        self._tipo_evento = None
        self._icone = None
        self._som = None
        self._cor = None

    @property
    def id_pessoa(self):
        """
        Gets the id_pessoa of this PushFCMEGCM.
        C\u00C3\u00B3digo identificado da pessoa

        :return: The id_pessoa of this PushFCMEGCM.
        :rtype: int
        """
        return self._id_pessoa

    @id_pessoa.setter
    def id_pessoa(self, id_pessoa):
        """
        Sets the id_pessoa of this PushFCMEGCM.
        C\u00C3\u00B3digo identificado da pessoa

        :param id_pessoa: The id_pessoa of this PushFCMEGCM.
        :type: int
        """
        self._id_pessoa = id_pessoa

    @property
    def id_conta(self):
        """
        Gets the id_conta of this PushFCMEGCM.
        C\u00C3\u00B3digo identificador da conta

        :return: The id_conta of this PushFCMEGCM.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this PushFCMEGCM.
        C\u00C3\u00B3digo identificador da conta

        :param id_conta: The id_conta of this PushFCMEGCM.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def token_dispositivo(self):
        """
        Gets the token_dispositivo of this PushFCMEGCM.
        Apresenta o token do dispositivo que dever\u00C3\u00A1 receber o push.

        :return: The token_dispositivo of this PushFCMEGCM.
        :rtype: str
        """
        return self._token_dispositivo

    @token_dispositivo.setter
    def token_dispositivo(self, token_dispositivo):
        """
        Sets the token_dispositivo of this PushFCMEGCM.
        Apresenta o token do dispositivo que dever\u00C3\u00A1 receber o push.

        :param token_dispositivo: The token_dispositivo of this PushFCMEGCM.
        :type: str
        """
        self._token_dispositivo = token_dispositivo

    @property
    def token_servidor(self):
        """
        Gets the token_servidor of this PushFCMEGCM.
        Apresenta o token da sua aplica\u00C3\u00A7\u00C3\u00A3o Android gerada pela Google.

        :return: The token_servidor of this PushFCMEGCM.
        :rtype: str
        """
        return self._token_servidor

    @token_servidor.setter
    def token_servidor(self, token_servidor):
        """
        Sets the token_servidor of this PushFCMEGCM.
        Apresenta o token da sua aplica\u00C3\u00A7\u00C3\u00A3o Android gerada pela Google.

        :param token_servidor: The token_servidor of this PushFCMEGCM.
        :type: str
        """
        self._token_servidor = token_servidor

    @property
    def titulo(self):
        """
        Gets the titulo of this PushFCMEGCM.
        Apresenta o t\u00C3\u00ADtulo da notifica\u00C3\u00A7\u00C3\u00A3o.

        :return: The titulo of this PushFCMEGCM.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        """
        Sets the titulo of this PushFCMEGCM.
        Apresenta o t\u00C3\u00ADtulo da notifica\u00C3\u00A7\u00C3\u00A3o.

        :param titulo: The titulo of this PushFCMEGCM.
        :type: str
        """
        self._titulo = titulo

    @property
    def conteudo(self):
        """
        Gets the conteudo of this PushFCMEGCM.
        Apresenta o texto da notifica\u00C3\u00A7\u00C3\u00A3o a ser enviado.

        :return: The conteudo of this PushFCMEGCM.
        :rtype: str
        """
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        """
        Sets the conteudo of this PushFCMEGCM.
        Apresenta o texto da notifica\u00C3\u00A7\u00C3\u00A3o a ser enviado.

        :param conteudo: The conteudo of this PushFCMEGCM.
        :type: str
        """
        self._conteudo = conteudo

    @property
    def tipo_evento(self):
        """
        Gets the tipo_evento of this PushFCMEGCM.
        Apresenta o tipoEvento a qual pertence a notifica\u00C3\u00A7\u00C3\u00A3o

        :return: The tipo_evento of this PushFCMEGCM.
        :rtype: str
        """
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, tipo_evento):
        """
        Sets the tipo_evento of this PushFCMEGCM.
        Apresenta o tipoEvento a qual pertence a notifica\u00C3\u00A7\u00C3\u00A3o

        :param tipo_evento: The tipo_evento of this PushFCMEGCM.
        :type: str
        """
        allowed_values = ["RISCO_FRAUDE", "TOKEN_SMS", "OUTROS"]
        if tipo_evento not in allowed_values:
            raise ValueError(
                "Invalid value for `tipo_evento`, must be one of {0}"
                .format(allowed_values)
            )
        self._tipo_evento = tipo_evento

    @property
    def icone(self):
        """
        Gets the icone of this PushFCMEGCM.
        Apresenta o nome do icone a ser apresentado no push.

        :return: The icone of this PushFCMEGCM.
        :rtype: str
        """
        return self._icone

    @icone.setter
    def icone(self, icone):
        """
        Sets the icone of this PushFCMEGCM.
        Apresenta o nome do icone a ser apresentado no push.

        :param icone: The icone of this PushFCMEGCM.
        :type: str
        """
        self._icone = icone

    @property
    def som(self):
        """
        Gets the som of this PushFCMEGCM.
        Apresenta o cor do icone a ser apresentado no push

        :return: The som of this PushFCMEGCM.
        :rtype: str
        """
        return self._som

    @som.setter
    def som(self, som):
        """
        Sets the som of this PushFCMEGCM.
        Apresenta o cor do icone a ser apresentado no push

        :param som: The som of this PushFCMEGCM.
        :type: str
        """
        self._som = som

    @property
    def cor(self):
        """
        Gets the cor of this PushFCMEGCM.
        Apresenta a cor do icone da notifica\u00C3\u00A7\u00C3\u00A3o. Essa cor dever\u00C3\u00A1 ser informada no formato RGB Ex. #000000.

        :return: The cor of this PushFCMEGCM.
        :rtype: str
        """
        return self._cor

    @cor.setter
    def cor(self, cor):
        """
        Sets the cor of this PushFCMEGCM.
        Apresenta a cor do icone da notifica\u00C3\u00A7\u00C3\u00A3o. Essa cor dever\u00C3\u00A1 ser informada no formato RGB Ex. #000000.

        :param cor: The cor of this PushFCMEGCM.
        :type: str
        """
        self._cor = cor

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

