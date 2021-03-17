# -*- coding: utf-8 -*-
from odoo import api, fields, models, api, _
from datetime import datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class Purchaserequesterorderline(models.Model):
    _inherit = 'purchase.requester'
    prodoserv = fields.Char(string='Producto o Servicio')
    cantidad_pos = fields.Float(string='Cantidad')
    prodoserv_id = fields.Many2one('purchase.requester')
    prodoserv_order_line = fields.One2many('purchase.requester', 'prodoserv_id', string="Partida")
    product_uom = fields.Many2one('udm.udm', 'Unidad de Medida')
