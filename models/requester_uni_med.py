# -*- coding: utf-8 -*-
from odoo import api, fields, models, api, _
from datetime import datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class Requesterunidaddemedida(models.Model):
    _name = 'udm.udm'
    _description = 'Request UdM'

    name = fields.Char(string='Unidad de Medida')
