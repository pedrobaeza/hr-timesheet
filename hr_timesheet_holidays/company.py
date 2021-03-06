# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier (Camptocamp)
#    Copyright 2011 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm, fields

class ResCompany(orm.Model):
    _inherit = 'res.company'
    _columns = {
        'timesheet_hours_per_day': fields.float('Timesheet Hours Per Day', digits=(2,2))
        }

    _defaults = {
        'timesheet_hours_per_day': 8.0
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
