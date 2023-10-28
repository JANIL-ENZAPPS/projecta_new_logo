# -*- coding: utf-8 -*-
{
    'name': "Projecta Expect Logo",
    'author': 'Enzapps Private Limited',
    'company': 'Enzapps Private Limited',
    'maintainer': 'Enzapps Private Limited',
    'summary': """This module is for printing E-Invoice report for Zatca(New Logo).""",

    'description': """This module is for printing E-Invoice report for Zatca(New Logi).""",
    'website': "www.enzapps.com",
    'category': 'base',
    'version': '14.0',
    'images': ['static/description/icon.png'],
    'depends': ['base', 'account', 'sale', 'purchase', 'stock', 'arabic_strings', 'enz_ksa_phase_two_zatca',
                'natcom_einvoice_formate', 'projecta_custom_formate', 'natcom_projecta_update',
                'natcom_projecta_jan_five', 'projecta_english_formate','projecta_advance_field_update'],
    'data': [
        'reports/header.xml',
        'reports/report_view.xml',
        'reports/report.xml',
        'views/company.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
