#########################################################################
#                                                                       #
# Copyright (C) 2009  Sharoon Thomas                                    #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################
{
    "name" : "Magento e-commerce",
    "version" : "1.0",
    "depends" : ["base",
                 "product",
                 "product_m2mcategories",
                 'delivery',
                 "base_sale_multichannels",
                 "product_images_olbs",
                 "product_links",
                ],
    "author" : "MagentoERPconnect Core Editors",
    "description": """Magento E-commerce management
""",
    "website" : "https://launchpad.net/magentoerpconnect",
    "category" : "Generic Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
            'security/ir.model.access.csv',
            'magerp_data.xml',
            'settings/external.referential.type.csv',
            'magerp_core_view.xml',
            'product_view.xml',
            'partner_view.xml',
            'sale_view.xml',
            'product_images_view.xml',
            'magerp_menu.xml',
            'settings/external.mapping.template.csv',
            'settings/external.mappinglines.template.csv',
            'settings/magerp_product_product_type.xml',
            'delivery_view.xml',
            'product_links_view.xml'
                    ],
    "active": False,
    "installable": True,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

