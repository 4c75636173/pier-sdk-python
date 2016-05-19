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


class CartaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CartaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bin': 'int',
            'cod_retorno': 'int',
            'codigo_desbloqueio': 'str',
            'criptografia_hsm': 'str',
            'data_emissao': 'datetime',
            'data_validade': 'datetime',
            'data_vencimento_padrao': 'str',
            'descricao_retorno': 'str',
            'estagio_cartao': 'int',
            'estagio_data': 'datetime',
            'flag_reversao': 'bool',
            'flag_senha': 'bool',
            'id_cartao': 'int',
            'id_conta': 'int',
            'id_emissor': 'int',
            'id_log': 'str',
            'id_pessoa_fisica': 'int',
            'id_produto': 'int',
            'numero_cartao': 'str',
            'numero_cartao_real': 'str',
            'status_cartao': 'int',
            'status_data': 'datetime'
        }

        self.attribute_map = {
            'bin': 'bin',
            'cod_retorno': 'codRetorno',
            'codigo_desbloqueio': 'codigoDesbloqueio',
            'criptografia_hsm': 'criptografiaHSM',
            'data_emissao': 'dataEmissao',
            'data_validade': 'dataValidade',
            'data_vencimento_padrao': 'dataVencimentoPadrao',
            'descricao_retorno': 'descricaoRetorno',
            'estagio_cartao': 'estagioCartao',
            'estagio_data': 'estagioData',
            'flag_reversao': 'flagReversao',
            'flag_senha': 'flagSenha',
            'id_cartao': 'idCartao',
            'id_conta': 'idConta',
            'id_emissor': 'idEmissor',
            'id_log': 'idLog',
            'id_pessoa_fisica': 'idPessoaFisica',
            'id_produto': 'idProduto',
            'numero_cartao': 'numeroCartao',
            'numero_cartao_real': 'numeroCartaoReal',
            'status_cartao': 'statusCartao',
            'status_data': 'statusData'
        }

        self._bin = None
        self._cod_retorno = None
        self._codigo_desbloqueio = None
        self._criptografia_hsm = None
        self._data_emissao = None
        self._data_validade = None
        self._data_vencimento_padrao = None
        self._descricao_retorno = None
        self._estagio_cartao = None
        self._estagio_data = None
        self._flag_reversao = None
        self._flag_senha = None
        self._id_cartao = None
        self._id_conta = None
        self._id_emissor = None
        self._id_log = None
        self._id_pessoa_fisica = None
        self._id_produto = None
        self._numero_cartao = None
        self._numero_cartao_real = None
        self._status_cartao = None
        self._status_data = None

    @property
    def bin(self):
        """
        Gets the bin of this CartaoResponse.


        :return: The bin of this CartaoResponse.
        :rtype: int
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this CartaoResponse.


        :param bin: The bin of this CartaoResponse.
        :type: int
        """
        self._bin = bin

    @property
    def cod_retorno(self):
        """
        Gets the cod_retorno of this CartaoResponse.


        :return: The cod_retorno of this CartaoResponse.
        :rtype: int
        """
        return self._cod_retorno

    @cod_retorno.setter
    def cod_retorno(self, cod_retorno):
        """
        Sets the cod_retorno of this CartaoResponse.


        :param cod_retorno: The cod_retorno of this CartaoResponse.
        :type: int
        """
        self._cod_retorno = cod_retorno

    @property
    def codigo_desbloqueio(self):
        """
        Gets the codigo_desbloqueio of this CartaoResponse.


        :return: The codigo_desbloqueio of this CartaoResponse.
        :rtype: str
        """
        return self._codigo_desbloqueio

    @codigo_desbloqueio.setter
    def codigo_desbloqueio(self, codigo_desbloqueio):
        """
        Sets the codigo_desbloqueio of this CartaoResponse.


        :param codigo_desbloqueio: The codigo_desbloqueio of this CartaoResponse.
        :type: str
        """
        self._codigo_desbloqueio = codigo_desbloqueio

    @property
    def criptografia_hsm(self):
        """
        Gets the criptografia_hsm of this CartaoResponse.


        :return: The criptografia_hsm of this CartaoResponse.
        :rtype: str
        """
        return self._criptografia_hsm

    @criptografia_hsm.setter
    def criptografia_hsm(self, criptografia_hsm):
        """
        Sets the criptografia_hsm of this CartaoResponse.


        :param criptografia_hsm: The criptografia_hsm of this CartaoResponse.
        :type: str
        """
        self._criptografia_hsm = criptografia_hsm

    @property
    def data_emissao(self):
        """
        Gets the data_emissao of this CartaoResponse.


        :return: The data_emissao of this CartaoResponse.
        :rtype: datetime
        """
        return self._data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao):
        """
        Sets the data_emissao of this CartaoResponse.


        :param data_emissao: The data_emissao of this CartaoResponse.
        :type: datetime
        """
        self._data_emissao = data_emissao

    @property
    def data_validade(self):
        """
        Gets the data_validade of this CartaoResponse.


        :return: The data_validade of this CartaoResponse.
        :rtype: datetime
        """
        return self._data_validade

    @data_validade.setter
    def data_validade(self, data_validade):
        """
        Sets the data_validade of this CartaoResponse.


        :param data_validade: The data_validade of this CartaoResponse.
        :type: datetime
        """
        self._data_validade = data_validade

    @property
    def data_vencimento_padrao(self):
        """
        Gets the data_vencimento_padrao of this CartaoResponse.


        :return: The data_vencimento_padrao of this CartaoResponse.
        :rtype: str
        """
        return self._data_vencimento_padrao

    @data_vencimento_padrao.setter
    def data_vencimento_padrao(self, data_vencimento_padrao):
        """
        Sets the data_vencimento_padrao of this CartaoResponse.


        :param data_vencimento_padrao: The data_vencimento_padrao of this CartaoResponse.
        :type: str
        """
        self._data_vencimento_padrao = data_vencimento_padrao

    @property
    def descricao_retorno(self):
        """
        Gets the descricao_retorno of this CartaoResponse.


        :return: The descricao_retorno of this CartaoResponse.
        :rtype: str
        """
        return self._descricao_retorno

    @descricao_retorno.setter
    def descricao_retorno(self, descricao_retorno):
        """
        Sets the descricao_retorno of this CartaoResponse.


        :param descricao_retorno: The descricao_retorno of this CartaoResponse.
        :type: str
        """
        self._descricao_retorno = descricao_retorno

    @property
    def estagio_cartao(self):
        """
        Gets the estagio_cartao of this CartaoResponse.


        :return: The estagio_cartao of this CartaoResponse.
        :rtype: int
        """
        return self._estagio_cartao

    @estagio_cartao.setter
    def estagio_cartao(self, estagio_cartao):
        """
        Sets the estagio_cartao of this CartaoResponse.


        :param estagio_cartao: The estagio_cartao of this CartaoResponse.
        :type: int
        """
        self._estagio_cartao = estagio_cartao

    @property
    def estagio_data(self):
        """
        Gets the estagio_data of this CartaoResponse.


        :return: The estagio_data of this CartaoResponse.
        :rtype: datetime
        """
        return self._estagio_data

    @estagio_data.setter
    def estagio_data(self, estagio_data):
        """
        Sets the estagio_data of this CartaoResponse.


        :param estagio_data: The estagio_data of this CartaoResponse.
        :type: datetime
        """
        self._estagio_data = estagio_data

    @property
    def flag_reversao(self):
        """
        Gets the flag_reversao of this CartaoResponse.


        :return: The flag_reversao of this CartaoResponse.
        :rtype: bool
        """
        return self._flag_reversao

    @flag_reversao.setter
    def flag_reversao(self, flag_reversao):
        """
        Sets the flag_reversao of this CartaoResponse.


        :param flag_reversao: The flag_reversao of this CartaoResponse.
        :type: bool
        """
        self._flag_reversao = flag_reversao

    @property
    def flag_senha(self):
        """
        Gets the flag_senha of this CartaoResponse.


        :return: The flag_senha of this CartaoResponse.
        :rtype: bool
        """
        return self._flag_senha

    @flag_senha.setter
    def flag_senha(self, flag_senha):
        """
        Sets the flag_senha of this CartaoResponse.


        :param flag_senha: The flag_senha of this CartaoResponse.
        :type: bool
        """
        self._flag_senha = flag_senha

    @property
    def id_cartao(self):
        """
        Gets the id_cartao of this CartaoResponse.


        :return: The id_cartao of this CartaoResponse.
        :rtype: int
        """
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, id_cartao):
        """
        Sets the id_cartao of this CartaoResponse.


        :param id_cartao: The id_cartao of this CartaoResponse.
        :type: int
        """
        self._id_cartao = id_cartao

    @property
    def id_conta(self):
        """
        Gets the id_conta of this CartaoResponse.


        :return: The id_conta of this CartaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this CartaoResponse.


        :param id_conta: The id_conta of this CartaoResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_emissor(self):
        """
        Gets the id_emissor of this CartaoResponse.


        :return: The id_emissor of this CartaoResponse.
        :rtype: int
        """
        return self._id_emissor

    @id_emissor.setter
    def id_emissor(self, id_emissor):
        """
        Sets the id_emissor of this CartaoResponse.


        :param id_emissor: The id_emissor of this CartaoResponse.
        :type: int
        """
        self._id_emissor = id_emissor

    @property
    def id_log(self):
        """
        Gets the id_log of this CartaoResponse.


        :return: The id_log of this CartaoResponse.
        :rtype: str
        """
        return self._id_log

    @id_log.setter
    def id_log(self, id_log):
        """
        Sets the id_log of this CartaoResponse.


        :param id_log: The id_log of this CartaoResponse.
        :type: str
        """
        self._id_log = id_log

    @property
    def id_pessoa_fisica(self):
        """
        Gets the id_pessoa_fisica of this CartaoResponse.


        :return: The id_pessoa_fisica of this CartaoResponse.
        :rtype: int
        """
        return self._id_pessoa_fisica

    @id_pessoa_fisica.setter
    def id_pessoa_fisica(self, id_pessoa_fisica):
        """
        Sets the id_pessoa_fisica of this CartaoResponse.


        :param id_pessoa_fisica: The id_pessoa_fisica of this CartaoResponse.
        :type: int
        """
        self._id_pessoa_fisica = id_pessoa_fisica

    @property
    def id_produto(self):
        """
        Gets the id_produto of this CartaoResponse.


        :return: The id_produto of this CartaoResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this CartaoResponse.


        :param id_produto: The id_produto of this CartaoResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def numero_cartao(self):
        """
        Gets the numero_cartao of this CartaoResponse.


        :return: The numero_cartao of this CartaoResponse.
        :rtype: str
        """
        return self._numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        """
        Sets the numero_cartao of this CartaoResponse.


        :param numero_cartao: The numero_cartao of this CartaoResponse.
        :type: str
        """
        self._numero_cartao = numero_cartao

    @property
    def numero_cartao_real(self):
        """
        Gets the numero_cartao_real of this CartaoResponse.


        :return: The numero_cartao_real of this CartaoResponse.
        :rtype: str
        """
        return self._numero_cartao_real

    @numero_cartao_real.setter
    def numero_cartao_real(self, numero_cartao_real):
        """
        Sets the numero_cartao_real of this CartaoResponse.


        :param numero_cartao_real: The numero_cartao_real of this CartaoResponse.
        :type: str
        """
        self._numero_cartao_real = numero_cartao_real

    @property
    def status_cartao(self):
        """
        Gets the status_cartao of this CartaoResponse.


        :return: The status_cartao of this CartaoResponse.
        :rtype: int
        """
        return self._status_cartao

    @status_cartao.setter
    def status_cartao(self, status_cartao):
        """
        Sets the status_cartao of this CartaoResponse.


        :param status_cartao: The status_cartao of this CartaoResponse.
        :type: int
        """
        self._status_cartao = status_cartao

    @property
    def status_data(self):
        """
        Gets the status_data of this CartaoResponse.


        :return: The status_data of this CartaoResponse.
        :rtype: datetime
        """
        return self._status_data

    @status_data.setter
    def status_data(self, status_data):
        """
        Sets the status_data of this CartaoResponse.


        :param status_data: The status_data of this CartaoResponse.
        :type: datetime
        """
        self._status_data = status_data

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
