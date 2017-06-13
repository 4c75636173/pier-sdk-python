# coding: utf-8

"""
CompraApi.py
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


class CompraApi(object):
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

    def efetivar_antecipacao_using_post(self, id_conta, id, quantidade_parcelas, **kwargs):
        """
        Faz a efetiva\u00C3\u00A7\u00C3\u00A3o da antecipa\u00C3\u00A7\u00C3\u00A3o
        Metodo responsavel pela efetiva\u00C3\u00A7\u00C3\u00A3o da antecipa\u00C3\u00A7\u00C3\u00A3o.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.efetivar_antecipacao_using_post(id_conta, id, quantidade_parcelas, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Conta. (required)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da compra. (required)
        :param int quantidade_parcelas: Quantidade de parcelas para serem antecipadas (quantidadeParcelas). (required)
        :return: AntecipacaoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'id', 'quantidade_parcelas']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method efetivar_antecipacao_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `efetivar_antecipacao_using_post`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `efetivar_antecipacao_using_post`")
        # verify the required parameter 'quantidade_parcelas' is set
        if ('quantidade_parcelas' not in params) or (params['quantidade_parcelas'] is None):
            raise ValueError("Missing the required parameter `quantidade_parcelas` when calling `efetivar_antecipacao_using_post`")

        resource_path = '/api/compras/{id}/efetivar-antecipacao'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AntecipacaoResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get5(self, id_conta, **kwargs):
        """
        Listar compras
        Lista as compras de uma conta.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get5(id_conta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo identificador da conta da Compra. (required)
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 50, Max = 50)
        :param int id_compra: C\u00C3\u00B3digo identificador da Compra.
        :param bool parcelada: Indica se a compra \u00C3\u00A9 parcelada.
        :param bool juros: Indica se a compra \u00C3\u00A9 com ou sem juros.
        :param str tipo_transacao: Indica se a compra \u00C3\u00A9 ON-US ou OFF-US
        :return: PageCompras
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'page', 'limit', 'id_compra', 'parcelada', 'juros', 'tipo_transacao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get5" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `listar_using_get5`")

        resource_path = '/api/compras'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'id_compra' in params:
            query_params['idCompra'] = params['id_compra']
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']
        if 'parcelada' in params:
            query_params['parcelada'] = params['parcelada']
        if 'juros' in params:
            query_params['juros'] = params['juros']
        if 'tipo_transacao' in params:
            query_params['tipoTransacao'] = params['tipo_transacao']

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
                                            response_type='PageCompras',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def simular_antecipacao_using_get(self, id_conta, id, **kwargs):
        """
        Simular antecipa\u00C3\u00A7\u00C3\u00A3o de parcelas
        Simula a antecipa\u00C3\u00A7\u00C3\u00A3o de parcelas de uma compra, listando todos os planos de parcelamento dispon\u00C3\u00ADveis.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simular_antecipacao_using_get(id_conta, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_conta: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o da conta (id). (required)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da compra. (required)
        :return: AntecipacaoSimuladaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_conta', 'id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simular_antecipacao_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_conta' is set
        if ('id_conta' not in params) or (params['id_conta'] is None):
            raise ValueError("Missing the required parameter `id_conta` when calling `simular_antecipacao_using_get`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `simular_antecipacao_using_get`")

        resource_path = '/api/compras/{id}/simular-antecipacao'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'id_conta' in params:
            query_params['idConta'] = params['id_conta']

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
                                            response_type='AntecipacaoSimuladaResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response