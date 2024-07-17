from  odoo import models, fields


from odoo import models, fields


class LinkCategory(models.Model):
    _name = 'link.category'
    _description = 'Link Category'

    name = fields.Char(string='Category Name', required=True)
    
class Devlinks(models.Model):
    _name = 'important.link'
    _description = 'Links devtrust'
    
    
    image_1920 =fields.Image("imagem")
    nome = fields.Char(string='Título', required=True)
    url = fields.Html(string='URL', required=True, help="Insira o link completo, por exemplo: <a href='http://www.example.com'>Link</a>")
    descricao = fields.Text(string='Descrição')
    category_id = fields.Many2one('link.category', string='Categoria')
    user_ids = fields.Many2many('res.users', string='Utizadores Associados')
    

    
    
    
    
    
 