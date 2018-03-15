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


class TransacaoNaoProcessadaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TransacaoNaoProcessadaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_tipo_transacao_nao_processada': 'int',
            'descricao_tipo_transacao_nao_processada': 'str',
            'descricao_abreviada': 'str',
            'id_conta': 'int',
            'cartao_mascarado': 'str',
            'nome_portador': 'str',
            'data_origem': 'str',
            'data_faturamento': 'str',
            'data_vencimento': 'str',
            'modo_entrada_transacao': 'str',
            'valor_taxa_embarque': 'float',
            'valor_entrada': 'float',
            'valor_brl': 'float',
            'valor_usd': 'float',
            'cotacao_usd': 'float',
            'data_cotacao_usd': 'str',
            'codigo_moeda_origem': 'str',
            'codigo_moeda_destino': 'str',
            'codigo_autorizacao': 'str',
            'codigo_referencia': 'str',
            'codigo_terminal': 'str',
            'codigo_mcc': 'int',
            'grupo_mcc': 'int',
            'grupo_descricao_mcc': 'str',
            'id_estabelecimento': 'int',
            'nome_estabelecimento': 'str',
            'nome_fantasia_estabelecimento': 'str',
            'localidade_estabelecimento': 'str',
            'plano_parcelamento': 'int',
            'numero_parcela': 'int',
            'detalhes_transacao': 'str',
            'flag_credito': 'int',
            'flag_faturado': 'int',
            'flag_estorno': 'int',
            'id_transacao_estorno': 'int',
            'status': 'int'
        }

        self.attribute_map = {
            'id_tipo_transacao_nao_processada': 'idTipoTransacaoNaoProcessada',
            'descricao_tipo_transacao_nao_processada': 'descricaoTipoTransacaoNaoProcessada',
            'descricao_abreviada': 'descricaoAbreviada',
            'id_conta': 'idConta',
            'cartao_mascarado': 'cartaoMascarado',
            'nome_portador': 'nomePortador',
            'data_origem': 'dataOrigem',
            'data_faturamento': 'dataFaturamento',
            'data_vencimento': 'dataVencimento',
            'modo_entrada_transacao': 'modoEntradaTransacao',
            'valor_taxa_embarque': 'valorTaxaEmbarque',
            'valor_entrada': 'valorEntrada',
            'valor_brl': 'valorBRL',
            'valor_usd': 'valorUSD',
            'cotacao_usd': 'cotacaoUSD',
            'data_cotacao_usd': 'dataCotacaoUSD',
            'codigo_moeda_origem': 'codigoMoedaOrigem',
            'codigo_moeda_destino': 'codigoMoedaDestino',
            'codigo_autorizacao': 'codigoAutorizacao',
            'codigo_referencia': 'codigoReferencia',
            'codigo_terminal': 'codigoTerminal',
            'codigo_mcc': 'codigoMCC',
            'grupo_mcc': 'grupoMCC',
            'grupo_descricao_mcc': 'grupoDescricaoMCC',
            'id_estabelecimento': 'idEstabelecimento',
            'nome_estabelecimento': 'nomeEstabelecimento',
            'nome_fantasia_estabelecimento': 'nomeFantasiaEstabelecimento',
            'localidade_estabelecimento': 'localidadeEstabelecimento',
            'plano_parcelamento': 'planoParcelamento',
            'numero_parcela': 'numeroParcela',
            'detalhes_transacao': 'detalhesTransacao',
            'flag_credito': 'flagCredito',
            'flag_faturado': 'flagFaturado',
            'flag_estorno': 'flagEstorno',
            'id_transacao_estorno': 'idTransacaoEstorno',
            'status': 'status'
        }

        self._id_tipo_transacao_nao_processada = None
        self._descricao_tipo_transacao_nao_processada = None
        self._descricao_abreviada = None
        self._id_conta = None
        self._cartao_mascarado = None
        self._nome_portador = None
        self._data_origem = None
        self._data_faturamento = None
        self._data_vencimento = None
        self._modo_entrada_transacao = None
        self._valor_taxa_embarque = None
        self._valor_entrada = None
        self._valor_brl = None
        self._valor_usd = None
        self._cotacao_usd = None
        self._data_cotacao_usd = None
        self._codigo_moeda_origem = None
        self._codigo_moeda_destino = None
        self._codigo_autorizacao = None
        self._codigo_referencia = None
        self._codigo_terminal = None
        self._codigo_mcc = None
        self._grupo_mcc = None
        self._grupo_descricao_mcc = None
        self._id_estabelecimento = None
        self._nome_estabelecimento = None
        self._nome_fantasia_estabelecimento = None
        self._localidade_estabelecimento = None
        self._plano_parcelamento = None
        self._numero_parcela = None
        self._detalhes_transacao = None
        self._flag_credito = None
        self._flag_faturado = None
        self._flag_estorno = None
        self._id_transacao_estorno = None
        self._status = None

    @property
    def id_tipo_transacao_nao_processada(self):
        """
        Gets the id_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Tipo da Transa\u00E7\u00E3o.

        :return: The id_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._id_tipo_transacao_nao_processada

    @id_tipo_transacao_nao_processada.setter
    def id_tipo_transacao_nao_processada(self, id_tipo_transacao_nao_processada):
        """
        Sets the id_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Tipo da Transa\u00E7\u00E3o.

        :param id_tipo_transacao_nao_processada: The id_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._id_tipo_transacao_nao_processada = id_tipo_transacao_nao_processada

    @property
    def descricao_tipo_transacao_nao_processada(self):
        """
        Gets the descricao_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o do Tipo da Transa\u00E7\u00E3o n\u00E3o Processada.

        :return: The descricao_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._descricao_tipo_transacao_nao_processada

    @descricao_tipo_transacao_nao_processada.setter
    def descricao_tipo_transacao_nao_processada(self, descricao_tipo_transacao_nao_processada):
        """
        Sets the descricao_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o do Tipo da Transa\u00E7\u00E3o n\u00E3o Processada.

        :param descricao_tipo_transacao_nao_processada: The descricao_tipo_transacao_nao_processada of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._descricao_tipo_transacao_nao_processada = descricao_tipo_transacao_nao_processada

    @property
    def descricao_abreviada(self):
        """
        Gets the descricao_abreviada of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o Abreviada da Transa\u00E7\u00E3o.

        :return: The descricao_abreviada of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._descricao_abreviada

    @descricao_abreviada.setter
    def descricao_abreviada(self, descricao_abreviada):
        """
        Sets the descricao_abreviada of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o Abreviada da Transa\u00E7\u00E3o.

        :param descricao_abreviada: The descricao_abreviada of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._descricao_abreviada = descricao_abreviada

    @property
    def id_conta(self):
        """
        Gets the id_conta of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Conta (id).

        :return: The id_conta of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Conta (id).

        :param id_conta: The id_conta of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def cartao_mascarado(self):
        """
        Gets the cartao_mascarado of this TransacaoNaoProcessadaResponse.
        N\u00FAmero do Cart\u00E3o em Formato 0000XXXXXXXX0000.

        :return: The cartao_mascarado of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._cartao_mascarado

    @cartao_mascarado.setter
    def cartao_mascarado(self, cartao_mascarado):
        """
        Sets the cartao_mascarado of this TransacaoNaoProcessadaResponse.
        N\u00FAmero do Cart\u00E3o em Formato 0000XXXXXXXX0000.

        :param cartao_mascarado: The cartao_mascarado of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._cartao_mascarado = cartao_mascarado

    @property
    def nome_portador(self):
        """
        Gets the nome_portador of this TransacaoNaoProcessadaResponse.
        Nome completo do Portador do Cart\u00E3o.

        :return: The nome_portador of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._nome_portador

    @nome_portador.setter
    def nome_portador(self, nome_portador):
        """
        Sets the nome_portador of this TransacaoNaoProcessadaResponse.
        Nome completo do Portador do Cart\u00E3o.

        :param nome_portador: The nome_portador of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._nome_portador = nome_portador

    @property
    def data_origem(self):
        """
        Gets the data_origem of this TransacaoNaoProcessadaResponse.
        Data em que a Transa\u00E7\u00E3o foi realizada.

        :return: The data_origem of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._data_origem

    @data_origem.setter
    def data_origem(self, data_origem):
        """
        Sets the data_origem of this TransacaoNaoProcessadaResponse.
        Data em que a Transa\u00E7\u00E3o foi realizada.

        :param data_origem: The data_origem of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._data_origem = data_origem

    @property
    def data_faturamento(self):
        """
        Gets the data_faturamento of this TransacaoNaoProcessadaResponse.
        Data de Faturamento da Transa\u00E7\u00E3o.

        :return: The data_faturamento of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._data_faturamento

    @data_faturamento.setter
    def data_faturamento(self, data_faturamento):
        """
        Sets the data_faturamento of this TransacaoNaoProcessadaResponse.
        Data de Faturamento da Transa\u00E7\u00E3o.

        :param data_faturamento: The data_faturamento of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._data_faturamento = data_faturamento

    @property
    def data_vencimento(self):
        """
        Gets the data_vencimento of this TransacaoNaoProcessadaResponse.
        Data de Vencimento da Fatura.

        :return: The data_vencimento of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        """
        Sets the data_vencimento of this TransacaoNaoProcessadaResponse.
        Data de Vencimento da Fatura.

        :param data_vencimento: The data_vencimento of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._data_vencimento = data_vencimento

    @property
    def modo_entrada_transacao(self):
        """
        Gets the modo_entrada_transacao of this TransacaoNaoProcessadaResponse.
        Descreve o modo utilizado para realizar a leitura dos dados do cart\u00E3o para realizar a Transa\u00E7\u00E3o.

        :return: The modo_entrada_transacao of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._modo_entrada_transacao

    @modo_entrada_transacao.setter
    def modo_entrada_transacao(self, modo_entrada_transacao):
        """
        Sets the modo_entrada_transacao of this TransacaoNaoProcessadaResponse.
        Descreve o modo utilizado para realizar a leitura dos dados do cart\u00E3o para realizar a Transa\u00E7\u00E3o.

        :param modo_entrada_transacao: The modo_entrada_transacao of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._modo_entrada_transacao = modo_entrada_transacao

    @property
    def valor_taxa_embarque(self):
        """
        Gets the valor_taxa_embarque of this TransacaoNaoProcessadaResponse.
        Valor da Taxa de Embarque em Real (BRL) quando a transa\u00E7\u00E3o for relacionada a Compra de Passagens A\u00E9reas.

        :return: The valor_taxa_embarque of this TransacaoNaoProcessadaResponse.
        :rtype: float
        """
        return self._valor_taxa_embarque

    @valor_taxa_embarque.setter
    def valor_taxa_embarque(self, valor_taxa_embarque):
        """
        Sets the valor_taxa_embarque of this TransacaoNaoProcessadaResponse.
        Valor da Taxa de Embarque em Real (BRL) quando a transa\u00E7\u00E3o for relacionada a Compra de Passagens A\u00E9reas.

        :param valor_taxa_embarque: The valor_taxa_embarque of this TransacaoNaoProcessadaResponse.
        :type: float
        """
        self._valor_taxa_embarque = valor_taxa_embarque

    @property
    def valor_entrada(self):
        """
        Gets the valor_entrada of this TransacaoNaoProcessadaResponse.
        Valor da Entrada em Real (BRL) quando a transa\u00E7\u00E3o for do tipo Parcelada com o pagamento de um valor de Entrada.

        :return: The valor_entrada of this TransacaoNaoProcessadaResponse.
        :rtype: float
        """
        return self._valor_entrada

    @valor_entrada.setter
    def valor_entrada(self, valor_entrada):
        """
        Sets the valor_entrada of this TransacaoNaoProcessadaResponse.
        Valor da Entrada em Real (BRL) quando a transa\u00E7\u00E3o for do tipo Parcelada com o pagamento de um valor de Entrada.

        :param valor_entrada: The valor_entrada of this TransacaoNaoProcessadaResponse.
        :type: float
        """
        self._valor_entrada = valor_entrada

    @property
    def valor_brl(self):
        """
        Gets the valor_brl of this TransacaoNaoProcessadaResponse.
        Valor da Transa\u00E7\u00E3o em Real (BRL).

        :return: The valor_brl of this TransacaoNaoProcessadaResponse.
        :rtype: float
        """
        return self._valor_brl

    @valor_brl.setter
    def valor_brl(self, valor_brl):
        """
        Sets the valor_brl of this TransacaoNaoProcessadaResponse.
        Valor da Transa\u00E7\u00E3o em Real (BRL).

        :param valor_brl: The valor_brl of this TransacaoNaoProcessadaResponse.
        :type: float
        """
        self._valor_brl = valor_brl

    @property
    def valor_usd(self):
        """
        Gets the valor_usd of this TransacaoNaoProcessadaResponse.
        Valor da Transa\u00E7\u00E3o em D\u00F3lar Americano (USD).

        :return: The valor_usd of this TransacaoNaoProcessadaResponse.
        :rtype: float
        """
        return self._valor_usd

    @valor_usd.setter
    def valor_usd(self, valor_usd):
        """
        Sets the valor_usd of this TransacaoNaoProcessadaResponse.
        Valor da Transa\u00E7\u00E3o em D\u00F3lar Americano (USD).

        :param valor_usd: The valor_usd of this TransacaoNaoProcessadaResponse.
        :type: float
        """
        self._valor_usd = valor_usd

    @property
    def cotacao_usd(self):
        """
        Gets the cotacao_usd of this TransacaoNaoProcessadaResponse.
        Valor do D\u00F3lar Americano (USD) convertido em Real (BRL).

        :return: The cotacao_usd of this TransacaoNaoProcessadaResponse.
        :rtype: float
        """
        return self._cotacao_usd

    @cotacao_usd.setter
    def cotacao_usd(self, cotacao_usd):
        """
        Sets the cotacao_usd of this TransacaoNaoProcessadaResponse.
        Valor do D\u00F3lar Americano (USD) convertido em Real (BRL).

        :param cotacao_usd: The cotacao_usd of this TransacaoNaoProcessadaResponse.
        :type: float
        """
        self._cotacao_usd = cotacao_usd

    @property
    def data_cotacao_usd(self):
        """
        Gets the data_cotacao_usd of this TransacaoNaoProcessadaResponse.
        Data de Fechamento da Cota\u00E7\u00E3o do D\u00F3lar Americano (USD).

        :return: The data_cotacao_usd of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._data_cotacao_usd

    @data_cotacao_usd.setter
    def data_cotacao_usd(self, data_cotacao_usd):
        """
        Sets the data_cotacao_usd of this TransacaoNaoProcessadaResponse.
        Data de Fechamento da Cota\u00E7\u00E3o do D\u00F3lar Americano (USD).

        :param data_cotacao_usd: The data_cotacao_usd of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._data_cotacao_usd = data_cotacao_usd

    @property
    def codigo_moeda_origem(self):
        """
        Gets the codigo_moeda_origem of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Moeda utilizada na Transa\u00E7\u00E3o, seguindo padr\u00E3o ISO 4217.

        :return: The codigo_moeda_origem of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._codigo_moeda_origem

    @codigo_moeda_origem.setter
    def codigo_moeda_origem(self, codigo_moeda_origem):
        """
        Sets the codigo_moeda_origem of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Moeda utilizada na Transa\u00E7\u00E3o, seguindo padr\u00E3o ISO 4217.

        :param codigo_moeda_origem: The codigo_moeda_origem of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._codigo_moeda_origem = codigo_moeda_origem

    @property
    def codigo_moeda_destino(self):
        """
        Gets the codigo_moeda_destino of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Moeda da Transa\u00E7\u00E3o ap\u00F3s a convers\u00E3o, seguindo padr\u00E3o ISO 4217.

        :return: The codigo_moeda_destino of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._codigo_moeda_destino

    @codigo_moeda_destino.setter
    def codigo_moeda_destino(self, codigo_moeda_destino):
        """
        Sets the codigo_moeda_destino of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Moeda da Transa\u00E7\u00E3o ap\u00F3s a convers\u00E3o, seguindo padr\u00E3o ISO 4217.

        :param codigo_moeda_destino: The codigo_moeda_destino of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._codigo_moeda_destino = codigo_moeda_destino

    @property
    def codigo_autorizacao(self):
        """
        Gets the codigo_autorizacao of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Autoriza\u00E7\u00E3o da Transa\u00E7\u00E3o.

        :return: The codigo_autorizacao of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._codigo_autorizacao

    @codigo_autorizacao.setter
    def codigo_autorizacao(self, codigo_autorizacao):
        """
        Sets the codigo_autorizacao of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Autoriza\u00E7\u00E3o da Transa\u00E7\u00E3o.

        :param codigo_autorizacao: The codigo_autorizacao of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._codigo_autorizacao = codigo_autorizacao

    @property
    def codigo_referencia(self):
        """
        Gets the codigo_referencia of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Refer\u00EAncia da Transa\u00E7\u00E3o quando utilizado Cart\u00E3o Bandeirado.

        :return: The codigo_referencia of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._codigo_referencia

    @codigo_referencia.setter
    def codigo_referencia(self, codigo_referencia):
        """
        Sets the codigo_referencia of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Refer\u00EAncia da Transa\u00E7\u00E3o quando utilizado Cart\u00E3o Bandeirado.

        :param codigo_referencia: The codigo_referencia of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._codigo_referencia = codigo_referencia

    @property
    def codigo_terminal(self):
        """
        Gets the codigo_terminal of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da origem da captura da Transa\u00E7\u00E3o.

        :return: The codigo_terminal of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._codigo_terminal

    @codigo_terminal.setter
    def codigo_terminal(self, codigo_terminal):
        """
        Sets the codigo_terminal of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da origem da captura da Transa\u00E7\u00E3o.

        :param codigo_terminal: The codigo_terminal of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._codigo_terminal = codigo_terminal

    @property
    def codigo_mcc(self):
        """
        Gets the codigo_mcc of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da categoria do Estabelecimento.

        :return: The codigo_mcc of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._codigo_mcc

    @codigo_mcc.setter
    def codigo_mcc(self, codigo_mcc):
        """
        Sets the codigo_mcc of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o da categoria do Estabelecimento.

        :param codigo_mcc: The codigo_mcc of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._codigo_mcc = codigo_mcc

    @property
    def grupo_mcc(self):
        """
        Gets the grupo_mcc of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do grupo do Estabelecimento.

        :return: The grupo_mcc of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._grupo_mcc

    @grupo_mcc.setter
    def grupo_mcc(self, grupo_mcc):
        """
        Sets the grupo_mcc of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de identifica\u00E7\u00E3o do grupo do Estabelecimento.

        :param grupo_mcc: The grupo_mcc of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._grupo_mcc = grupo_mcc

    @property
    def grupo_descricao_mcc(self):
        """
        Gets the grupo_descricao_mcc of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o do grupo do Estabelecimento.

        :return: The grupo_descricao_mcc of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._grupo_descricao_mcc

    @grupo_descricao_mcc.setter
    def grupo_descricao_mcc(self, grupo_descricao_mcc):
        """
        Sets the grupo_descricao_mcc of this TransacaoNaoProcessadaResponse.
        Descri\u00E7\u00E3o do grupo do Estabelecimento.

        :param grupo_descricao_mcc: The grupo_descricao_mcc of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._grupo_descricao_mcc = grupo_descricao_mcc

    @property
    def id_estabelecimento(self):
        """
        Gets the id_estabelecimento of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Estabelecimento (id).

        :return: The id_estabelecimento of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._id_estabelecimento

    @id_estabelecimento.setter
    def id_estabelecimento(self, id_estabelecimento):
        """
        Sets the id_estabelecimento of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o do Estabelecimento (id).

        :param id_estabelecimento: The id_estabelecimento of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._id_estabelecimento = id_estabelecimento

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this TransacaoNaoProcessadaResponse.
        Nome do Estabelecimento.

        :return: The nome_estabelecimento of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this TransacaoNaoProcessadaResponse.
        Nome do Estabelecimento.

        :param nome_estabelecimento: The nome_estabelecimento of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def nome_fantasia_estabelecimento(self):
        """
        Gets the nome_fantasia_estabelecimento of this TransacaoNaoProcessadaResponse.
        Nome Fantasia do Estabelecimento.

        :return: The nome_fantasia_estabelecimento of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._nome_fantasia_estabelecimento

    @nome_fantasia_estabelecimento.setter
    def nome_fantasia_estabelecimento(self, nome_fantasia_estabelecimento):
        """
        Sets the nome_fantasia_estabelecimento of this TransacaoNaoProcessadaResponse.
        Nome Fantasia do Estabelecimento.

        :param nome_fantasia_estabelecimento: The nome_fantasia_estabelecimento of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._nome_fantasia_estabelecimento = nome_fantasia_estabelecimento

    @property
    def localidade_estabelecimento(self):
        """
        Gets the localidade_estabelecimento of this TransacaoNaoProcessadaResponse.
        Localidade do Estabelecimento.

        :return: The localidade_estabelecimento of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._localidade_estabelecimento

    @localidade_estabelecimento.setter
    def localidade_estabelecimento(self, localidade_estabelecimento):
        """
        Sets the localidade_estabelecimento of this TransacaoNaoProcessadaResponse.
        Localidade do Estabelecimento.

        :param localidade_estabelecimento: The localidade_estabelecimento of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._localidade_estabelecimento = localidade_estabelecimento

    @property
    def plano_parcelamento(self):
        """
        Gets the plano_parcelamento of this TransacaoNaoProcessadaResponse.
        Quando a Transa\u00E7\u00E3o for do tipo Parcelada, apresenta o n\u00FAmero total de Parcelas.

        :return: The plano_parcelamento of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._plano_parcelamento

    @plano_parcelamento.setter
    def plano_parcelamento(self, plano_parcelamento):
        """
        Sets the plano_parcelamento of this TransacaoNaoProcessadaResponse.
        Quando a Transa\u00E7\u00E3o for do tipo Parcelada, apresenta o n\u00FAmero total de Parcelas.

        :param plano_parcelamento: The plano_parcelamento of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._plano_parcelamento = plano_parcelamento

    @property
    def numero_parcela(self):
        """
        Gets the numero_parcela of this TransacaoNaoProcessadaResponse.
        Quando a Transa\u00E7\u00E3o for do tipo Parcelada, apresenta o n\u00FAmero da Parcela.

        :return: The numero_parcela of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._numero_parcela

    @numero_parcela.setter
    def numero_parcela(self, numero_parcela):
        """
        Sets the numero_parcela of this TransacaoNaoProcessadaResponse.
        Quando a Transa\u00E7\u00E3o for do tipo Parcelada, apresenta o n\u00FAmero da Parcela.

        :param numero_parcela: The numero_parcela of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._numero_parcela = numero_parcela

    @property
    def detalhes_transacao(self):
        """
        Gets the detalhes_transacao of this TransacaoNaoProcessadaResponse.
        Detalhes complementares a respeito da Transa\u00E7\u00E3o.

        :return: The detalhes_transacao of this TransacaoNaoProcessadaResponse.
        :rtype: str
        """
        return self._detalhes_transacao

    @detalhes_transacao.setter
    def detalhes_transacao(self, detalhes_transacao):
        """
        Sets the detalhes_transacao of this TransacaoNaoProcessadaResponse.
        Detalhes complementares a respeito da Transa\u00E7\u00E3o.

        :param detalhes_transacao: The detalhes_transacao of this TransacaoNaoProcessadaResponse.
        :type: str
        """
        self._detalhes_transacao = detalhes_transacao

    @property
    def flag_credito(self):
        """
        Gets the flag_credito of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o \u00E9 do Tipo 'Cr\u00E9dito'.

        :return: The flag_credito of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._flag_credito

    @flag_credito.setter
    def flag_credito(self, flag_credito):
        """
        Sets the flag_credito of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o \u00E9 do Tipo 'Cr\u00E9dito'.

        :param flag_credito: The flag_credito of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._flag_credito = flag_credito

    @property
    def flag_faturado(self):
        """
        Gets the flag_faturado of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o foi consolidada em uma Fatura.

        :return: The flag_faturado of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._flag_faturado

    @flag_faturado.setter
    def flag_faturado(self, flag_faturado):
        """
        Sets the flag_faturado of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o foi consolidada em uma Fatura.

        :param flag_faturado: The flag_faturado of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._flag_faturado = flag_faturado

    @property
    def flag_estorno(self):
        """
        Gets the flag_estorno of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o foi estornada.

        :return: The flag_estorno of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._flag_estorno

    @flag_estorno.setter
    def flag_estorno(self, flag_estorno):
        """
        Sets the flag_estorno of this TransacaoNaoProcessadaResponse.
        Quando ativa, indica que a Transa\u00E7\u00E3o foi estornada.

        :param flag_estorno: The flag_estorno of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._flag_estorno = flag_estorno

    @property
    def id_transacao_estorno(self):
        """
        Gets the id_transacao_estorno of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Transa\u00E7\u00E3o (id) que gerou o estorno.

        :return: The id_transacao_estorno of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._id_transacao_estorno

    @id_transacao_estorno.setter
    def id_transacao_estorno(self, id_transacao_estorno):
        """
        Sets the id_transacao_estorno of this TransacaoNaoProcessadaResponse.
        C\u00F3digo de Identifica\u00E7\u00E3o da Transa\u00E7\u00E3o (id) que gerou o estorno.

        :param id_transacao_estorno: The id_transacao_estorno of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._id_transacao_estorno = id_transacao_estorno

    @property
    def status(self):
        """
        Gets the status of this TransacaoNaoProcessadaResponse.
        Atributo que representa o c\u00F3digo identificador do status da transa\u00E7\u00E3o.

        :return: The status of this TransacaoNaoProcessadaResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TransacaoNaoProcessadaResponse.
        Atributo que representa o c\u00F3digo identificador do status da transa\u00E7\u00E3o.

        :param status: The status of this TransacaoNaoProcessadaResponse.
        :type: int
        """
        self._status = status

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

