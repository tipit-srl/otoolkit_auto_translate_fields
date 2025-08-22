from odoo import models


class Blog(models.Model):
    _name = 'blog.post'
    _inherit = ['blog.post', 'otk.translation.mixin']
