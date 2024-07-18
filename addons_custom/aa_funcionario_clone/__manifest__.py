# -*- coding: utf-8 -*-
{
    'name': 'Funcionario Clone',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Customização do módulo de Funcionários do Odoo',
    'description': """
        Este módulo personaliza e estende o módulo padrão de Funcionários do Odoo
        para incluir campos personalizados e ajustes na interface.
    """,
    'author': 'Amadou Veiga',
    'website': '',
    'depends': ['base', 'hr', 'hr_skills', 'mail'],
    'data': [
        'views/action.xml',
        'views/my_view.xml',
       
        

    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
