from odoo import models


class Page(models.Model):
    _name = 'website.page'
    _inherit = ['website.page', 'otk.translation.mixin']
