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


class UsuarioPersistencia(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UsuarioPersistencia - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'nome': 'str',
            'login': 'str',
            'cpf': 'str',
            'email': 'str',
            'senha': 'str',
            'data_validade': 'str',
            'id_plataforma': 'int'
        }

        self.attribute_map = {
            'nome': 'nome',
            'login': 'login',
            'cpf': 'cpf',
            'email': 'email',
            'senha': 'senha',
            'data_validade': 'dataValidade',
            'id_plataforma': 'idPlataforma'
        }

        self._nome = None
        self._login = None
        self._cpf = None
        self._email = None
        self._senha = None
        self._data_validade = None
        self._id_plataforma = None

    @property
    def nome(self):
        """
        Gets the nome of this UsuarioPersistencia.
        {{{usuario_persistencia_nome_descricao}}}

        :return: The nome of this UsuarioPersistencia.
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """
        Sets the nome of this UsuarioPersistencia.
        {{{usuario_persistencia_nome_descricao}}}

        :param nome: The nome of this UsuarioPersistencia.
        :type: str
        """
        self._nome = nome

    @property
    def login(self):
        """
        Gets the login of this UsuarioPersistencia.
        {{{usuario_persistencia_login_descricao}}}

        :return: The login of this UsuarioPersistencia.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """
        Sets the login of this UsuarioPersistencia.
        {{{usuario_persistencia_login_descricao}}}

        :param login: The login of this UsuarioPersistencia.
        :type: str
        """
        self._login = login

    @property
    def cpf(self):
        """
        Gets the cpf of this UsuarioPersistencia.
        {{{usuario_persistencia_cpf_descricao}}}

        :return: The cpf of this UsuarioPersistencia.
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """
        Sets the cpf of this UsuarioPersistencia.
        {{{usuario_persistencia_cpf_descricao}}}

        :param cpf: The cpf of this UsuarioPersistencia.
        :type: str
        """
        self._cpf = cpf

    @property
    def email(self):
        """
        Gets the email of this UsuarioPersistencia.
        {{{usuario_persistencia_email_descricao}}}

        :return: The email of this UsuarioPersistencia.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UsuarioPersistencia.
        {{{usuario_persistencia_email_descricao}}}

        :param email: The email of this UsuarioPersistencia.
        :type: str
        """
        self._email = email

    @property
    def senha(self):
        """
        Gets the senha of this UsuarioPersistencia.
        {{{usuario_persistencia_senha_descricao}}}

        :return: The senha of this UsuarioPersistencia.
        :rtype: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """
        Sets the senha of this UsuarioPersistencia.
        {{{usuario_persistencia_senha_descricao}}}

        :param senha: The senha of this UsuarioPersistencia.
        :type: str
        """
        self._senha = senha

    @property
    def data_validade(self):
        """
        Gets the data_validade of this UsuarioPersistencia.
        {{{usuario_persistencia_data_validade_descricao}}}

        :return: The data_validade of this UsuarioPersistencia.
        :rtype: str
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this UsuarioPersistencia.
        {{{usuario_persistencia_data_validade_descricao}}}

        :param data_validade: The data_validade of this UsuarioPersistencia.
        :type: str
        """
        self._data_validade = data_validade

    @property
    def id_plataforma(self):
        """
        Gets the id_plataforma of this UsuarioPersistencia.
        {{{usuario_persistencia_id_plataforma_descricao}}}

        :return: The id_plataforma of this UsuarioPersistencia.
        :rtype: int
        """
        return self._id_plataforma

    @id_plataforma.setter
    def id_plataforma(self, id_plataforma):
        """
        Sets the id_plataforma of this UsuarioPersistencia.
        {{{usuario_persistencia_id_plataforma_descricao}}}

        :param id_plataforma: The id_plataforma of this UsuarioPersistencia.
        :type: int
        """
        self._id_plataforma = id_plataforma

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
