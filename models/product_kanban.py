from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
        ('4', 'Urgent')
    ], string='Priority', default='0')