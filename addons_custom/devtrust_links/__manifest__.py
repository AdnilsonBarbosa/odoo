{
    'name': 'Important Links',
    'version': '1.0',
    'category': 'Human Resources',
    'summary':'Este App serve para listar todos os links importante da empresa devtrust',
    'author': 'Anilson Barbosa, Amadou veiga, Edmilson Fernandes',
    'company':'DevTrust Consulting',
    'website':'https://www.devtrust.cv/',
    'web_icon': 'static/description/icon.png',
    
    'depends': ['base'],
    'data': [
        
        'views/devlinks_views.xml',
        'security/ir.model.access.csv',
        'security/security.xml'
        
        
         
       
    ],
    'application': True,
}
