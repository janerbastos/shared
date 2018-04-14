# -*- coding: utf-8 -*-

def ENGINE_DB(path, **kwargs):
    '''
    Função responsável por manipular os valores de configuração da base de dados
    :param path: String do arquivo de configuração do banco de dados ou banco de dados
    :param kwargs: String de paramentros adicionais de configuração do banco de dados
    :return: Dicionário de dados de configuração do banco de dados
    '''

    _ENGINER = {
        'mysql': 'django.db.backends.mysql',
        'sqlite': 'django.db.backends.sqlite3',
        'postgres': '?',
    }
    _engine = kwargs.get('ENGINE', None)
    _result = {}
    if not _engine:
        _result['NAME'] = path
        _result['ENGINE'] = _ENGINER['sqlite']
    else:
        _file = open(path, 'r')
        _row = _file.readline()

        while _row:
            _row = _row.split('|')
            for i in _row:
                item = i.split('|')
                _result[item[0]] = item[1]
            _row = _file.readline()

        _file.close()

        _result['ENGINE'] = _ENGINER[_engine]

    return _result
