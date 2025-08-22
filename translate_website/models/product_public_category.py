from odoo import models


class ProductPublicCategory(models.Model):
    _name = "product.public.category"
    _inherit = ['product.public.category', 'otk.translation.mixin']