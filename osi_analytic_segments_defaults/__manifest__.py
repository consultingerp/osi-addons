# Copyright (C) 2019 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "OSI Analytic Segments Defaults",
    "version": "12.0.1.0.0",
    "license": "LGPL-3",
    "summary": "Additional analytic segments for Analytic Defaults",
    "author": "Open Source Integrators",
    "maintainer": "Open Source Integrators",
    "website": "http://www.opensourceintegrators.com",
    "category": "Analytic Accounting",
    "depends": [
        "purchase",
        "account_analytic_default",
        "osi_analytic_segments",
    ],
    "data": [
        "views/account_analytic_default_view.xml",
    ],
    "installable": True,
}
