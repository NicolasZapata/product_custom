from odoo import fields, models, api, _


class ProductProduct(models.Model):
    _inherit = "product.template.attribute.value"

    attribute_type = fields.Selection(
        [("brand", "Brand"), ("material", "Material"), ("other", "Other")],
        string="Attribute Type",
        related="attribute_line_id.attribute_type",
    )
