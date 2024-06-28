{
    'name': 'Important Links',
    'version': '1.0',
    'category': 'Human Resources/Important Links',
    'summary':'Este App serve para listar todos os links importante da empresa devtrust',
    'author': 'Anilson Barbosa, Amadou veiga, Edmilson Fernandes',
    'company':'DevTrust Consulting',
    'website':'https://www.devtrust.cv/',
    
    'depends': ['base'],
    'data': [
        
        'views/devlinks_views.xml',
        'security/ir.model.access.csv',
        'security/security.xml'
        
         
       
    ],
    'application': True,
    'installable': True,
    

   
    'license': 'LGPL-3',

    
}
