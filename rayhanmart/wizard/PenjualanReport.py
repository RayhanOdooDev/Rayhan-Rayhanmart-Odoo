from odoo import api, fields, models


class PenjualanReport(models.Model):
    _name = 'rayhanmart.penjualanreport'
    _description = 'New Description'

    konsumen_id = fields.Many2one(comodel_name='res.partner', 
                                string='Konsumen',
                                required=False)
    dari_tgl = fields.Date(string='Dari Tanggal', 
                                required=False)
    ke_tgl = fields.Date(string='Ke Tanggal', 
                                required=False)
    
    
    def action_penjualan_report(self):
        filter = []
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['rayhanmart.penjualan'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualan': penjualan
        }
        return self.env.ref('rayhanmart.wizard_penjualanreport_pdf').report_action(self, data=data)
        

    
