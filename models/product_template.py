# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ["product.template", "mail.thread", "mail.activity.mixin"]
    _check_company_auto = True

    category_code = fields.Char("Category Code", related="categ_id.code", tracking=True)
    product_product_id = fields.Many2one('product.product', string='Product Product')
    product_class_id = fields.Many2one(
        "product.class",
        string="Product Class",
        tracking=True,
        change_default=True,
        # related="product_product_id.product_class_id",
        readonly=False,
        # store=True,
    )
    product_class_code = fields.Char(
        "Product CLass Code",
        related="product_class_id.code",
        tracking=True,
    )
    product_brand_ids = fields.One2many(
        "product.brand", "product_template_id", string="Product Brand"
    )
    product_material_ids = fields.One2many(
        "product.material", "product_template_id", string="Product Material"
    )
    optional_product_ids = fields.Many2many(
        "product.template",
        "product_optional_rel",
        "src_id",
        "dest_id",
        string="Optional Products",
        help="Optional Products are suggested "
        "whenever the customer hits *Add to Cart* (cross-sell strategy, "
        "e.g. for computers: warranty, software, etc.).",
        check_company=True,
    )

    @api.onchange('product_class_id')
    def _onchange_product_class_id(self):
        self.product_variant_ids.product_class_id = self.product_class_id

    @api.depends(
        "attribute_line_ids.value_ids.is_custom",
        "attribute_line_ids.attribute_id.create_variant",
    )
    def _compute_has_configurable_attributes(self):
        """A product is considered configurable if:
        - It has dynamic attributes
        - It has any attribute line with at least 2 attribute values configured
        - It has at least one custom attribute value"""
        for product in self:
            product.has_configurable_attributes = (
                any(
                    attribute.create_variant == "dynamic"
                    for attribute in product.mapped("attribute_line_ids.attribute_id")
                )
                or any(
                    len(attribute_line_id.value_ids) >= 2
                    for attribute_line_id in product.attribute_line_ids
                )
                or any(
                    attribute_value.is_custom
                    for attribute_value in product.mapped(
                        "attribute_line_ids.value_ids"
                    )
                )
            )

    def get_single_product_variant(self):
        """Method used by the product configurator to check if the product is configurable or not.

        We need to open the product configurator if the product:
        - is configurable (see has_configurable_attributes)
        - has optional products"""
        self.ensure_one()
        res = super(ProductTemplate, self).get_single_product_variant()
        if res.get("product_id", False):
            has_optional_products = False
            for optional_product in self.product_variant_id.optional_product_ids:
                if (
                    optional_product.has_dynamic_attributes()
                    or optional_product._get_possible_variants(
                        self.product_variant_id.product_template_attribute_value_ids
                    )
                ):
                    has_optional_products = True
                    break
            res.update({"has_optional_products": has_optional_products})
        return res
