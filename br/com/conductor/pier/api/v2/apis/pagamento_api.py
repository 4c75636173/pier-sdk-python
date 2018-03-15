# coding: utf-8

"""
PagamentoApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PagamentoApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def consultar_using_get(self, id, **kwargs):
        """
        Consulta os dados de um determinado acordo
        Este m\u00E9todo permite consultar dados de um determinado acordo a partir de seu codigo de identifica\u00E7\u00E3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00F3digo de identifica\u00E7\u00E3o do acordo (id). (required)
        :return: AcordoDetalheResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `consultar_using_get`")

        resource_path = '/api/acordos/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AcordoDetalheResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_pagamentos_using_get1(self, **kwargs):
        """
        Lista hist\u00F3rico de pagamentos
        Este recurso permite listar todos os Pagamentos realizados independente do seu Status de Processamento.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_pagamentos_using_get1(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: Tipo de ordena\u00E7\u00E3o dos registros.
        :param int page: P\u00E1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00E7\u00E3o (Default = 50, Max = 50)
        :param int id_conta: C\u00F3digo de Identifica\u00E7\u00E3o da Conta
        :param int id_pagamento: C\u00F3digo de Identifica\u00E7\u00E3o do Pagamento
        :param int id_estabelecimento: C\u00F3digo de Identifica\u00E7\u00E3o do Estabelecimento onde o Pagamento foi realizado, quando este for o local de pagamento
        :param int id_banco: C\u00F3digo de Identifica\u00E7\u00E3o da Institui\u00E7\u00E3o Banc\u00E1ria onde o Pagamento foi realizado, quando este for o local de pagamento
        :param int id_cartao: C\u00F3digo de Identifica\u00E7\u00E3o do Cart\u00E3o
        :param str data_hora_pagamento: Data e Hora da realiza\u00E7\u00E3o do Pagamento. Quando feito em Institui\u00E7\u00E3o Banc\u00E1ria, o hor\u00E1rio do pagamento \u00E9 exibido com valor zero
        :param int status: C\u00F3digo de Identifica\u00E7\u00E3o do Status do Pagamento
        :return: PageHistoricoPagamentoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'id_conta', 'id_pagamento', 'id_estabelecimento', 'id_banco', 'id_cartao', 'data_hora_pagamento', 'status']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_pagamentos_using_get1" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/pagamentos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'id_pagamento' in params:
            query_params['idPagamento'] = params['id_pagamento']
        if 'id_estabelecimento' in params:
            query_params['idEstabelecimento'] = params['id_estabelecimento']
        if 'id_banco' in params:
            query_params['idBanco'] = params['id_banco']
        if 'id_cartao' in params:
            query_params['idCartao'] = params['id_cartao']
        if 'data_hora_pagamento' in params:
            query_params['dataHoraPagamento'] = params['data_hora_pagamento']
        if 'status' in params:
            query_params['status'] = params['status']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageHistoricoPagamentoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get(self, **kwargs):
        """
        Lista os acordos existentes na base
        Este m\u00E9todo permite que sejam listados todos os acordos existentes na base do emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sort: Tipo de ordena\u00E7\u00E3o dos registros.
        :param int page: P\u00E1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00E7\u00E3o (Default = 50, Max = 50)
        :param int id_conta: C\u00F3digo Identificador da conta na base (id)
        :param int status_acordo: Status do acordo na base
        :param str data_acordo: Data do acordo
        :param int quantidade_parcelas: Quantidade de parcelas
        :return: PageAcordoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'limit', 'id_conta', 'status_acordo', 'data_acordo', 'quantidade_parcelas']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/acordos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'status_acordo' in params:
            query_params['statusAcordo'] = params['status_acordo']
        if 'data_acordo' in params:
            query_params['dataAcordo'] = params['data_acordo']
        if 'quantidade_parcelas' in params:
            query_params['quantidadeParcelas'] = params['quantidade_parcelas']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageAcordoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
