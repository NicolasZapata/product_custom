# -*- coding: utf-8 -*-
#
# Autor: Leonardo Garavito y Nicolás Zapata
# Email: lgaravito@grupoquanam.com, nzapata@grupoquanam.com
# Desarrollador y funcional Odoo
#
{
    "name": "Product Custom",
    "summary": """
        16.0.1 Product variant attributes extension module, and wizard view for product variants in purchase orders.
        """,
    "description": """
        Product variant attributes extension module, and wizard view for product variants in purchase orders..
    """,
    "author": "Grupo Quanam Colombia, https://www.grupoquanam.com",
    "website": "https://www.grupoquanam.com",
    "category": "Stock",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "stock",
        "sale_management",
        "sale",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_extend_view.xml",
        "views/product_template_attribute_value_extend_view.xml",
        "views/product_product_extend_view.xml",
        "views/product_brand_view.xml",
        "views/product_material_views.xml",
        'views/product_category.xml',
        'views/product_class_view.xml',
        'views/product_reference_views.xml',
        # 'views/purchase_views.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
