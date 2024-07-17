from odoo import models, fields

class MyModel(models.Model):
    _inherit = 'hr.employee'
    

    # Adicione mais campos conforme necessário
    birth_island = fields.Selection([
        ('Boa Vista', 'Boa Vista'),
        ('Brava', 'Brava'),
        ('Fogo', 'Fogo'),
        ('Maio', 'Maio'),
        ('Sal', 'Sal'),
        ('Santiago', 'Santiago'),
        ('Santo Antão', 'Santo Antão'),
        ('São Nicolau', 'São Nicolau'),
        ('São Vicente', 'São Vicente')
    ], string="Ilha de Nascimento")
    num_cam = fields.Char(string='Numero de Camisa')
    concelho = fields.Char(string='Concelho de Origem')
    data_inicio = fields.Date(string='Data de Início')
    nosi_p = fields.Selection([
        ('Sim', 'Sim'),
        ('Não', 'Não')
    ], string="Passagem Pela Nosi")
