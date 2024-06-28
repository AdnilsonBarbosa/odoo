from odoo  import models , fields


class  FunxionarioDev(models.Model):
     #Herdando os dados da tabela funcionario na base de dados rh
    _inherit = 'hr.employee'
    
    
    
    anonsc = fields.Char(string="Mes Aniversario")

