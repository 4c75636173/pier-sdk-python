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


class AntecipacaoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mcc': 'int',
            'uf': 'str',
            'id': 'int',
            'id_conta': 'int',
            'id_compra': 'int',
            'quantidade_parcelas_total': 'int',
            'quantidade_parcelas_antecipadas': 'int',
            'valor_parcela': 'float',
            'valor_desconto_total': 'float',
            'valor_total_com_desconto': 'float',
            'taxa_desconto': 'float',
            'data_compra': 'str',
            'status': 'str',
            'nome_estabelecimento': 'str',
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
            'nome_fantasia_estabelecimento': 'str'
        }

        self.attribute_map = {
            'mcc': 'mcc',
            'uf': 'uf',
            'id': 'id',
            'id_conta': 'idConta',
            'id_compra': 'idCompra',
            'quantidade_parcelas_total': 'quantidadeParcelasTotal',
            'quantidade_parcelas_antecipadas': 'quantidadeParcelasAntecipadas',
            'valor_parcela': 'valorParcela',
            'valor_desconto_total': 'valorDescontoTotal',
            'valor_total_com_desconto': 'valorTotalComDesconto',
            'taxa_desconto': 'taxaDesconto',
            'data_compra': 'dataCompra',
            'status': 'status',
            'nome_estabelecimento': 'nomeEstabelecimento',
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
            'nome_fantasia_estabelecimento': 'nomeFantasiaEstabelecimento'
        }

        self._mcc = None
        self._uf = None
        self._id = None
        self._id_conta = None
        self._id_compra = None
        self._quantidade_parcelas_total = None
        self._quantidade_parcelas_antecipadas = None
        self._valor_parcela = None
        self._valor_desconto_total = None
        self._valor_total_com_desconto = None
        self._taxa_desconto = None
        self._data_compra = None
        self._status = None
        self._nome_estabelecimento = None
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

    @property
    def mcc(self):
        """
        Gets the mcc of this AntecipacaoResponse.


        :return: The mcc of this AntecipacaoResponse.
        :rtype: int
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """
        Sets the mcc of this AntecipacaoResponse.


        :param mcc: The mcc of this AntecipacaoResponse.
        :type: int
        """
        self._mcc = mcc

    @property
    def uf(self):
        """
        Gets the uf of this AntecipacaoResponse.


        :return: The uf of this AntecipacaoResponse.
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """
        Sets the uf of this AntecipacaoResponse.


        :param uf: The uf of this AntecipacaoResponse.
        :type: str
        """
        self._uf = uf

    @property
    def id(self):
        """
        Gets the id of this AntecipacaoResponse.
        {{{antecipacao_response_id_value}}}

        :return: The id of this AntecipacaoResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AntecipacaoResponse.
        {{{antecipacao_response_id_value}}}

        :param id: The id of this AntecipacaoResponse.
        :type: int
        """
        self._id = id

    @property
    def id_conta(self):
        """
        Gets the id_conta of this AntecipacaoResponse.
        {{{antecipacao_response_id_conta_value}}}

        :return: The id_conta of this AntecipacaoResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this AntecipacaoResponse.
        {{{antecipacao_response_id_conta_value}}}

        :param id_conta: The id_conta of this AntecipacaoResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_compra(self):
        """
        Gets the id_compra of this AntecipacaoResponse.
        {{{antecipacao_response_id_compra_value}}}

        :return: The id_compra of this AntecipacaoResponse.
        :rtype: int
        """
        return self._id_compra

    @id_compra.setter
    def id_compra(self, id_compra):
        """
        Sets the id_compra of this AntecipacaoResponse.
        {{{antecipacao_response_id_compra_value}}}

        :param id_compra: The id_compra of this AntecipacaoResponse.
        :type: int
        """
        self._id_compra = id_compra

    @property
    def quantidade_parcelas_total(self):
        """
        Gets the quantidade_parcelas_total of this AntecipacaoResponse.
        {{{antecipacao_response_quantidade_parcelas_total_value}}}

        :return: The quantidade_parcelas_total of this AntecipacaoResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_total

    @quantidade_parcelas_total.setter
    def quantidade_parcelas_total(self, quantidade_parcelas_total):
        """
        Sets the quantidade_parcelas_total of this AntecipacaoResponse.
        {{{antecipacao_response_quantidade_parcelas_total_value}}}

        :param quantidade_parcelas_total: The quantidade_parcelas_total of this AntecipacaoResponse.
        :type: int
        """
        self._quantidade_parcelas_total = quantidade_parcelas_total

    @property
    def quantidade_parcelas_antecipadas(self):
        """
        Gets the quantidade_parcelas_antecipadas of this AntecipacaoResponse.
        {{{antecipacao_response_quantidade_parcelas_antecipadas_value}}}

        :return: The quantidade_parcelas_antecipadas of this AntecipacaoResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_antecipadas

    @quantidade_parcelas_antecipadas.setter
    def quantidade_parcelas_antecipadas(self, quantidade_parcelas_antecipadas):
        """
        Sets the quantidade_parcelas_antecipadas of this AntecipacaoResponse.
        {{{antecipacao_response_quantidade_parcelas_antecipadas_value}}}

        :param quantidade_parcelas_antecipadas: The quantidade_parcelas_antecipadas of this AntecipacaoResponse.
        :type: int
        """
        self._quantidade_parcelas_antecipadas = quantidade_parcelas_antecipadas

    @property
    def valor_parcela(self):
        """
        Gets the valor_parcela of this AntecipacaoResponse.
        {{{antecipacao_response_valor_parcela_value}}}

        :return: The valor_parcela of this AntecipacaoResponse.
        :rtype: float
        """
        return self._valor_parcela

    @valor_parcela.setter
    def valor_parcela(self, valor_parcela):
        """
        Sets the valor_parcela of this AntecipacaoResponse.
        {{{antecipacao_response_valor_parcela_value}}}

        :param valor_parcela: The valor_parcela of this AntecipacaoResponse.
        :type: float
        """
        self._valor_parcela = valor_parcela

    @property
    def valor_desconto_total(self):
        """
        Gets the valor_desconto_total of this AntecipacaoResponse.
        {{{antecipacao_response_valor_desconto_total_value}}}

        :return: The valor_desconto_total of this AntecipacaoResponse.
        :rtype: float
        """
        return self._valor_desconto_total

    @valor_desconto_total.setter
    def valor_desconto_total(self, valor_desconto_total):
        """
        Sets the valor_desconto_total of this AntecipacaoResponse.
        {{{antecipacao_response_valor_desconto_total_value}}}

        :param valor_desconto_total: The valor_desconto_total of this AntecipacaoResponse.
        :type: float
        """
        self._valor_desconto_total = valor_desconto_total

    @property
    def valor_total_com_desconto(self):
        """
        Gets the valor_total_com_desconto of this AntecipacaoResponse.
        {{{antecipacao_response_valor_total_com_desconto_value}}}

        :return: The valor_total_com_desconto of this AntecipacaoResponse.
        :rtype: float
        """
        return self._valor_total_com_desconto

    @valor_total_com_desconto.setter
    def valor_total_com_desconto(self, valor_total_com_desconto):
        """
        Sets the valor_total_com_desconto of this AntecipacaoResponse.
        {{{antecipacao_response_valor_total_com_desconto_value}}}

        :param valor_total_com_desconto: The valor_total_com_desconto of this AntecipacaoResponse.
        :type: float
        """
        self._valor_total_com_desconto = valor_total_com_desconto

    @property
    def taxa_desconto(self):
        """
        Gets the taxa_desconto of this AntecipacaoResponse.
        {{{antecipacao_response_taxa_desconto_value}}}

        :return: The taxa_desconto of this AntecipacaoResponse.
        :rtype: float
        """
        return self._taxa_desconto

    @taxa_desconto.setter
    def taxa_desconto(self, taxa_desconto):
        """
        Sets the taxa_desconto of this AntecipacaoResponse.
        {{{antecipacao_response_taxa_desconto_value}}}

        :param taxa_desconto: The taxa_desconto of this AntecipacaoResponse.
        :type: float
        """
        self._taxa_desconto = taxa_desconto

    @property
    def data_compra(self):
        """
        Gets the data_compra of this AntecipacaoResponse.
        {{{antecipacao_response_data_compra_value}}}

        :return: The data_compra of this AntecipacaoResponse.
        :rtype: str
        """
        return self._data_compra

    @data_compra.setter
    def data_compra(self, data_compra):
        """
        Sets the data_compra of this AntecipacaoResponse.
        {{{antecipacao_response_data_compra_value}}}

        :param data_compra: The data_compra of this AntecipacaoResponse.
        :type: str
        """
        self._data_compra = data_compra

    @property
    def status(self):
        """
        Gets the status of this AntecipacaoResponse.
        {{{antecipacao_response_status_value}}}

        :return: The status of this AntecipacaoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AntecipacaoResponse.
        {{{antecipacao_response_status_value}}}

        :param status: The status of this AntecipacaoResponse.
        :type: str
        """
        self._status = status

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_nome_estabelecimento_value}}}

        :return: The nome_estabelecimento of this AntecipacaoResponse.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_nome_estabelecimento_value}}}

        :param nome_estabelecimento: The nome_estabelecimento of this AntecipacaoResponse.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def tipo_origem_transacao(self):
        """
        Gets the tipo_origem_transacao of this AntecipacaoResponse.
        {{{antecipacao_response_tipo_origem_transacao_value}}}

        :return: The tipo_origem_transacao of this AntecipacaoResponse.
        :rtype: str
        """
        return self._tipo_origem_transacao

    @tipo_origem_transacao.setter
    def tipo_origem_transacao(self, tipo_origem_transacao):
        """
        Sets the tipo_origem_transacao of this AntecipacaoResponse.
        {{{antecipacao_response_tipo_origem_transacao_value}}}

        :param tipo_origem_transacao: The tipo_origem_transacao of this AntecipacaoResponse.
        :type: str
        """
        self._tipo_origem_transacao = tipo_origem_transacao

    @property
    def cidade(self):
        """
        Gets the cidade of this AntecipacaoResponse.
        {{{antecipacao_response_cidade_value}}}

        :return: The cidade of this AntecipacaoResponse.
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """
        Sets the cidade of this AntecipacaoResponse.
        {{{antecipacao_response_cidade_value}}}

        :param cidade: The cidade of this AntecipacaoResponse.
        :type: str
        """
        self._cidade = cidade

    @property
    def pais(self):
        """
        Gets the pais of this AntecipacaoResponse.
        {{{antecipacao_response_pais_value}}}

        :return: The pais of this AntecipacaoResponse.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais):
        """
        Sets the pais of this AntecipacaoResponse.
        {{{antecipacao_response_pais_value}}}

        :param pais: The pais of this AntecipacaoResponse.
        :type: str
        """
        self._pais = pais

    @property
    def latitude(self):
        """
        Gets the latitude of this AntecipacaoResponse.
        {{{antecipacao_response_latitude_value}}}

        :return: The latitude of this AntecipacaoResponse.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this AntecipacaoResponse.
        {{{antecipacao_response_latitude_value}}}

        :param latitude: The latitude of this AntecipacaoResponse.
        :type: str
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this AntecipacaoResponse.
        {{{antecipacao_response_longitude_value}}}

        :return: The longitude of this AntecipacaoResponse.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this AntecipacaoResponse.
        {{{antecipacao_response_longitude_value}}}

        :param longitude: The longitude of this AntecipacaoResponse.
        :type: str
        """
        self._longitude = longitude

    @property
    def id_grupo_mcc(self):
        """
        Gets the id_grupo_mcc of this AntecipacaoResponse.
        {{{antecipacao_response_id_grupo_m_c_c_value}}}

        :return: The id_grupo_mcc of this AntecipacaoResponse.
        :rtype: int
        """
        return self._id_grupo_mcc

    @id_grupo_mcc.setter
    def id_grupo_mcc(self, id_grupo_mcc):
        """
        Sets the id_grupo_mcc of this AntecipacaoResponse.
        {{{antecipacao_response_id_grupo_m_c_c_value}}}

        :param id_grupo_mcc: The id_grupo_mcc of this AntecipacaoResponse.
        :type: int
        """
        self._id_grupo_mcc = id_grupo_mcc

    @property
    def descricao_grupo_mcc(self):
        """
        Gets the descricao_grupo_mcc of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_grupo_m_c_c_value}}}

        :return: The descricao_grupo_mcc of this AntecipacaoResponse.
        :rtype: str
        """
        return self._descricao_grupo_mcc

    @descricao_grupo_mcc.setter
    def descricao_grupo_mcc(self, descricao_grupo_mcc):
        """
        Sets the descricao_grupo_mcc of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_grupo_m_c_c_value}}}

        :param descricao_grupo_mcc: The descricao_grupo_mcc of this AntecipacaoResponse.
        :type: str
        """
        self._descricao_grupo_mcc = descricao_grupo_mcc

    @property
    def id_produto(self):
        """
        Gets the id_produto of this AntecipacaoResponse.
        {{{antecipacao_response_id_produto_value}}}

        :return: The id_produto of this AntecipacaoResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this AntecipacaoResponse.
        {{{antecipacao_response_id_produto_value}}}

        :param id_produto: The id_produto of this AntecipacaoResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def descricao_produto(self):
        """
        Gets the descricao_produto of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_produto_value}}}

        :return: The descricao_produto of this AntecipacaoResponse.
        :rtype: str
        """
        return self._descricao_produto

    @descricao_produto.setter
    def descricao_produto(self, descricao_produto):
        """
        Sets the descricao_produto of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_produto_value}}}

        :param descricao_produto: The descricao_produto of this AntecipacaoResponse.
        :type: str
        """
        self._descricao_produto = descricao_produto

    @property
    def descricao_estabelecimento(self):
        """
        Gets the descricao_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_estabelecimento_value}}}

        :return: The descricao_estabelecimento of this AntecipacaoResponse.
        :rtype: str
        """
        return self._descricao_estabelecimento

    @descricao_estabelecimento.setter
    def descricao_estabelecimento(self, descricao_estabelecimento):
        """
        Sets the descricao_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_descricao_estabelecimento_value}}}

        :param descricao_estabelecimento: The descricao_estabelecimento of this AntecipacaoResponse.
        :type: str
        """
        self._descricao_estabelecimento = descricao_estabelecimento

    @property
    def nome_fantasia_estabelecimento(self):
        """
        Gets the nome_fantasia_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_nome_fantasia_estabelecimento_value}}}

        :return: The nome_fantasia_estabelecimento of this AntecipacaoResponse.
        :rtype: str
        """
        return self._nome_fantasia_estabelecimento

    @nome_fantasia_estabelecimento.setter
    def nome_fantasia_estabelecimento(self, nome_fantasia_estabelecimento):
        """
        Sets the nome_fantasia_estabelecimento of this AntecipacaoResponse.
        {{{antecipacao_response_nome_fantasia_estabelecimento_value}}}

        :param nome_fantasia_estabelecimento: The nome_fantasia_estabelecimento of this AntecipacaoResponse.
        :type: str
        """
        self._nome_fantasia_estabelecimento = nome_fantasia_estabelecimento

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

