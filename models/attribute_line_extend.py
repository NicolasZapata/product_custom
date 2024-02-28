from odoo import fields, models, api, _


class ProductProduct(models.Model):
    _inherit = "product.template.attribute.line"

    attribute_type = fields.Selection(
        [("brand", "Brand"), ("material", "Material"), ("other", "Other")],
        string="Attribute Type",
        default="other",
    )
