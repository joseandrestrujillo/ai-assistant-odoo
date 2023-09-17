# -*- coding: utf-8 -*-
{
    'name': "Asistente SQL con IA",
    'application': True,
    'summary': """
        Cualquier consulta a los datos de tu empresa, sin complicaciones.
        """,

    'description': """
        Este modulo te permite realizar consultas sobre los datos de tu e-comerce en lenguaje natural.
    """,

    'author': "Ai2SQL",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'icon': '/sql_assistant/static/src/logo.png',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
