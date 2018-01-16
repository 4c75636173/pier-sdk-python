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


class BoletoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BoletoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'numero_do_documento': 'str',
            'data_processamento': 'str',
            'data_documento': 'str',
            'data_vencimento': 'str',
            'data_fechamento': 'str',
            'valor_boleto': 'float',
            'nome_beneficiario': 'str',
            'documento_beneficiario': 'str',
            'agencia': 'str',
            'codigo_beneficiario': 'str',
            'numero_convenio': 'str',
            'digito_codigo_beneficiario': 'str',
            'carteira': 'str',
            'nosso_numero': 'str',
            'digito_nosso_numero': 'str',
            'banco': 'str',
            'aceite': 'bool',
            'especie_do_documento': 'str',
            'especie': 'str',
            'instrucoes': 'list[str]',
            'locais_de_pagamento': 'list[str]',
            'nome_pagador': 'str',
            'documento_pagador': 'str',
            'logradouro_pagador': 'str',
            'bairro_pagador': 'str',
            'cep_pagador': 'str',
            'cidade_pagador': 'str',
            'uf_pagador': 'str',
            'codigo_de_barras': 'str',
            'linha_digitavel': 'str'
        }

        self.attribute_map = {
            'numero_do_documento': 'numeroDoDocumento',
            'data_processamento': 'dataProcessamento',
            'data_documento': 'dataDocumento',
            'data_vencimento': 'dataVencimento',
            'data_fechamento': 'dataFechamento',
            'valor_boleto': 'valorBoleto',
            'nome_beneficiario': 'nomeBeneficiario',
            'documento_beneficiario': 'documentoBeneficiario',
            'agencia': 'agencia',
            'codigo_beneficiario': 'codigoBeneficiario',
            'numero_convenio': 'numeroConvenio',
            'digito_codigo_beneficiario': 'digitoCodigoBeneficiario',
            'carteira': 'carteira',
            'nosso_numero': 'nossoNumero',
            'digito_nosso_numero': 'digitoNossoNumero',
            'banco': 'banco',
            'aceite': 'aceite',
            'especie_do_documento': 'especieDoDocumento',
            'especie': 'especie',
            'instrucoes': 'instrucoes',
            'locais_de_pagamento': 'locaisDePagamento',
            'nome_pagador': 'nomePagador',
            'documento_pagador': 'documentoPagador',
            'logradouro_pagador': 'logradouroPagador',
            'bairro_pagador': 'bairroPagador',
            'cep_pagador': 'cepPagador',
            'cidade_pagador': 'cidadePagador',
            'uf_pagador': 'ufPagador',
            'codigo_de_barras': 'codigoDeBarras',
            'linha_digitavel': 'linhaDigitavel'
        }

        self._numero_do_documento = None
        self._data_processamento = None
        self._data_documento = None
        self._data_vencimento = None
        self._data_fechamento = None
        self._valor_boleto = None
        self._nome_beneficiario = None
        self._documento_beneficiario = None
        self._agencia = None
        self._codigo_beneficiario = None
        self._numero_convenio = None
        self._digito_codigo_beneficiario = None
        self._carteira = None
        self._nosso_numero = None
        self._digito_nosso_numero = None
        self._banco = None
        self._aceite = None
        self._especie_do_documento = None
        self._especie = None
        self._instrucoes = None
        self._locais_de_pagamento = None
        self._nome_pagador = None
        self._documento_pagador = None
        self._logradouro_pagador = None
        self._bairro_pagador = None
        self._cep_pagador = None
        self._cidade_pagador = None
        self._uf_pagador = None
        self._codigo_de_barras = None
        self._linha_digitavel = None

    @property
    def numero_do_documento(self):
        """
        Gets the numero_do_documento of this BoletoResponse.
        N\u00C3\u00BAmero do documento \u00C3\u00A9 o c\u00C3\u00B3digo informado pelo banco para identifica\u00C3\u00A7\u00C3\u00A3o do cliente

        :return: The numero_do_documento of this BoletoResponse.
        :rtype: str
        """
        return self._numero_do_documento

    @numero_do_documento.setter
    def numero_do_documento(self, numero_do_documento):
        """
        Sets the numero_do_documento of this BoletoResponse.
        N\u00C3\u00BAmero do documento \u00C3\u00A9 o c\u00C3\u00B3digo informado pelo banco para identifica\u00C3\u00A7\u00C3\u00A3o do cliente

        :param numero_do_documento: The numero_do_documento of this BoletoResponse.
        :type: str
        """
        self._numero_do_documento = numero_do_documento

    @property
    def data_processamento(self):
        """
        Gets the data_processamento of this BoletoResponse.
        Data do processamento (emiss\u00C3\u00A3o ou faturamento) do boleto

        :return: The data_processamento of this BoletoResponse.
        :rtype: str
        """
        return self._data_processamento

    @data_processamento.setter
    def data_processamento(self, data_processamento):
        """
        Sets the data_processamento of this BoletoResponse.
        Data do processamento (emiss\u00C3\u00A3o ou faturamento) do boleto

        :param data_processamento: The data_processamento of this BoletoResponse.
        :type: str
        """
        self._data_processamento = data_processamento

    @property
    def data_documento(self):
        """
        Gets the data_documento of this BoletoResponse.
        Data do documento (impress\u00C3\u00A3o)

        :return: The data_documento of this BoletoResponse.
        :rtype: str
        """
        return self._data_documento

    @data_documento.setter
    def data_documento(self, data_documento):
        """
        Sets the data_documento of this BoletoResponse.
        Data do documento (impress\u00C3\u00A3o)

        :param data_documento: The data_documento of this BoletoResponse.
        :type: str
        """
        self._data_documento = data_documento

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this BoletoResponse.
        Data do vencimento

        :return: The data_vencimento of this BoletoResponse.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this BoletoResponse.
        Data do vencimento

        :param data_vencimento: The data_vencimento of this BoletoResponse.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def data_fechamento(self):
        """
        Gets the data_fechamento of this BoletoResponse.
        Data do fechamento

        :return: The data_fechamento of this BoletoResponse.
        :rtype: str
        """
        return self._data_fechamento

    @data_fechamento.setter
    def data_fechamento(self, data_fechamento):
        """
        Sets the data_fechamento of this BoletoResponse.
        Data do fechamento

        :param data_fechamento: The data_fechamento of this BoletoResponse.
        :type: str
        """
        self._data_fechamento = data_fechamento

    @property
    def valor_boleto(self):
        """
        Gets the valor_boleto of this BoletoResponse.
        Valor do Boleto.

        :return: The valor_boleto of this BoletoResponse.
        :rtype: float
        """
        return self._valor_boleto

    @valor_boleto.setter
    def valor_boleto(self, valor_boleto):
        """
        Sets the valor_boleto of this BoletoResponse.
        Valor do Boleto.

        :param valor_boleto: The valor_boleto of this BoletoResponse.
        :type: float
        """
        self._valor_boleto = valor_boleto

    @property
    def nome_beneficiario(self):
        """
        Gets the nome_beneficiario of this BoletoResponse.
        Benefici\u00C3\u00A1rio \u00C3\u00A9 a pessoa/empresa que gera o boleto

        :return: The nome_beneficiario of this BoletoResponse.
        :rtype: str
        """
        return self._nome_beneficiario

    @nome_beneficiario.setter
    def nome_beneficiario(self, nome_beneficiario):
        """
        Sets the nome_beneficiario of this BoletoResponse.
        Benefici\u00C3\u00A1rio \u00C3\u00A9 a pessoa/empresa que gera o boleto

        :param nome_beneficiario: The nome_beneficiario of this BoletoResponse.
        :type: str
        """
        self._nome_beneficiario = nome_beneficiario

    @property
    def documento_beneficiario(self):
        """
        Gets the documento_beneficiario of this BoletoResponse.
        Documento do Beneficiario.

        :return: The documento_beneficiario of this BoletoResponse.
        :rtype: str
        """
        return self._documento_beneficiario

    @documento_beneficiario.setter
    def documento_beneficiario(self, documento_beneficiario):
        """
        Sets the documento_beneficiario of this BoletoResponse.
        Documento do Beneficiario.

        :param documento_beneficiario: The documento_beneficiario of this BoletoResponse.
        :type: str
        """
        self._documento_beneficiario = documento_beneficiario

    @property
    def agencia(self):
        """
        Gets the agencia of this BoletoResponse.
        Ag\u00C3\u00AAncia.

        :return: The agencia of this BoletoResponse.
        :rtype: str
        """
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        """
        Sets the agencia of this BoletoResponse.
        Ag\u00C3\u00AAncia.

        :param agencia: The agencia of this BoletoResponse.
        :type: str
        """
        self._agencia = agencia

    @property
    def codigo_beneficiario(self):
        """
        Gets the codigo_beneficiario of this BoletoResponse.
        C\u00C3\u00B3digo do benefici\u00C3\u00A1rio

        :return: The codigo_beneficiario of this BoletoResponse.
        :rtype: str
        """
        return self._codigo_beneficiario

    @codigo_beneficiario.setter
    def codigo_beneficiario(self, codigo_beneficiario):
        """
        Sets the codigo_beneficiario of this BoletoResponse.
        C\u00C3\u00B3digo do benefici\u00C3\u00A1rio

        :param codigo_beneficiario: The codigo_beneficiario of this BoletoResponse.
        :type: str
        """
        self._codigo_beneficiario = codigo_beneficiario

    @property
    def numero_convenio(self):
        """
        Gets the numero_convenio of this BoletoResponse.
        N\u00C3\u00BAmero do conv\u00C3\u00AAnio fornecido pelo banco \u00C3\u00A9 o c\u00C3\u00B3digo que identifica um emissor junto ao seu banco para associar seus boletos.

        :return: The numero_convenio of this BoletoResponse.
        :rtype: str
        """
        return self._numero_convenio

    @numero_convenio.setter
    def numero_convenio(self, numero_convenio):
        """
        Sets the numero_convenio of this BoletoResponse.
        N\u00C3\u00BAmero do conv\u00C3\u00AAnio fornecido pelo banco \u00C3\u00A9 o c\u00C3\u00B3digo que identifica um emissor junto ao seu banco para associar seus boletos.

        :param numero_convenio: The numero_convenio of this BoletoResponse.
        :type: str
        """
        self._numero_convenio = numero_convenio

    @property
    def digito_codigo_beneficiario(self):
        """
        Gets the digito_codigo_beneficiario of this BoletoResponse.
        D\u00C3\u00ADgito do c\u00C3\u00B3digo do benefici\u00C3\u00A1rio

        :return: The digito_codigo_beneficiario of this BoletoResponse.
        :rtype: str
        """
        return self._digito_codigo_beneficiario

    @digito_codigo_beneficiario.setter
    def digito_codigo_beneficiario(self, digito_codigo_beneficiario):
        """
        Sets the digito_codigo_beneficiario of this BoletoResponse.
        D\u00C3\u00ADgito do c\u00C3\u00B3digo do benefici\u00C3\u00A1rio

        :param digito_codigo_beneficiario: The digito_codigo_beneficiario of this BoletoResponse.
        :type: str
        """
        self._digito_codigo_beneficiario = digito_codigo_beneficiario

    @property
    def carteira(self):
        """
        Gets the carteira of this BoletoResponse.
        Carteira \u00C3\u00A9 o c\u00C3\u00B3digo informado pelo banco pra identifica\u00C3\u00A7\u00C3\u00A3o do tipo do boleto

        :return: The carteira of this BoletoResponse.
        :rtype: str
        """
        return self._carteira

    @carteira.setter
    def carteira(self, carteira):
        """
        Sets the carteira of this BoletoResponse.
        Carteira \u00C3\u00A9 o c\u00C3\u00B3digo informado pelo banco pra identifica\u00C3\u00A7\u00C3\u00A3o do tipo do boleto

        :param carteira: The carteira of this BoletoResponse.
        :type: str
        """
        self._carteira = carteira

    @property
    def nosso_numero(self):
        """
        Gets the nosso_numero of this BoletoResponse.
        Nosso n\u00C3\u00BAmero \u00C3\u00A9 o c\u00C3\u00B3digo que o benefici\u00C3\u00A1rio escolhe para manter controle sobre seus boletos. Esse valor serve para o cedente identificar quais boletos foram pagos ou n\u00C3\u00A3o. Recomenda-se o uso de n\u00C3\u00BAmeros sequ\u00C3\u00AAnciais, na gera\u00C3\u00A7\u00C3\u00A3o de diversos boletos, para facilitar a identifica\u00C3\u00A7\u00C3\u00A3o dos boletos pagos

        :return: The nosso_numero of this BoletoResponse.
        :rtype: str
        """
        return self._nosso_numero

    @nosso_numero.setter
    def nosso_numero(self, nosso_numero):
        """
        Sets the nosso_numero of this BoletoResponse.
        Nosso n\u00C3\u00BAmero \u00C3\u00A9 o c\u00C3\u00B3digo que o benefici\u00C3\u00A1rio escolhe para manter controle sobre seus boletos. Esse valor serve para o cedente identificar quais boletos foram pagos ou n\u00C3\u00A3o. Recomenda-se o uso de n\u00C3\u00BAmeros sequ\u00C3\u00AAnciais, na gera\u00C3\u00A7\u00C3\u00A3o de diversos boletos, para facilitar a identifica\u00C3\u00A7\u00C3\u00A3o dos boletos pagos

        :param nosso_numero: The nosso_numero of this BoletoResponse.
        :type: str
        """
        self._nosso_numero = nosso_numero

    @property
    def digito_nosso_numero(self):
        """
        Gets the digito_nosso_numero of this BoletoResponse.
        D\u00C3\u00ADgito do nosso n\u00C3\u00BAmero

        :return: The digito_nosso_numero of this BoletoResponse.
        :rtype: str
        """
        return self._digito_nosso_numero

    @digito_nosso_numero.setter
    def digito_nosso_numero(self, digito_nosso_numero):
        """
        Sets the digito_nosso_numero of this BoletoResponse.
        D\u00C3\u00ADgito do nosso n\u00C3\u00BAmero

        :param digito_nosso_numero: The digito_nosso_numero of this BoletoResponse.
        :type: str
        """
        self._digito_nosso_numero = digito_nosso_numero

    @property
    def banco(self):
        """
        Gets the banco of this BoletoResponse.
        Banco

        :return: The banco of this BoletoResponse.
        :rtype: str
        """
        return self._banco

    @banco.setter
    def banco(self, banco):
        """
        Sets the banco of this BoletoResponse.
        Banco

        :param banco: The banco of this BoletoResponse.
        :type: str
        """
        self._banco = banco

    @property
    def aceite(self):
        """
        Gets the aceite of this BoletoResponse.
        Aceite informa ao banco se deve aceitar o boleto ap\u00C3\u00B3s a data de vencimento (padr\u00C3\u00A3o: \"N\")

        :return: The aceite of this BoletoResponse.
        :rtype: bool
        """
        return self._aceite

    @aceite.setter
    def aceite(self, aceite):
        """
        Sets the aceite of this BoletoResponse.
        Aceite informa ao banco se deve aceitar o boleto ap\u00C3\u00B3s a data de vencimento (padr\u00C3\u00A3o: \"N\")

        :param aceite: The aceite of this BoletoResponse.
        :type: bool
        """
        self._aceite = aceite

    @property
    def especie_do_documento(self):
        """
        Gets the especie_do_documento of this BoletoResponse.
        Esp\u00C3\u00A9cie do documento \u00C3\u00A9 o identificador do tipo de boleto (padr\u00C3\u00A3o: \"DV\")

        :return: The especie_do_documento of this BoletoResponse.
        :rtype: str
        """
        return self._especie_do_documento

    @especie_do_documento.setter
    def especie_do_documento(self, especie_do_documento):
        """
        Sets the especie_do_documento of this BoletoResponse.
        Esp\u00C3\u00A9cie do documento \u00C3\u00A9 o identificador do tipo de boleto (padr\u00C3\u00A3o: \"DV\")

        :param especie_do_documento: The especie_do_documento of this BoletoResponse.
        :type: str
        """
        self._especie_do_documento = especie_do_documento

    @property
    def especie(self):
        """
        Gets the especie of this BoletoResponse.
        Esp\u00C3\u00A9cie \u00C3\u00A9 o identificador da moeda do boleto (padr\u00C3\u00A3o: \"R$\")

        :return: The especie of this BoletoResponse.
        :rtype: str
        """
        return self._especie

    @especie.setter
    def especie(self, especie):
        """
        Sets the especie of this BoletoResponse.
        Esp\u00C3\u00A9cie \u00C3\u00A9 o identificador da moeda do boleto (padr\u00C3\u00A3o: \"R$\")

        :param especie: The especie of this BoletoResponse.
        :type: str
        """
        self._especie = especie

    @property
    def instrucoes(self):
        """
        Gets the instrucoes of this BoletoResponse.
        Instru\u00C3\u00A7\u00C3\u00B5es para o benefici\u00C3\u00A1rio

        :return: The instrucoes of this BoletoResponse.
        :rtype: list[str]
        """
        return self._instrucoes

    @instrucoes.setter
    def instrucoes(self, instrucoes):
        """
        Sets the instrucoes of this BoletoResponse.
        Instru\u00C3\u00A7\u00C3\u00B5es para o benefici\u00C3\u00A1rio

        :param instrucoes: The instrucoes of this BoletoResponse.
        :type: list[str]
        """
        self._instrucoes = instrucoes

    @property
    def locais_de_pagamento(self):
        """
        Gets the locais_de_pagamento of this BoletoResponse.
        Locais de pagamento

        :return: The locais_de_pagamento of this BoletoResponse.
        :rtype: list[str]
        """
        return self._locais_de_pagamento

    @locais_de_pagamento.setter
    def locais_de_pagamento(self, locais_de_pagamento):
        """
        Sets the locais_de_pagamento of this BoletoResponse.
        Locais de pagamento

        :param locais_de_pagamento: The locais_de_pagamento of this BoletoResponse.
        :type: list[str]
        """
        self._locais_de_pagamento = locais_de_pagamento

    @property
    def nome_pagador(self):
        """
        Gets the nome_pagador of this BoletoResponse.
        Pagador \u00C3\u00A9 a pessoa/empresa que deve pagar o boleto

        :return: The nome_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._nome_pagador

    @nome_pagador.setter
    def nome_pagador(self, nome_pagador):
        """
        Sets the nome_pagador of this BoletoResponse.
        Pagador \u00C3\u00A9 a pessoa/empresa que deve pagar o boleto

        :param nome_pagador: The nome_pagador of this BoletoResponse.
        :type: str
        """
        self._nome_pagador = nome_pagador

    @property
    def documento_pagador(self):
        """
        Gets the documento_pagador of this BoletoResponse.
        Documento do pagador (CPF ou CNPJ)

        :return: The documento_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._documento_pagador

    @documento_pagador.setter
    def documento_pagador(self, documento_pagador):
        """
        Sets the documento_pagador of this BoletoResponse.
        Documento do pagador (CPF ou CNPJ)

        :param documento_pagador: The documento_pagador of this BoletoResponse.
        :type: str
        """
        self._documento_pagador = documento_pagador

    @property
    def logradouro_pagador(self):
        """
        Gets the logradouro_pagador of this BoletoResponse.
        Logradouro do pagador

        :return: The logradouro_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._logradouro_pagador

    @logradouro_pagador.setter
    def logradouro_pagador(self, logradouro_pagador):
        """
        Sets the logradouro_pagador of this BoletoResponse.
        Logradouro do pagador

        :param logradouro_pagador: The logradouro_pagador of this BoletoResponse.
        :type: str
        """
        self._logradouro_pagador = logradouro_pagador

    @property
    def bairro_pagador(self):
        """
        Gets the bairro_pagador of this BoletoResponse.
        Bairro do pagador

        :return: The bairro_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._bairro_pagador

    @bairro_pagador.setter
    def bairro_pagador(self, bairro_pagador):
        """
        Sets the bairro_pagador of this BoletoResponse.
        Bairro do pagador

        :param bairro_pagador: The bairro_pagador of this BoletoResponse.
        :type: str
        """
        self._bairro_pagador = bairro_pagador

    @property
    def cep_pagador(self):
        """
        Gets the cep_pagador of this BoletoResponse.
        CEP do pagador

        :return: The cep_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._cep_pagador

    @cep_pagador.setter
    def cep_pagador(self, cep_pagador):
        """
        Sets the cep_pagador of this BoletoResponse.
        CEP do pagador

        :param cep_pagador: The cep_pagador of this BoletoResponse.
        :type: str
        """
        self._cep_pagador = cep_pagador

    @property
    def cidade_pagador(self):
        """
        Gets the cidade_pagador of this BoletoResponse.
        Cidade do pagador

        :return: The cidade_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._cidade_pagador

    @cidade_pagador.setter
    def cidade_pagador(self, cidade_pagador):
        """
        Sets the cidade_pagador of this BoletoResponse.
        Cidade do pagador

        :param cidade_pagador: The cidade_pagador of this BoletoResponse.
        :type: str
        """
        self._cidade_pagador = cidade_pagador

    @property
    def uf_pagador(self):
        """
        Gets the uf_pagador of this BoletoResponse.
        Unidade federativa do pagador

        :return: The uf_pagador of this BoletoResponse.
        :rtype: str
        """
        return self._uf_pagador

    @uf_pagador.setter
    def uf_pagador(self, uf_pagador):
        """
        Sets the uf_pagador of this BoletoResponse.
        Unidade federativa do pagador

        :param uf_pagador: The uf_pagador of this BoletoResponse.
        :type: str
        """
        self._uf_pagador = uf_pagador

    @property
    def codigo_de_barras(self):
        """
        Gets the codigo_de_barras of this BoletoResponse.
        Valor num\u00C3\u00A9rico do c\u00C3\u00B3digo de barras

        :return: The codigo_de_barras of this BoletoResponse.
        :rtype: str
        """
        return self._codigo_de_barras

    @codigo_de_barras.setter
    def codigo_de_barras(self, codigo_de_barras):
        """
        Sets the codigo_de_barras of this BoletoResponse.
        Valor num\u00C3\u00A9rico do c\u00C3\u00B3digo de barras

        :param codigo_de_barras: The codigo_de_barras of this BoletoResponse.
        :type: str
        """
        self._codigo_de_barras = codigo_de_barras

    @property
    def linha_digitavel(self):
        """
        Gets the linha_digitavel of this BoletoResponse.
        Linha digit\u00C3\u00A1vel formatada

        :return: The linha_digitavel of this BoletoResponse.
        :rtype: str
        """
        return self._linha_digitavel

    @linha_digitavel.setter
    def linha_digitavel(self, linha_digitavel):
        """
        Sets the linha_digitavel of this BoletoResponse.
        Linha digit\u00C3\u00A1vel formatada

        :param linha_digitavel: The linha_digitavel of this BoletoResponse.
        :type: str
        """
        self._linha_digitavel = linha_digitavel

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
