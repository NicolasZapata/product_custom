from odoo import _, api, fields, models

class ProductMaterial(models.Model):
  _name = 'product.material'
  _description = 'Product Material'
  
  name = fields.Char(string='Name')
  code = fields.Char(string='Code')