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


class AntecipacaoSimuladaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoSimuladaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mcc': 'int',
            'uf': 'str',
            'id_antecipacao_simulada': 'int',
            'id_conta': 'int',
            'id_compra': 'int',
            'id_tipo_transacao': 'int',
            'quantidade_parcelas_antecipaveis': 'int',
            'valor_parcela': 'float',
            'data_hora_simulacao': 'str',
            'taxa_antecipacao_ano': 'float',
            'nome_estabelecimento': 'str',
            'status': 'str',
            'data_compra': 'str',
            'tipo_origem_transacao': 'str',
            'cidade': 'str',
            'pais': 'str',
            'latitude': 'str',
            'longitude': 'str',
            'id_grupo_mcc': 'int',
            'descricao_grupo_mcc': 'str',
            'id_produto': 'int',
            'descricao_produto': 'str',
            'descricao_estabelecimento': 'str',
            'nome_fantasia_estabelecimento': 'str',
            'detalhes': 'list[AntecipacaoSimuladaDetalhesResponse]'
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'uf': 'uf',
            'id_antecipacao_simulada': 'idAntecipacaoSimulada',
            'id_conta': 'idConta',
            'id_compra': 'idCompra',
            'id_tipo_transacao': 'idTipoTransacao',
            'quantidade_parcelas_antecipaveis': 'quantidadeParcelasAntecipaveis',
            'valor_parcela': 'valorParcela',
            'data_hora_simulacao': 'dataHoraSimulacao',
            'taxa_antecipacao_ano': 'taxaAntecipacaoAno',
            'nome_estabelecimento': 'nomeEstabelecimento',
            'status': 'status',
            'data_compra': 'dataCompra',
            'tipo_origem_transacao': 'tipoOrigemTransacao',
            'cidade': 'cidade',
            'pais': 'pais',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'id_grupo_mcc': 'idGrupoMCC',
            'descricao_grupo_mcc': 'descricaoGrupoMCC',
            'id_produto': 'idProduto',
            'descricao_produto': 'descricaoProduto',
            'descricao_estabelecimento': 'descricaoEstabelecimento',
            'nome_fantasia_estabelecimento': 'nomeFantasiaEstabelecimento',
            'detalhes': 'detalhes'
        }

        self._mcc = None
        self._uf = None
        self._id_antecipacao_simulada = None
        self._id_conta = None
        self._id_compra = None
        self._id_tipo_transacao = None
        self._quantidade_parcelas_antecipaveis = None
        self._valor_parcela = None
        self._data_hora_simulacao = None
        self._taxa_antecipacao_ano = None
        self._nome_estabelecimento = None
        self._status = None
        self._data_compra = None
        self._tipo_origem_transacao = None
        self._cidade = None
        self._pais = None
        self._latitude = None
        self._longitude = None
        self._id_grupo_mcc = None
        self._descricao_grupo_mcc = None
        self._id_produto = None
        self._descricao_produto = None
        self._descricao_estabelecimento = None
        self._nome_fantasia_estabelecimento = None
        self._detalhes = None

    @property
    def mcc(self):
        """
        Gets the mcc of this AntecipacaoSimuladaResponse.


        :return: The mcc of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """
        Sets the mcc of this AntecipacaoSimuladaResponse.


        :param mcc: The mcc of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._mcc = mcc

    @property
    def uf(self):
        """
        Gets the uf of this AntecipacaoSimuladaResponse.


        :return: The uf of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """
        Sets the uf of this AntecipacaoSimuladaResponse.


        :param uf: The uf of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._uf = uf

    @property
    def id_antecipacao_simulada(self):
        """
        Gets the id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_antecipacao_simulada_value}}}

        :return: The id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_antecipacao_simulada

    @id_antecipacao_simulada.setter
    def id_antecipacao_simulada(self, id_antecipacao_simulada):
        """
        Sets the id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_antecipacao_simulada_value}}}

        :param id_antecipacao_simulada: The id_antecipacao_simulada of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_antecipacao_simulada = id_antecipacao_simulada

    @property
    def id_conta(self):
        """
        Gets the id_conta of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_conta_value}}}

        :return: The id_conta of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_conta_value}}}

        :param id_conta: The id_conta of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_compra(self):
        """
        Gets the id_compra of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_compra_value}}}

        :return: The id_compra of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_compra

    @id_compra.setter
    def id_compra(self, id_compra):
        """
        Sets the id_compra of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_compra_value}}}

        :param id_compra: The id_compra of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_compra = id_compra

    @property
    def id_tipo_transacao(self):
        """
        Gets the id_tipo_transacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_tipo_transacao_value}}}

        :return: The id_tipo_transacao of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_tipo_transacao

    @id_tipo_transacao.setter
    def id_tipo_transacao(self, id_tipo_transacao):
        """
        Sets the id_tipo_transacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_tipo_transacao_value}}}

        :param id_tipo_transacao: The id_tipo_transacao of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_tipo_transacao = id_tipo_transacao

    @property
    def quantidade_parcelas_antecipaveis(self):
        """
        Gets the quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_quantidade_parcelas_antecipaveis_value}}}

        :return: The quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_antecipaveis

    @quantidade_parcelas_antecipaveis.setter
    def quantidade_parcelas_antecipaveis(self, quantidade_parcelas_antecipaveis):
        """
        Sets the quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_quantidade_parcelas_antecipaveis_value}}}

        :param quantidade_parcelas_antecipaveis: The quantidade_parcelas_antecipaveis of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._quantidade_parcelas_antecipaveis = quantidade_parcelas_antecipaveis

    @property
    def valor_parcela(self):
        """
        Gets the valor_parcela of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_valor_parcela_value}}}

        :return: The valor_parcela of this AntecipacaoSimuladaResponse.
        :rtype: float
        """
        return self._valor_parcela

    @valor_parcela.setter
    def valor_parcela(self, valor_parcela):
        """
        Sets the valor_parcela of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_valor_parcela_value}}}

        :param valor_parcela: The valor_parcela of this AntecipacaoSimuladaResponse.
        :type: float
        """
        self._valor_parcela = valor_parcela

    @property
    def data_hora_simulacao(self):
        """
        Gets the data_hora_simulacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_data_hora_simulacao_value}}}

        :return: The data_hora_simulacao of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._data_hora_simulacao

    @data_hora_simulacao.setter
    def data_hora_simulacao(self, data_hora_simulacao):
        """
        Sets the data_hora_simulacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_data_hora_simulacao_value}}}

        :param data_hora_simulacao: The data_hora_simulacao of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._data_hora_simulacao = data_hora_simulacao

    @property
    def taxa_antecipacao_ano(self):
        """
        Gets the taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_taxa_antecipacao_ano_value}}}

        :return: The taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        :rtype: float
        """
        return self._taxa_antecipacao_ano

    @taxa_antecipacao_ano.setter
    def taxa_antecipacao_ano(self, taxa_antecipacao_ano):
        """
        Sets the taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_taxa_antecipacao_ano_value}}}

        :param taxa_antecipacao_ano: The taxa_antecipacao_ano of this AntecipacaoSimuladaResponse.
        :type: float
        """
        self._taxa_antecipacao_ano = taxa_antecipacao_ano

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_nome_estabelecimento_value}}}

        :return: The nome_estabelecimento of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_nome_estabelecimento_value}}}

        :param nome_estabelecimento: The nome_estabelecimento of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def status(self):
        """
        Gets the status of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_status_value}}}

        :return: The status of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_status_value}}}

        :param status: The status of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._status = status

    @property
    def data_compra(self):
        """
        Gets the data_compra of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_data_compra_value}}}

        :return: The data_compra of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._data_compra

    @data_compra.setter
    def data_compra(self, data_compra):
        """
        Sets the data_compra of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_data_compra_value}}}

        :param data_compra: The data_compra of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._data_compra = data_compra

    @property
    def tipo_origem_transacao(self):
        """
        Gets the tipo_origem_transacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_tipo_origem_transacao_value}}}

        :return: The tipo_origem_transacao of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._tipo_origem_transacao

    @tipo_origem_transacao.setter
    def tipo_origem_transacao(self, tipo_origem_transacao):
        """
        Sets the tipo_origem_transacao of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_tipo_origem_transacao_value}}}

        :param tipo_origem_transacao: The tipo_origem_transacao of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._tipo_origem_transacao = tipo_origem_transacao

    @property
    def cidade(self):
        """
        Gets the cidade of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_cidade_value}}}

        :return: The cidade of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """
        Sets the cidade of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_cidade_value}}}

        :param cidade: The cidade of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._cidade = cidade

    @property
    def pais(self):
        """
        Gets the pais of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_pais_value}}}

        :return: The pais of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais):
        """
        Sets the pais of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_pais_value}}}

        :param pais: The pais of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._pais = pais

    @property
    def latitude(self):
        """
        Gets the latitude of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_latitude_value}}}

        :return: The latitude of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_latitude_value}}}

        :param latitude: The latitude of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_longitude_value}}}

        :return: The longitude of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_longitude_value}}}

        :param longitude: The longitude of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._longitude = longitude

    @property
    def id_grupo_mcc(self):
        """
        Gets the id_grupo_mcc of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_grupo_m_c_c_value}}}

        :return: The id_grupo_mcc of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_grupo_mcc

    @id_grupo_mcc.setter
    def id_grupo_mcc(self, id_grupo_mcc):
        """
        Sets the id_grupo_mcc of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_grupo_m_c_c_value}}}

        :param id_grupo_mcc: The id_grupo_mcc of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_grupo_mcc = id_grupo_mcc

    @property
    def descricao_grupo_mcc(self):
        """
        Gets the descricao_grupo_mcc of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_grupo_m_c_c_value}}}

        :return: The descricao_grupo_mcc of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._descricao_grupo_mcc

    @descricao_grupo_mcc.setter
    def descricao_grupo_mcc(self, descricao_grupo_mcc):
        """
        Sets the descricao_grupo_mcc of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_grupo_m_c_c_value}}}

        :param descricao_grupo_mcc: The descricao_grupo_mcc of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._descricao_grupo_mcc = descricao_grupo_mcc

    @property
    def id_produto(self):
        """
        Gets the id_produto of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_produto_value}}}

        :return: The id_produto of this AntecipacaoSimuladaResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_id_produto_value}}}

        :param id_produto: The id_produto of this AntecipacaoSimuladaResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def descricao_produto(self):
        """
        Gets the descricao_produto of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_produto_value}}}

        :return: The descricao_produto of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._descricao_produto

    @descricao_produto.setter
    def descricao_produto(self, descricao_produto):
        """
        Sets the descricao_produto of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_produto_value}}}

        :param descricao_produto: The descricao_produto of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._descricao_produto = descricao_produto

    @property
    def descricao_estabelecimento(self):
        """
        Gets the descricao_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_estabelecimento_value}}}

        :return: The descricao_estabelecimento of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._descricao_estabelecimento

    @descricao_estabelecimento.setter
    def descricao_estabelecimento(self, descricao_estabelecimento):
        """
        Sets the descricao_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_descricao_estabelecimento_value}}}

        :param descricao_estabelecimento: The descricao_estabelecimento of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._descricao_estabelecimento = descricao_estabelecimento

    @property
    def nome_fantasia_estabelecimento(self):
        """
        Gets the nome_fantasia_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_nome_fantasia_estabelecimento_value}}}

        :return: The nome_fantasia_estabelecimento of this AntecipacaoSimuladaResponse.
        :rtype: str
        """
        return self._nome_fantasia_estabelecimento

    @nome_fantasia_estabelecimento.setter
    def nome_fantasia_estabelecimento(self, nome_fantasia_estabelecimento):
        """
        Sets the nome_fantasia_estabelecimento of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_nome_fantasia_estabelecimento_value}}}

        :param nome_fantasia_estabelecimento: The nome_fantasia_estabelecimento of this AntecipacaoSimuladaResponse.
        :type: str
        """
        self._nome_fantasia_estabelecimento = nome_fantasia_estabelecimento

    @property
    def detalhes(self):
        """
        Gets the detalhes of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_detalhes_value}}}

        :return: The detalhes of this AntecipacaoSimuladaResponse.
        :rtype: list[AntecipacaoSimuladaDetalhesResponse]
        """
        return self._detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        """
        Sets the detalhes of this AntecipacaoSimuladaResponse.
        {{{antecipacao_simulada_response_detalhes_value}}}

        :param detalhes: The detalhes of this AntecipacaoSimuladaResponse.
        :type: list[AntecipacaoSimuladaDetalhesResponse]
        """
        self._detalhes = detalhes

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

