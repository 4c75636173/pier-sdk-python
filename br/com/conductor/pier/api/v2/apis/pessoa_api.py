# coding: utf-8

"""
PessoaApi.py
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


class PessoaApi(object):
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

    def alterar_using_put1(self, id, nome, tipo, **kwargs):
        """
        Atualiza os dados de uma determinada Pessoa
        Este m\u00C3\u00A9todo permite que seja alterado na base do emissor um registro de determinada Pessoa.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alterar_using_put1(id, nome, tipo, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID da Pessoa (required)
        :param str nome: Apresenta o 'Nome Completo da PF' ou o 'Nome Completo da Raz\u00C3\u00A3o Social (Nome Empresarial)'. (required)
        :param str tipo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo da Pessoa, sendo: (\"PF\": Pessoa F\u00C3\u00ADsica), (\"PJ\": Pessoa Jur\u00C3\u00ADdica). (required)
        :param str cpf: N\u00C3\u00BAmero do CPF, quando PF.
        :param str cnpj: N\u00C3\u00BAmero do CNPJ, quando PJ.
        :param date data_nascimento: Data de Nascimento da Pessoa, quando PF, ou a Data de Abertura da Empresa, quando PJ.
        :param str sexo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).
        :return: Pessoa
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'tipo', 'cpf', 'cnpj', 'data_nascimento', 'sexo']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alterar_using_put1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `alterar_using_put1`")
        # verify the required parameter 'nome' is set
        if ('nome' not in params) or (params['nome'] is None):
            raise ValueError("Missing the required parameter `nome` when calling `alterar_using_put1`")
        # verify the required parameter 'tipo' is set
        if ('tipo' not in params) or (params['tipo'] is None):
            raise ValueError("Missing the required parameter `tipo` when calling `alterar_using_put1`")

        resource_path = '/api/pessoas'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'tipo' in params:
            query_params['tipo'] = params['tipo']
        if 'cpf' in params:
            query_params['cpf'] = params['cpf']
        if 'cnpj' in params:
            query_params['cnpj'] = params['cnpj']
        if 'data_nascimento' in params:
            query_params['dataNascimento'] = params['data_nascimento']
        if 'sexo' in params:
            query_params['sexo'] = params['sexo']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Pessoa',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def consultar_using_get3(self, id_pessoa, **kwargs):
        """
        Apresenta os dados de uma determinada Pessoa
        Este m\u00C3\u00A9todo permite que sejam listadas as Pessoas existentes na base de dados do Emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consultar_using_get3(id_pessoa, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_pessoa: ID da Pessoa (required)
        :return: Pessoa
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_pessoa']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_using_get3" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id_pessoa' is set
        if ('id_pessoa' not in params) or (params['id_pessoa'] is None):
            raise ValueError("Missing the required parameter `id_pessoa` when calling `consultar_using_get3`")

        resource_path = '/api/pessoas/{id_pessoa}'.replace('{format}', 'json')
        path_params = {}
        if 'id_pessoa' in params:
            path_params['id_pessoa'] = params['id_pessoa']

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
                                            response_type='Pessoa',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def listar_using_get3(self, **kwargs):
        """
        Lista as Pessoas cadastradas no Emissor
        Este m\u00C3\u00A9todo permite que sejam listadas as Pessoas existentes na base de dados do Emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.listar_using_get3(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: C\u00C3\u00B3digo de Identifica\u00C3\u00A7\u00C3\u00A3o da Pessoa (id).
        :param str nome: Apresenta o 'Nome Completo da PF' ou o 'Nome Completo da Raz\u00C3\u00A3o Social (Nome Empresarial)'.
        :param str tipo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo da Pessoa, sendo: (\"PF\": Pessoa F\u00C3\u00ADsica), (\"PJ\": Pessoa Jur\u00C3\u00ADdica).
        :param str cpf: N\u00C3\u00BAmero do CPF, quando PF.
        :param str cnpj: N\u00C3\u00BAmero do CNPJ, quando PJ.
        :param date data_nascimento: Data de Nascimento da Pessoa, quando PF, ou a Data de Abertura da Empresa, quando PJ.
        :param str sexo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).
        :param int page: P\u00C3\u00A1gina solicitada (Default = 0)
        :param int limit: Limite de elementos por solicita\u00C3\u00A7\u00C3\u00A3o (Default = 100, Max = 100)
        :return: PagePessoas
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'nome', 'tipo', 'cpf', 'cnpj', 'data_nascimento', 'sexo', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method listar_using_get3" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/pessoas'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'tipo' in params:
            query_params['tipo'] = params['tipo']
        if 'cpf' in params:
            query_params['cpf'] = params['cpf']
        if 'cnpj' in params:
            query_params['cnpj'] = params['cnpj']
        if 'data_nascimento' in params:
            query_params['dataNascimento'] = params['data_nascimento']
        if 'sexo' in params:
            query_params['sexo'] = params['sexo']
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
                                            response_type='PagePessoas',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def salvar_using_post1(self, nome, tipo, **kwargs):
        """
        Realiza o cadastro de um nova Pessoa
        Este m\u00C3\u00A9todo permite que seja cadastrado uma nova Pessoa na base de dados do Emissor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.salvar_using_post1(nome, tipo, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str nome: Apresenta o 'Nome Completo da PF' ou o 'Nome Completo da Raz\u00C3\u00A3o Social (Nome Empresarial)'. (required)
        :param str tipo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do tipo da Pessoa, sendo: (\"PF\": Pessoa F\u00C3\u00ADsica), (\"PJ\": Pessoa Jur\u00C3\u00ADdica). (required)
        :param str cpf: N\u00C3\u00BAmero do CPF, quando PF.
        :param str cnpj: N\u00C3\u00BAmero do CNPJ, quando PJ.
        :param date data_nascimento: Data de Nascimento da Pessoa, quando PF, ou a Data de Abertura da Empresa, quando PJ.
        :param str sexo: C\u00C3\u00B3digo de identifica\u00C3\u00A7\u00C3\u00A3o do sexo da Pessoa, quando PF, sendo: (\"M\": Masculino), (\"F\": Feminino), (\"O\": Outro), (\"N\": N\u00C3\u00A3o Especificado).
        :return: Pessoa
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['nome', 'tipo', 'cpf', 'cnpj', 'data_nascimento', 'sexo']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method salvar_using_post1" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'nome' is set
        if ('nome' not in params) or (params['nome'] is None):
            raise ValueError("Missing the required parameter `nome` when calling `salvar_using_post1`")
        # verify the required parameter 'tipo' is set
        if ('tipo' not in params) or (params['tipo'] is None):
            raise ValueError("Missing the required parameter `tipo` when calling `salvar_using_post1`")

        resource_path = '/api/pessoas'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'nome' in params:
            query_params['nome'] = params['nome']
        if 'tipo' in params:
            query_params['tipo'] = params['tipo']
        if 'cpf' in params:
            query_params['cpf'] = params['cpf']
        if 'cnpj' in params:
            query_params['cnpj'] = params['cnpj']
        if 'data_nascimento' in params:
            query_params['dataNascimento'] = params['data_nascimento']
        if 'sexo' in params:
            query_params['sexo'] = params['sexo']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Pessoa',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
