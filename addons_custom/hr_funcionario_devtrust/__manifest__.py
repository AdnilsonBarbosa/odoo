# __manifest__.py
{
    'name': 'Funcionario Devtrust',
    'version': '1.0',
    'summary': 'Customizations for the Employee Module',
    'description': 'Modifies fields of the Employee module.',
    'author': 'Adnilson Barbosa',
    'depends': ['base', 'hr'],
    'data': [
        'views/custom_employee_views.xml',
        'views/menu.xml',
        
        
    ],
    'installable': True,
    'application': True,
}
