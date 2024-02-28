from odoo import _, api, fields, models

class ProductBrand(models.Model):
  _name = 'product.brand'
  _description = 'Brand'
  
  name = fields.Char(string='Name')
  code = fields.Char(string='Code')