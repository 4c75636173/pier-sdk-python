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


class AntecipacaoMockResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntecipacaoMockResponse - a model defined in Swagger

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
            'descricao_produto': 'str'
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
            'descricao_produto': 'descricaoProduto'
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

    @property
    def mcc(self):
        """
        Gets the mcc of this AntecipacaoMockResponse.


        :return: The mcc of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """
        Sets the mcc of this AntecipacaoMockResponse.


        :param mcc: The mcc of this AntecipacaoMockResponse.
        :type: int
        """
        self._mcc = mcc

    @property
    def uf(self):
        """
        Gets the uf of this AntecipacaoMockResponse.


        :return: The uf of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._uf

    @uf.setter
    def uf(self, uf):
        """
        Sets the uf of this AntecipacaoMockResponse.


        :param uf: The uf of this AntecipacaoMockResponse.
        :type: str
        """
        self._uf = uf

    @property
    def id(self):
        """
        Gets the id of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da antecipa\u00C3\u00A7\u00C3\u00A3o

        :return: The id of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da antecipa\u00C3\u00A7\u00C3\u00A3o

        :param id: The id of this AntecipacaoMockResponse.
        :type: int
        """
        self._id = id

    @property
    def id_conta(self):
        """
        Gets the id_conta of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta

        :return: The id_conta of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta

        :param id_conta: The id_conta of this AntecipacaoMockResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_compra(self):
        """
        Gets the id_compra of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da compra

        :return: The id_compra of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._id_compra

    @id_compra.setter
    def id_compra(self, id_compra):
        """
        Sets the id_compra of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da compra

        :param id_compra: The id_compra of this AntecipacaoMockResponse.
        :type: int
        """
        self._id_compra = id_compra

    @property
    def quantidade_parcelas_total(self):
        """
        Gets the quantidade_parcelas_total of this AntecipacaoMockResponse.
        Apresenta o numero total de parcelas da compra

        :return: The quantidade_parcelas_total of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_total

    @quantidade_parcelas_total.setter
    def quantidade_parcelas_total(self, quantidade_parcelas_total):
        """
        Sets the quantidade_parcelas_total of this AntecipacaoMockResponse.
        Apresenta o numero total de parcelas da compra

        :param quantidade_parcelas_total: The quantidade_parcelas_total of this AntecipacaoMockResponse.
        :type: int
        """
        self._quantidade_parcelas_total = quantidade_parcelas_total

    @property
    def quantidade_parcelas_antecipadas(self):
        """
        Gets the quantidade_parcelas_antecipadas of this AntecipacaoMockResponse.
        Apresenta o numero de parcelas antecipadas

        :return: The quantidade_parcelas_antecipadas of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._quantidade_parcelas_antecipadas

    @quantidade_parcelas_antecipadas.setter
    def quantidade_parcelas_antecipadas(self, quantidade_parcelas_antecipadas):
        """
        Sets the quantidade_parcelas_antecipadas of this AntecipacaoMockResponse.
        Apresenta o numero de parcelas antecipadas

        :param quantidade_parcelas_antecipadas: The quantidade_parcelas_antecipadas of this AntecipacaoMockResponse.
        :type: int
        """
        self._quantidade_parcelas_antecipadas = quantidade_parcelas_antecipadas

    @property
    def valor_parcela(self):
        """
        Gets the valor_parcela of this AntecipacaoMockResponse.
        Apresenta o valor de cada parcela antecipadas

        :return: The valor_parcela of this AntecipacaoMockResponse.
        :rtype: float
        """
        return self._valor_parcela

    @valor_parcela.setter
    def valor_parcela(self, valor_parcela):
        """
        Sets the valor_parcela of this AntecipacaoMockResponse.
        Apresenta o valor de cada parcela antecipadas

        :param valor_parcela: The valor_parcela of this AntecipacaoMockResponse.
        :type: float
        """
        self._valor_parcela = valor_parcela

    @property
    def valor_desconto_total(self):
        """
        Gets the valor_desconto_total of this AntecipacaoMockResponse.
        Apresenta o valor total do desconto

        :return: The valor_desconto_total of this AntecipacaoMockResponse.
        :rtype: float
        """
        return self._valor_desconto_total

    @valor_desconto_total.setter
    def valor_desconto_total(self, valor_desconto_total):
        """
        Sets the valor_desconto_total of this AntecipacaoMockResponse.
        Apresenta o valor total do desconto

        :param valor_desconto_total: The valor_desconto_total of this AntecipacaoMockResponse.
        :type: float
        """
        self._valor_desconto_total = valor_desconto_total

    @property
    def valor_total_com_desconto(self):
        """
        Gets the valor_total_com_desconto of this AntecipacaoMockResponse.
        Apresenta o valor total com desconto

        :return: The valor_total_com_desconto of this AntecipacaoMockResponse.
        :rtype: float
        """
        return self._valor_total_com_desconto

    @valor_total_com_desconto.setter
    def valor_total_com_desconto(self, valor_total_com_desconto):
        """
        Sets the valor_total_com_desconto of this AntecipacaoMockResponse.
        Apresenta o valor total com desconto

        :param valor_total_com_desconto: The valor_total_com_desconto of this AntecipacaoMockResponse.
        :type: float
        """
        self._valor_total_com_desconto = valor_total_com_desconto

    @property
    def taxa_desconto(self):
        """
        Gets the taxa_desconto of this AntecipacaoMockResponse.
        Apresenta a taxa de desconto

        :return: The taxa_desconto of this AntecipacaoMockResponse.
        :rtype: float
        """
        return self._taxa_desconto

    @taxa_desconto.setter
    def taxa_desconto(self, taxa_desconto):
        """
        Sets the taxa_desconto of this AntecipacaoMockResponse.
        Apresenta a taxa de desconto

        :param taxa_desconto: The taxa_desconto of this AntecipacaoMockResponse.
        :type: float
        """
        self._taxa_desconto = taxa_desconto

    @property
    def data_compra(self):
        """
        Gets the data_compra of this AntecipacaoMockResponse.
        Data da compra.

        :return: The data_compra of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._data_compra

    @data_compra.setter
    def data_compra(self, data_compra):
        """
        Sets the data_compra of this AntecipacaoMockResponse.
        Data da compra.

        :param data_compra: The data_compra of this AntecipacaoMockResponse.
        :type: str
        """
        self._data_compra = data_compra

    @property
    def status(self):
        """
        Gets the status of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do status da autoriza\u00C3\u00A7\u00C3\u00A3o da compra.

        :return: The status of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do status da autoriza\u00C3\u00A7\u00C3\u00A3o da compra.

        :param status: The status of this AntecipacaoMockResponse.
        :type: str
        """
        self._status = status

    @property
    def nome_estabelecimento(self):
        """
        Gets the nome_estabelecimento of this AntecipacaoMockResponse.
        Nome do estabelecimento da compra.

        :return: The nome_estabelecimento of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._nome_estabelecimento

    @nome_estabelecimento.setter
    def nome_estabelecimento(self, nome_estabelecimento):
        """
        Sets the nome_estabelecimento of this AntecipacaoMockResponse.
        Nome do estabelecimento da compra.

        :param nome_estabelecimento: The nome_estabelecimento of this AntecipacaoMockResponse.
        :type: str
        """
        self._nome_estabelecimento = nome_estabelecimento

    @property
    def tipo_origem_transacao(self):
        """
        Gets the tipo_origem_transacao of this AntecipacaoMockResponse.
        Tipo de transa\u00C3\u00A7\u00C3\u00A3o da compra.

        :return: The tipo_origem_transacao of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._tipo_origem_transacao

    @tipo_origem_transacao.setter
    def tipo_origem_transacao(self, tipo_origem_transacao):
        """
        Sets the tipo_origem_transacao of this AntecipacaoMockResponse.
        Tipo de transa\u00C3\u00A7\u00C3\u00A3o da compra.

        :param tipo_origem_transacao: The tipo_origem_transacao of this AntecipacaoMockResponse.
        :type: str
        """
        self._tipo_origem_transacao = tipo_origem_transacao

    @property
    def cidade(self):
        """
        Gets the cidade of this AntecipacaoMockResponse.
        Cidade onde a compra foi realizada.

        :return: The cidade of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        """
        Sets the cidade of this AntecipacaoMockResponse.
        Cidade onde a compra foi realizada.

        :param cidade: The cidade of this AntecipacaoMockResponse.
        :type: str
        """
        self._cidade = cidade

    @property
    def pais(self):
        """
        Gets the pais of this AntecipacaoMockResponse.
        Pa\u00C3\u00ADs onde a compra foi realizada.

        :return: The pais of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais):
        """
        Sets the pais of this AntecipacaoMockResponse.
        Pa\u00C3\u00ADs onde a compra foi realizada.

        :param pais: The pais of this AntecipacaoMockResponse.
        :type: str
        """
        self._pais = pais

    @property
    def latitude(self):
        """
        Gets the latitude of this AntecipacaoMockResponse.
        Coordenada latitudinal da localiza\u00C3\u00A7\u00C3\u00A3o da compra.

        :return: The latitude of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this AntecipacaoMockResponse.
        Coordenada latitudinal da localiza\u00C3\u00A7\u00C3\u00A3o da compra.

        :param latitude: The latitude of this AntecipacaoMockResponse.
        :type: str
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this AntecipacaoMockResponse.
        Coordenada longitudinal da localiza\u00C3\u00A7\u00C3\u00A3o da compra.

        :return: The longitude of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this AntecipacaoMockResponse.
        Coordenada longitudinal da localiza\u00C3\u00A7\u00C3\u00A3o da compra.

        :param longitude: The longitude of this AntecipacaoMockResponse.
        :type: str
        """
        self._longitude = longitude

    @property
    def id_grupo_mcc(self):
        """
        Gets the id_grupo_mcc of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Grupo MCC da compra.

        :return: The id_grupo_mcc of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._id_grupo_mcc

    @id_grupo_mcc.setter
    def id_grupo_mcc(self, id_grupo_mcc):
        """
        Sets the id_grupo_mcc of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Grupo MCC da compra.

        :param id_grupo_mcc: The id_grupo_mcc of this AntecipacaoMockResponse.
        :type: int
        """
        self._id_grupo_mcc = id_grupo_mcc

    @property
    def descricao_grupo_mcc(self):
        """
        Gets the descricao_grupo_mcc of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do Grupo MCC da compra.

        :return: The descricao_grupo_mcc of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._descricao_grupo_mcc

    @descricao_grupo_mcc.setter
    def descricao_grupo_mcc(self, descricao_grupo_mcc):
        """
        Sets the descricao_grupo_mcc of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do Grupo MCC da compra.

        :param descricao_grupo_mcc: The descricao_grupo_mcc of this AntecipacaoMockResponse.
        :type: str
        """
        self._descricao_grupo_mcc = descricao_grupo_mcc

    @property
    def id_produto(self):
        """
        Gets the id_produto of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do produto da compra.

        :return: The id_produto of this AntecipacaoMockResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this AntecipacaoMockResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do produto da compra.

        :param id_produto: The id_produto of this AntecipacaoMockResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def descricao_produto(self):
        """
        Gets the descricao_produto of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do produto da compra.

        :return: The descricao_produto of this AntecipacaoMockResponse.
        :rtype: str
        """
        return self._descricao_produto

    @descricao_produto.setter
    def descricao_produto(self, descricao_produto):
        """
        Sets the descricao_produto of this AntecipacaoMockResponse.
        Descri\u00C3\u00A7\u00C3\u00A3o do produto da compra.

        :param descricao_produto: The descricao_produto of this AntecipacaoMockResponse.
        :type: str
        """
        self._descricao_produto = descricao_produto

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

