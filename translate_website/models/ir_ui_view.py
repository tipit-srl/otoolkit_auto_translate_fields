from odoo import models


class View(models.Model):
    _name = 'ir.ui.view'
    _inherit = ['ir.ui.view', 'otk.translation.mixin']