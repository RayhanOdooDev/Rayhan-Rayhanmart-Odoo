from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'rayhanmart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    barang_id = fields.Many2many(comodel_name='rayhanmart.barang', string='Barang')
    
    
