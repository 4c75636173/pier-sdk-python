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


class PessoaJuridicaAprovadaResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PessoaJuridicaAprovadaResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'razao_social': 'str',
            'nome_fantasia': 'str',
            'cnpj': 'str',
            'inscricao_estadual': 'str',
            'data_abertura_empresa': 'str',
            'id_origem_comercial': 'int',
            'id_produto': 'int',
            'numero_agencia': 'int',
            'numero_conta_corrente': 'str',
            'email': 'str',
            'dia_vencimento': 'int',
            'nome_impresso': 'str',
            'id_conta': 'int',
            'id_proposta': 'int',
            'canal_entrada': 'str',
            'telefones': 'list[TelefonePessoaAprovadaResponse]',
            'enderecos': 'list[EnderecoAprovadoResponse]',
            'socios': 'list[SocioAprovadoResponse]'
        }

        self.attribute_map = {
            'id': 'id',
            'razao_social': 'razaoSocial',
            'nome_fantasia': 'nomeFantasia',
            'cnpj': 'cnpj',
            'inscricao_estadual': 'inscricaoEstadual',
            'data_abertura_empresa': 'dataAberturaEmpresa',
            'id_origem_comercial': 'idOrigemComercial',
            'id_produto': 'idProduto',
            'numero_agencia': 'numeroAgencia',
            'numero_conta_corrente': 'numeroContaCorrente',
            'email': 'email',
            'dia_vencimento': 'diaVencimento',
            'nome_impresso': 'nomeImpresso',
            'id_conta': 'idConta',
            'id_proposta': 'idProposta',
            'canal_entrada': 'canalEntrada',
            'telefones': 'telefones',
            'enderecos': 'enderecos',
            'socios': 'socios'
        }

        self._id = None
        self._razao_social = None
        self._nome_fantasia = None
        self._cnpj = None
        self._inscricao_estadual = None
        self._data_abertura_empresa = None
        self._id_origem_comercial = None
        self._id_produto = None
        self._numero_agencia = None
        self._numero_conta_corrente = None
        self._email = None
        self._dia_vencimento = None
        self._nome_impresso = None
        self._id_conta = None
        self._id_proposta = None
        self._canal_entrada = None
        self._telefones = None
        self._enderecos = None
        self._socios = None

    @property
    def id(self):
        """
        Gets the id of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da pessoa jur\u00C3\u00ADdica (id)

        :return: The id of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da pessoa jur\u00C3\u00ADdica (id)

        :param id: The id of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._id = id

    @property
    def razao_social(self):
        """
        Gets the razao_social of this PessoaJuridicaAprovadaResponse.
        Apresenta o nome completo da raz\u00C3\u00A3o social (nome empresarial)'.

        :return: The razao_social of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        """
        Sets the razao_social of this PessoaJuridicaAprovadaResponse.
        Apresenta o nome completo da raz\u00C3\u00A3o social (nome empresarial)'.

        :param razao_social: The razao_social of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._razao_social = razao_social

    @property
    def nome_fantasia(self):
        """
        Gets the nome_fantasia of this PessoaJuridicaAprovadaResponse.
        Apresenta o nome fantasia da empresa.

        :return: The nome_fantasia of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        """
        Sets the nome_fantasia of this PessoaJuridicaAprovadaResponse.
        Apresenta o nome fantasia da empresa.

        :param nome_fantasia: The nome_fantasia of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._nome_fantasia = nome_fantasia

    @property
    def cnpj(self):
        """
        Gets the cnpj of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero do Cadastro Nacional de Pessoa Juridica (CNPJ)

        :return: The cnpj of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        """
        Sets the cnpj of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero do Cadastro Nacional de Pessoa Juridica (CNPJ)

        :param cnpj: The cnpj of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._cnpj = cnpj

    @property
    def inscricao_estadual(self):
        """
        Gets the inscricao_estadual of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da Inscri\u00C3\u00A7\u00C3\u00A3o Estadual (IE).

        :return: The inscricao_estadual of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._inscricao_estadual

    @inscricao_estadual.setter
    def inscricao_estadual(self, inscricao_estadual):
        """
        Sets the inscricao_estadual of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da Inscri\u00C3\u00A7\u00C3\u00A3o Estadual (IE).

        :param inscricao_estadual: The inscricao_estadual of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._inscricao_estadual = inscricao_estadual

    @property
    def data_abertura_empresa(self):
        """
        Gets the data_abertura_empresa of this PessoaJuridicaAprovadaResponse.
        Data de abertura da empresa, essa data deve ser informada no formato: aaaa-MM-dd.

        :return: The data_abertura_empresa of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._data_abertura_empresa

    @data_abertura_empresa.setter
    def data_abertura_empresa(self, data_abertura_empresa):
        """
        Sets the data_abertura_empresa of this PessoaJuridicaAprovadaResponse.
        Data de abertura da empresa, essa data deve ser informada no formato: aaaa-MM-dd.

        :param data_abertura_empresa: The data_abertura_empresa of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._data_abertura_empresa = data_abertura_empresa

    @property
    def id_origem_comercial(self):
        """
        Gets the id_origem_comercial of this PessoaJuridicaAprovadaResponse.
        Id da origem comercial

        :return: The id_origem_comercial of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._id_origem_comercial

    @id_origem_comercial.setter
    def id_origem_comercial(self, id_origem_comercial):
        """
        Sets the id_origem_comercial of this PessoaJuridicaAprovadaResponse.
        Id da origem comercial

        :param id_origem_comercial: The id_origem_comercial of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._id_origem_comercial = id_origem_comercial

    @property
    def id_produto(self):
        """
        Gets the id_produto of this PessoaJuridicaAprovadaResponse.
        Id do produto

        :return: The id_produto of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        """
        Sets the id_produto of this PessoaJuridicaAprovadaResponse.
        Id do produto

        :param id_produto: The id_produto of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._id_produto = id_produto

    @property
    def numero_agencia(self):
        """
        Gets the numero_agencia of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :return: The numero_agencia of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._numero_agencia

    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        """
        Sets the numero_agencia of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da ag\u00C3\u00AAncia.

        :param numero_agencia: The numero_agencia of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._numero_agencia = numero_agencia

    @property
    def numero_conta_corrente(self):
        """
        Gets the numero_conta_corrente of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da conta corrente.

        :return: The numero_conta_corrente of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._numero_conta_corrente

    @numero_conta_corrente.setter
    def numero_conta_corrente(self, numero_conta_corrente):
        """
        Sets the numero_conta_corrente of this PessoaJuridicaAprovadaResponse.
        N\u00C3\u00BAmero da conta corrente.

        :param numero_conta_corrente: The numero_conta_corrente of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._numero_conta_corrente = numero_conta_corrente

    @property
    def email(self):
        """
        Gets the email of this PessoaJuridicaAprovadaResponse.
        Email da empresa

        :return: The email of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PessoaJuridicaAprovadaResponse.
        Email da empresa

        :param email: The email of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._email = email

    @property
    def dia_vencimento(self):
        """
        Gets the dia_vencimento of this PessoaJuridicaAprovadaResponse.
        Dia vencimento

        :return: The dia_vencimento of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._dia_vencimento

    @dia_vencimento.setter
    def dia_vencimento(self, dia_vencimento):
        """
        Sets the dia_vencimento of this PessoaJuridicaAprovadaResponse.
        Dia vencimento

        :param dia_vencimento: The dia_vencimento of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._dia_vencimento = dia_vencimento

    @property
    def nome_impresso(self):
        """
        Gets the nome_impresso of this PessoaJuridicaAprovadaResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :return: The nome_impresso of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._nome_impresso

    @nome_impresso.setter
    def nome_impresso(self, nome_impresso):
        """
        Sets the nome_impresso of this PessoaJuridicaAprovadaResponse.
        Nome que deve ser impresso no cart\u00C3\u00A3o

        :param nome_impresso: The nome_impresso of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._nome_impresso = nome_impresso

    @property
    def id_conta(self):
        """
        Gets the id_conta of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta cadastrada

        :return: The id_conta of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta):
        """
        Sets the id_conta of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta cadastrada

        :param id_conta: The id_conta of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._id_conta = id_conta

    @property
    def id_proposta(self):
        """
        Gets the id_proposta of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da proposta

        :return: The id_proposta of this PessoaJuridicaAprovadaResponse.
        :rtype: int
        """
        return self._id_proposta

    @id_proposta.setter
    def id_proposta(self, id_proposta):
        """
        Sets the id_proposta of this PessoaJuridicaAprovadaResponse.
        C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da proposta

        :param id_proposta: The id_proposta of this PessoaJuridicaAprovadaResponse.
        :type: int
        """
        self._id_proposta = id_proposta

    @property
    def canal_entrada(self):
        """
        Gets the canal_entrada of this PessoaJuridicaAprovadaResponse.
        Indica o canal pelo qual o cadastro do cliente foi realizado

        :return: The canal_entrada of this PessoaJuridicaAprovadaResponse.
        :rtype: str
        """
        return self._canal_entrada

    @canal_entrada.setter
    def canal_entrada(self, canal_entrada):
        """
        Sets the canal_entrada of this PessoaJuridicaAprovadaResponse.
        Indica o canal pelo qual o cadastro do cliente foi realizado

        :param canal_entrada: The canal_entrada of this PessoaJuridicaAprovadaResponse.
        :type: str
        """
        self._canal_entrada = canal_entrada

    @property
    def telefones(self):
        """
        Gets the telefones of this PessoaJuridicaAprovadaResponse.
        Apresenta os telefones da empresa

        :return: The telefones of this PessoaJuridicaAprovadaResponse.
        :rtype: list[TelefonePessoaAprovadaResponse]
        """
        return self._telefones

    @telefones.setter
    def telefones(self, telefones):
        """
        Sets the telefones of this PessoaJuridicaAprovadaResponse.
        Apresenta os telefones da empresa

        :param telefones: The telefones of this PessoaJuridicaAprovadaResponse.
        :type: list[TelefonePessoaAprovadaResponse]
        """
        self._telefones = telefones

    @property
    def enderecos(self):
        """
        Gets the enderecos of this PessoaJuridicaAprovadaResponse.
        Pode ser informado os seguintes tipos de endere\u00C3\u00A7o: Residencial, Comercial, e Outros

        :return: The enderecos of this PessoaJuridicaAprovadaResponse.
        :rtype: list[EnderecoAprovadoResponse]
        """
        return self._enderecos

    @enderecos.setter
    def enderecos(self, enderecos):
        """
        Sets the enderecos of this PessoaJuridicaAprovadaResponse.
        Pode ser informado os seguintes tipos de endere\u00C3\u00A7o: Residencial, Comercial, e Outros

        :param enderecos: The enderecos of this PessoaJuridicaAprovadaResponse.
        :type: list[EnderecoAprovadoResponse]
        """
        self._enderecos = enderecos

    @property
    def socios(self):
        """
        Gets the socios of this PessoaJuridicaAprovadaResponse.
        Apresenta os dados dos s\u00C3\u00B3cios da empresa, caso exista

        :return: The socios of this PessoaJuridicaAprovadaResponse.
        :rtype: list[SocioAprovadoResponse]
        """
        return self._socios

    @socios.setter
    def socios(self, socios):
        """
        Sets the socios of this PessoaJuridicaAprovadaResponse.
        Apresenta os dados dos s\u00C3\u00B3cios da empresa, caso exista

        :param socios: The socios of this PessoaJuridicaAprovadaResponse.
        :type: list[SocioAprovadoResponse]
        """
        self._socios = socios

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

