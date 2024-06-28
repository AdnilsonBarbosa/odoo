from  odoo import models, fields

#crbelaiacao da tabela categorias de links
class LinkCategory(models.Model):
    _name = 'link.category'  #nome da base de dados
    _description = 'Link Category'  #descricao da base de dados

    name = fields.Char(string='Category Name', required=True)
    
    
   #criacao da tabela important.link 
class Devlinks(models.Model):
    _name = 'important.link' #nome da base de dados
    _description = 'Links devtrust' #descricao da base de dados
    
    #campos da tabela
    image_1920 =fields.Image("imagem")
    nome = fields.Char(string='Título', required=True)
    url = fields.Html(string='URL', required=True, help="Usa /  depois seleciona a opção do botão e depois preeenche os campos ")
    descricao = fields.Text(string='Descrição')
    category_id = fields.Many2one('link.category', string='Category')

    
    
    
    
    
 