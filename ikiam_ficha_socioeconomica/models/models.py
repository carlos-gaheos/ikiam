# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CountryState(models.Model):
    _inherit = 'res.country.state'
   
    ponderacion = fields.Integer('Ponderacion')