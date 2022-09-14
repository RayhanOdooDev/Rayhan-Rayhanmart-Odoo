from odoo import http, models, fields
from odoo.http import request
import json

class Rayhanmart(http.Controller):
    @http.route('/rayhanmart/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['rayhanmart.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/rayhanmart/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['rayhanmart.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'barang' : s.barang_id[0].name
            })
        return json.dumps(sup)