# coding: utf-8

"""
StatusParametrosApi.py
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


class StatusParametrosApi(object):
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

    def consultar_estagio_cartao_using_get(self, id_estagio_cartao, **kwargs):
        """
        Apresenta os dados de um determinado Estagio Cart\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite consultar os par\u00C3\u00A2metros de um determinado Est\u00C3\u00A1gio de Entrega do Cart\u00C3\u00A3o a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_estagio_cartao_using_get(id_estagio_cartao, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_estagio_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Entrega do Cart\u00C3\u00A3o (id). (required)
        :return: EstagioCartao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_estagio_cartao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_estagio_cartao_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_estagio_cartao' is set
        if ('id_estagio_cartao' not in params) or (params['id_estagio_cartao'] is None):
            raise ValueError("Missing the required parameter `id_estagio_cartao` when calling `consultar_estagio_cartao_using_get`")

        resource_path = '/api/estagios-cartoes/{id_estagio_cartao}'.replace('{format}', 'json')
        path_params = {}
        if 'id_estagio_cartao' in params:
            path_params['id_estagio_cartao'] = params['id_estagio_cartao']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EstagioCartao',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_status_cartao_using_get(self, id_status_cartao, **kwargs):
        """
        Apresenta os dados de um determinado Status Cart\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite consultar os par\u00C3\u00A2metros de um determinado Status de Cart\u00C3\u00A3o a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_status_cartao_using_get(id_status_cartao, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_status_cartao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Est\u00C3\u00A1gio de Entrega do Cart\u00C3\u00A3o (id). (required)
        :return: StatusCartao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_status_cartao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_status_cartao_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_status_cartao' is set
        if ('id_status_cartao' not in params) or (params['id_status_cartao'] is None):
            raise ValueError("Missing the required parameter `id_status_cartao` when calling `consultar_status_cartao_using_get`")

        resource_path = '/api/status-cartoes/{id_status_cartao}'.replace('{format}', 'json')
        path_params = {}
        if 'id_status_cartao' in params:
            path_params['id_status_cartao'] = params['id_status_cartao']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='StatusCartao',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get4(self, id_status_conta, **kwargs):
        """
        Apresenta os dados de um determinado Status Conta
        Este m\u00C3\u00A9todo permite consultar os par\u00C3\u00A2metros de um determinado Status Conta a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get4(id_status_conta, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_status_conta: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status da Conta (id). (required)
        :return: StatusConta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_status_conta']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get4" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_status_conta' is set
        if ('id_status_conta' not in params) or (params['id_status_conta'] is None):
            raise ValueError("Missing the required parameter `id_status_conta` when calling `consultar_using_get4`")

        resource_path = '/api/status-contas/{id_status_conta}'.replace('{format}', 'json')
        path_params = {}
        if 'id_status_conta' in params:
            path_params['id_status_conta'] = params['id_status_conta']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='StatusConta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get5(self, id_status_impressao, **kwargs):
        """
        Apresenta os dados de um determinado Status Impress\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite consultar os par\u00C3\u00A2metros de um determinado Status de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o a partir do seu c\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o (id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get5(id_status_impressao, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_status_impressao: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status de Impress\u00C3\u00A3o do Cart\u00C3\u00A3o (id). (required)
        :return: StatusImpressao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_status_impressao']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get5" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_status_impressao' is set
        if ('id_status_impressao' not in params) or (params['id_status_impressao'] is None):
            raise ValueError("Missing the required parameter `id_status_impressao` when calling `consultar_using_get5`")

        resource_path = '/api/status-impressoes/{id_status_impressao}'.replace('{format}', 'json')
        path_params = {}
        if 'id_status_impressao' in params:
            path_params['id_status_impressao'] = params['id_status_impressao']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='StatusImpressao',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_estagios_cartoes_using_get(self, **kwargs):
        """
        Lista as op\u00C3\u00A7\u00C3\u00B5es de Est\u00C3\u00A1gios do Cart\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite que sejam listadas as op\u00C3\u00A7\u00C3\u00B5es de Est\u00C3\u00A1gio de Entrega que podem ser atribu\u00C3\u00ADdas aos Cart\u00C3\u00B5es.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_estagios_cartoes_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id do est\u00C3\u00A1gio cart\u00C3\u00A3o
        :param str nome: Nome do est\u00C3\u00A1gio cart\u00C3\u00A3o
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageEstagiosCartoes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_estagios_cartoes_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/estagios-cartoes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageEstagiosCartoes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_status_cartoes_using_get(self, **kwargs):
        """
        Lista as op\u00C3\u00A7\u00C3\u00B5es de Status do Cart\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite que sejam listadas as possibilidades de Status que podem ser atribu\u00C3\u00ADdas aos Cart\u00C3\u00B5es.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_status_cartoes_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status do Cart\u00C3\u00A3o (id) 
        :param str nome: Nome atribu\u00C3\u00ADdo ao Status de Entrega do Cart\u00C3\u00A3o.
        :param int flag_cancela_cartao: Quando ativa, indica que ao ser atribu\u00C3\u00ADdo um idStatusCartao com essa caracter\u00C3\u00ADstica, o cart\u00C3\u00A3o ter\u00C3\u00A1 o seu idStatusCartao alterado para o que fora escolhido. Caso contr\u00C3\u00A1rio, o idStatusCartao s\u00C3\u00B3 ser\u00C3\u00A1 alterado ap\u00C3\u00B3s o desbloqueio de um novo cart\u00C3\u00A3o do mesmo Portador e Conta.
        :param int flag_cancela_no_desbloqueio: Quando ativa, indica que o cart\u00C3\u00A3o ativo que o portador possuir na mesma conta do cart\u00C3\u00A3o a ser desbloqueado, e que o status dele possua essa caracter\u00C3\u00ADstica, dever\u00C3\u00A1 ser cancelado quando um novo cart\u00C3\u00A3o for desbloqueado.
        :param int id_status_destino_desbloqueio: Indica qual o idStatusCartao que ser\u00C3\u00A1 atribu\u00C3\u00ADdo aos cart\u00C3\u00B5es que forem cancelados devido ao desbloqueio de um novo cart\u00C3\u00A3o.
        :param int id_status_destino_conta: Indica qual o idStatusCartao que ser\u00C3\u00A1 atribu\u00C3\u00ADdo a conta, caso ela seja cancelada devido ao bloqueio de um cart\u00C3\u00A3o quando for utilizado um idStatusCartao no processo de Bloqueio que possua essa caracter\u00C3\u00ADstica.
        :param int flag_cobra_tarifa: Quando ativa, indica que cart\u00C3\u00B5es que tiverem um idStatusCartao atribu\u00C3\u00ADdo com essa caracter\u00C3\u00ADstica, incluir\u00C3\u00A3o a cobran\u00C3\u00A7a de uma tarifa para a conta de acordo com os valores definidos nos par\u00C3\u00A2metros do emissor.
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageStatusCartoes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'flag_cancela_cartao', 'flag_cancela_no_desbloqueio', 'id_status_destino_desbloqueio', 'id_status_destino_conta', 'flag_cobra_tarifa', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_status_cartoes_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/status-cartoes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'flag_cancela_cartao' in params:
            query_params['flagCancelaCartao'] = params['flag_cancela_cartao']
        if 'flag_cancela_no_desbloqueio' in params:
            query_params['flagCancelaNoDesbloqueio'] = params['flag_cancela_no_desbloqueio']
        if 'id_status_destino_desbloqueio' in params:
            query_params['idStatusDestinoDesbloqueio'] = params['id_status_destino_desbloqueio']
        if 'id_status_destino_conta' in params:
            query_params['idStatusDestinoConta'] = params['id_status_destino_conta']
        if 'flag_cobra_tarifa' in params:
            query_params['flagCobraTarifa'] = params['flag_cobra_tarifa']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageStatusCartoes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get5(self, **kwargs):
        """
        Lista os Status Contas cadastrados para o Emissor
        Este m\u00C3\u00A9todo permite que sejam listados os Status Contas existentes na base de dados do Emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get5(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o do Status da Conta (id).
        :param str nome: Nome atribu\u00C3\u00ADdo ao Status da Conta.
        :param int flag_altera_limite: Par\u00C3\u00A2metro que define se o Status da Conta permite realizar a Altera\u00C3\u00A7\u00C3\u00A3o de Limites do Portador, sendo: 0: Inativo e 1: Ativo.
        :param str mensagem_consulta_negada: Apresenta o texto com o motivo que ser\u00C3\u00A1 apresentado na resposta as opera\u00C3\u00A7\u00C3\u00B5es de Listar e Consultar LimitesDisponibilidades.
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageStatusContas
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'flag_altera_limite', 'mensagem_consulta_negada', 'page', 'limit']
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


        resource_path = '/api/status-contas'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'flag_altera_limite' in params:
            query_params['flagAlteraLimite'] = params['flag_altera_limite']
        if 'mensagem_consulta_negada' in params:
            query_params['mensagemConsultaNegada'] = params['mensagem_consulta_negada']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageStatusContas',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get6(self, **kwargs):
        """
        Lista as op\u00C3\u00A7\u00C3\u00B5es de Status Impress\u00C3\u00A3o
        Este m\u00C3\u00A9todo permite que sejam listadas as op\u00C3\u00A7\u00C3\u00B5es de Status Impress\u00C3\u00A3o que podem ser atribu\u00C3\u00ADdas aos Cart\u00C3\u00B5es.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get6(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id do est\u00C3\u00A1gio cart\u00C3\u00A3o
        :param str nome: Nome do status impress\u00C3\u00A3o
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PageStatusImpressao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get6" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/status-impressoes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
        auth_settings = ['access_token']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageStatusImpressao',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response