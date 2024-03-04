from odoo import _, api, fields, models

class ProductReference(models.Model):
  _name = 'product.reference'
  _inherit = ['mail.thread', 'mail.activity.mixin']
  _description = 'Product Reference'
  
  name = fields.Char('Name', tracking=True)
  code = fields.Char('Code', tracking=True)