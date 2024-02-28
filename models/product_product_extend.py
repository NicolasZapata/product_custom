from odoo import fields, models, api, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    brand_id = fields.Many2many(
        comodel_name="product.template.attribute.value",
        relation="x_product_template_attribute_brand_rel",
        column1="product_id",
        column2="product_attribute_id",
        string="Brand",
        compute_sudo=False,
        compute="_compute_select_variant_brand",
        search="_search_select_variant_brand",
    )
    brand_id2 = fields.Many2many(
        comodel_name="product.template.attribute.value",
        relation="x_product_template_attribute_brand_rel",
        column1="product_id",
        column2="product_attribute_id",
        string="Marca",
        store=True,
    )
    material_id = fields.Many2many(
        comodel_name="product.template.attribute.value",
        relation="x_product_template_attribute_material_rel",
        column1="product_id",
        column2="product_material_id",
        string="Material",
        compute_sudo=False,
        compute="_compute_select_variant_material",
        search="_search_select_variant_material",
    )
    material_id2 = fields.Many2many(
        comodel_name="product.template.attribute.value",
        relation="x_product_template_attribute_material_rel",
        column1="product_id",
        column2="product_material_id",
        string="Material",
        store=True,
    )
    product_brand_id = fields.Many2one("product.brand", string="Brand Id")
    product_material_id = fields.Many2one("product.material", string="Product Material")

    @api.depends("product_template_variant_value_ids")
    def _compute_select_variant_brand(self):
        for rec in self:
            if rec.product_template_variant_value_ids:
                vat = rec.mapped("product_template_variant_value_ids").filtered(
                    lambda pl: pl.attribute_type == "brand"
                )
                rec.brand_id = vat
                rec.brand_id2 = vat
            else:
                rec.brand_id = False

    def _search_select_variant_brand(self, operator, value):
        value_1 = value.upper()  # Convierte a mayuscula
        vat = []
        name = self.env["product.template.attribute.value"].search(
            [("name", "=", value_1)]
        )
        data = self.env["product.product"].search(
            [("product_template_variant_value_ids", "in", name.ids)]
        )
        if data:
            for rec in data:
                vat.append(rec.id)
        else:
            vat = []
        return [("id", "in", vat)]

    @api.depends("product_template_variant_value_ids")
    def _compute_select_variant_material(self):
        for rec in self:
            if rec.product_template_variant_value_ids:
                vat = rec.mapped("product_template_variant_value_ids").filtered(
                    lambda pl: pl.attribute_type == "material"
                )
                rec.material_id = vat
                rec.material_id2 = vat
            else:
                rec.material_id = False

    def _search_select_variant_material(self, operator, value):
        value_1 = value.upper()  # Convierte a mayuscula
        vat = []
        name = self.env["product.template.attribute.value"].search(
            [("name", "=", value_1)]
        )
        data = self.env["product.product"].search(
            [("product_template_variant_value_ids", "in", name.ids)]
        )
        if data:
            for rec in data:
                vat.append(rec.id)
        else:
            vat = []
        return [("id", "in", vat)]
