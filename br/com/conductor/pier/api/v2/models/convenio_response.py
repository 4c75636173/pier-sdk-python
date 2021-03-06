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


class ConvenioResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConvenioResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'banco': 'int',
            'agencia': 'int',
            'conta_corrente': 'str',
            'especie': 'str',
            'numero_convenio': 'float',
            'carteira': 'int',
            'codigo_cedente': 'str',
            'especie_tipo': 'str',
            'especie_documento': 'str',
            'aceite': 'str',
            'instrucoes': 'str',
            'local_pagamento1': 'str',
            'local_pagamento2': 'str',
            'endereco_cobranca_emissor': 'str',
            'nome_beneficiario': 'str',
            'cnpj_beneficiario': 'str',
            'operador': 'str',
            'data': 'str',
            'maquina': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'banco': 'banco',
            'agencia': 'agencia',
            'conta_corrente': 'contaCorrente',
            'especie': 'especie',
            'numero_convenio': 'numeroConvenio',
            'carteira': 'carteira',
            'codigo_cedente': 'codigoCedente',
            'especie_tipo': 'especieTipo',
            'especie_documento': 'especieDocumento',
            'aceite': 'aceite',
            'instrucoes': 'instrucoes',
            'local_pagamento1': 'localPagamento1',
            'local_pagamento2': 'localPagamento2',
            'endereco_cobranca_emissor': 'enderecoCobrancaEmissor',
            'nome_beneficiario': 'nomeBeneficiario',
            'cnpj_beneficiario': 'cnpjBeneficiario',
            'operador': 'operador',
            'data': 'data',
            'maquina': 'maquina'
        }

        self._id = None
        self._banco = None
        self._agencia = None
        self._conta_corrente = None
        self._especie = None
        self._numero_convenio = None
        self._carteira = None
        self._codigo_cedente = None
        self._especie_tipo = None
        self._especie_documento = None
        self._aceite = None
        self._instrucoes = None
        self._local_pagamento1 = None
        self._local_pagamento2 = None
        self._endereco_cobranca_emissor = None
        self._nome_beneficiario = None
        self._cnpj_beneficiario = None
        self._operador = None
        self._data = None
        self._maquina = None

    @property
    def id(self):
        """
        Gets the id of this ConvenioResponse.
        Id do conv\u00EAnio.

        :return: The id of this ConvenioResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConvenioResponse.
        Id do conv\u00EAnio.

        :param id: The id of this ConvenioResponse.
        :type: int
        """
        self._id = id

    @property
    def banco(self):
        """
        Gets the banco of this ConvenioResponse.
        Identifica\u00E7\u00E3o do banco.

        :return: The banco of this ConvenioResponse.
        :rtype: int
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this ConvenioResponse.
        Identifica\u00E7\u00E3o do banco.

        :param banco: The banco of this ConvenioResponse.
        :type: int
        """
        self._banco = banco

    @property
    def agencia(self):
        """
        Gets the agencia of this ConvenioResponse.
        N\u00FAmero da ag\u00EAncia.

        :return: The agencia of this ConvenioResponse.
        :rtype: int
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        """
        Sets the agencia of this ConvenioResponse.
        N\u00FAmero da ag\u00EAncia.

        :param agencia: The agencia of this ConvenioResponse.
        :type: int
        """
        self._agencia = agencia

    @property
    def conta_corrente(self):
        """
        Gets the conta_corrente of this ConvenioResponse.
        Conta corrente.

        :return: The conta_corrente of this ConvenioResponse.
        :rtype: str
        """
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta_corrente):
        """
        Sets the conta_corrente of this ConvenioResponse.
        Conta corrente.

        :param conta_corrente: The conta_corrente of this ConvenioResponse.
        :type: str
        """
        self._conta_corrente = conta_corrente

    @property
    def especie(self):
        """
        Gets the especie of this ConvenioResponse.
        C\u00F3digo do tipo de esp\u00E9cie do documento.

        :return: The especie of this ConvenioResponse.
        :rtype: str
        """
        return self._especie

    @especie.setter
    def especie(self, especie):
        """
        Sets the especie of this ConvenioResponse.
        C\u00F3digo do tipo de esp\u00E9cie do documento.

        :param especie: The especie of this ConvenioResponse.
        :type: str
        """
        self._especie = especie

    @property
    def numero_convenio(self):
        """
        Gets the numero_convenio of this ConvenioResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do conv\u00EAnio.

        :return: The numero_convenio of this ConvenioResponse.
        :rtype: float
        """
        return self._numero_convenio

    @numero_convenio.setter
    def numero_convenio(self, numero_convenio):
        """
        Sets the numero_convenio of this ConvenioResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do conv\u00EAnio.

        :param numero_convenio: The numero_convenio of this ConvenioResponse.
        :type: float
        """
        self._numero_convenio = numero_convenio

    @property
    def carteira(self):
        """
        Gets the carteira of this ConvenioResponse.
        C\u00F3digo da carteira de cobran\u00E7a.

        :return: The carteira of this ConvenioResponse.
        :rtype: int
        """
        return self._carteira

    @carteira.setter
    def carteira(self, carteira):
        """
        Sets the carteira of this ConvenioResponse.
        C\u00F3digo da carteira de cobran\u00E7a.

        :param carteira: The carteira of this ConvenioResponse.
        :type: int
        """
        self._carteira = carteira

    @property
    def codigo_cedente(self):
        """
        Gets the codigo_cedente of this ConvenioResponse.
        C\u00F3digo do cedente.

        :return: The codigo_cedente of this ConvenioResponse.
        :rtype: str
        """
        return self._codigo_cedente

    @codigo_cedente.setter
    def codigo_cedente(self, codigo_cedente):
        """
        Sets the codigo_cedente of this ConvenioResponse.
        C\u00F3digo do cedente.

        :param codigo_cedente: The codigo_cedente of this ConvenioResponse.
        :type: str
        """
        self._codigo_cedente = codigo_cedente

    @property
    def especie_tipo(self):
        """
        Gets the especie_tipo of this ConvenioResponse.
        Tipo de esp\u00E9cie de t\u00EDtulo de cr\u00E9dito.

        :return: The especie_tipo of this ConvenioResponse.
        :rtype: str
        """
        return self._especie_tipo

    @especie_tipo.setter
    def especie_tipo(self, especie_tipo):
        """
        Sets the especie_tipo of this ConvenioResponse.
        Tipo de esp\u00E9cie de t\u00EDtulo de cr\u00E9dito.

        :param especie_tipo: The especie_tipo of this ConvenioResponse.
        :type: str
        """
        self._especie_tipo = especie_tipo

    @property
    def especie_documento(self):
        """
        Gets the especie_documento of this ConvenioResponse.
        Esp\u00E9cie do documento.

        :return: The especie_documento of this ConvenioResponse.
        :rtype: str
        """
        return self._especie_documento

    @especie_documento.setter
    def especie_documento(self, especie_documento):
        """
        Sets the especie_documento of this ConvenioResponse.
        Esp\u00E9cie do documento.

        :param especie_documento: The especie_documento of this ConvenioResponse.
        :type: str
        """
        self._especie_documento = especie_documento

    @property
    def aceite(self):
        """
        Gets the aceite of this ConvenioResponse.
        Indica se o pagador assinou o documento de cobran\u00E7a que originou o boleto. O padr\u00E3o \u00E9 usar \"N\".

        :return: The aceite of this ConvenioResponse.
        :rtype: str
        """
        return self._aceite

    @aceite.setter
    def aceite(self, aceite):
        """
        Sets the aceite of this ConvenioResponse.
        Indica se o pagador assinou o documento de cobran\u00E7a que originou o boleto. O padr\u00E3o \u00E9 usar \"N\".

        :param aceite: The aceite of this ConvenioResponse.
        :type: str
        """
        self._aceite = aceite

    @property
    def instrucoes(self):
        """
        Gets the instrucoes of this ConvenioResponse.
        Instru\u00E7\u00F5es para pagamento.

        :return: The instrucoes of this ConvenioResponse.
        :rtype: str
        """
        return self._instrucoes

    @instrucoes.setter
    def instrucoes(self, instrucoes):
        """
        Sets the instrucoes of this ConvenioResponse.
        Instru\u00E7\u00F5es para pagamento.

        :param instrucoes: The instrucoes of this ConvenioResponse.
        :type: str
        """
        self._instrucoes = instrucoes

    @property
    def local_pagamento1(self):
        """
        Gets the local_pagamento1 of this ConvenioResponse.
        Local preferencial onde pode ser efetuado o pagamento.

        :return: The local_pagamento1 of this ConvenioResponse.
        :rtype: str
        """
        return self._local_pagamento1

    @local_pagamento1.setter
    def local_pagamento1(self, local_pagamento1):
        """
        Sets the local_pagamento1 of this ConvenioResponse.
        Local preferencial onde pode ser efetuado o pagamento.

        :param local_pagamento1: The local_pagamento1 of this ConvenioResponse.
        :type: str
        """
        self._local_pagamento1 = local_pagamento1

    @property
    def local_pagamento2(self):
        """
        Gets the local_pagamento2 of this ConvenioResponse.
        Local para pagamento (campo adicional).

        :return: The local_pagamento2 of this ConvenioResponse.
        :rtype: str
        """
        return self._local_pagamento2

    @local_pagamento2.setter
    def local_pagamento2(self, local_pagamento2):
        """
        Sets the local_pagamento2 of this ConvenioResponse.
        Local para pagamento (campo adicional).

        :param local_pagamento2: The local_pagamento2 of this ConvenioResponse.
        :type: str
        """
        self._local_pagamento2 = local_pagamento2

    @property
    def endereco_cobranca_emissor(self):
        """
        Gets the endereco_cobranca_emissor of this ConvenioResponse.
        Endere\u00E7o de cobran\u00E7a do emissor.

        :return: The endereco_cobranca_emissor of this ConvenioResponse.
        :rtype: str
        """
        return self._endereco_cobranca_emissor

    @endereco_cobranca_emissor.setter
    def endereco_cobranca_emissor(self, endereco_cobranca_emissor):
        """
        Sets the endereco_cobranca_emissor of this ConvenioResponse.
        Endere\u00E7o de cobran\u00E7a do emissor.

        :param endereco_cobranca_emissor: The endereco_cobranca_emissor of this ConvenioResponse.
        :type: str
        """
        self._endereco_cobranca_emissor = endereco_cobranca_emissor

    @property
    def nome_beneficiario(self):
        """
        Gets the nome_beneficiario of this ConvenioResponse.
        Nome do benefici\u00E1rio/cedente da cobran\u00E7a.

        :return: The nome_beneficiario of this ConvenioResponse.
        :rtype: str
        """
        return self._nome_beneficiario

    @nome_beneficiario.setter
    def nome_beneficiario(self, nome_beneficiario):
        """
        Sets the nome_beneficiario of this ConvenioResponse.
        Nome do benefici\u00E1rio/cedente da cobran\u00E7a.

        :param nome_beneficiario: The nome_beneficiario of this ConvenioResponse.
        :type: str
        """
        self._nome_beneficiario = nome_beneficiario

    @property
    def cnpj_beneficiario(self):
        """
        Gets the cnpj_beneficiario of this ConvenioResponse.
        CNPJ do benefici\u00E1rio/cedente da cobran\u00E7a.

        :return: The cnpj_beneficiario of this ConvenioResponse.
        :rtype: str
        """
        return self._cnpj_beneficiario

    @cnpj_beneficiario.setter
    def cnpj_beneficiario(self, cnpj_beneficiario):
        """
        Sets the cnpj_beneficiario of this ConvenioResponse.
        CNPJ do benefici\u00E1rio/cedente da cobran\u00E7a.

        :param cnpj_beneficiario: The cnpj_beneficiario of this ConvenioResponse.
        :type: str
        """
        self._cnpj_beneficiario = cnpj_beneficiario

    @property
    def operador(self):
        """
        Gets the operador of this ConvenioResponse.
        Usu\u00E1rio responsavel pelo cadastro e/ou altera\u00E7\u00E3o do conv\u00EAnio.

        :return: The operador of this ConvenioResponse.
        :rtype: str
        """
        return self._operador

    @operador.setter
    def operador(self, operador):
        """
        Sets the operador of this ConvenioResponse.
        Usu\u00E1rio responsavel pelo cadastro e/ou altera\u00E7\u00E3o do conv\u00EAnio.

        :param operador: The operador of this ConvenioResponse.
        :type: str
        """
        self._operador = operador

    @property
    def data(self):
        """
        Gets the data of this ConvenioResponse.
        Data de cadastro/altera\u00E7\u00E3o do conv\u00EAnio.

        :return: The data of this ConvenioResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ConvenioResponse.
        Data de cadastro/altera\u00E7\u00E3o do conv\u00EAnio.

        :param data: The data of this ConvenioResponse.
        :type: str
        """
        self._data = data

    @property
    def maquina(self):
        """
        Gets the maquina of this ConvenioResponse.
        M\u00E1quina pela qual foi realizado o cadastro ou altera\u00E7\u00E3o.

        :return: The maquina of this ConvenioResponse.
        :rtype: str
        """
        return self._maquina

    @maquina.setter
    def maquina(self, maquina):
        """
        Sets the maquina of this ConvenioResponse.
        M\u00E1quina pela qual foi realizado o cadastro ou altera\u00E7\u00E3o.

        :param maquina: The maquina of this ConvenioResponse.
        :type: str
        """
        self._maquina = maquina

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

