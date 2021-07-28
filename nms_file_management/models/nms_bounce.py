# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NMSBounce(models.Model):
    _name = 'nms.bounce'
    _description = 'NMS Bounce'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'model'

    po = fields.Many2one(
        comodel_name='purchase.order',
        string='PO', tracking=True,
        required=False)
    supplier_name = fields.Many2one(
        comodel_name='res.partner',
        string='Supplier Name', tracking=True,
        required=False)
    imei = fields.Char(string='IMEI', required=False, tracking=True, )
    imei2 = fields.Char(string='IMEI2', required=False, tracking=True, )
    meid_hex = fields.Char(string='meidHEX', required=False, tracking=True, )
    meid_dec = fields.Char(string='meidDEC', required=False, tracking=True, )
    model = fields.Char(string='Model', required=True, tracking=True, )
    sim_tech = fields.Char(string=' SIM Technology', required=False, tracking=True, )
    model_number = fields.Char(string='Model Number', required=False, tracking=True, )
    capacity = fields.Char(string='Capacity', required=False, tracking=True, )
    color = fields.Char(string='Color', required=False, tracking=True, )

    def export_nms(self):
        print('replace code of export here')

    def import_nms(self):
        print('replace code of import here')
