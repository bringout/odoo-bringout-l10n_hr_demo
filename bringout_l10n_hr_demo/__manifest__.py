{
    "name": "Croatia — Demo Localization (bring.out test-bed)",
    "summary": "Minimal Croatia CoA + PDV taxes for demo / multi-company test bed (NOT for production)",
    "description": """
Croatia Demo Localization
=========================

Minimal chart of accounts (~12 accounts) and dominant PDV tax templates
(25%, 13%, 5%, 0% export) for use as a test-bed for multi-company
features. NOT a production localization — do not use as a replacement
for a real l10n_hr.
    """,
    "version": "19.0.1.0.0",
    "author": "bring.out doo Sarajevo",
    "website": "https://www.bring.out.ba",
    "category": "Localization",
    "license": "AGPL-3",
    "depends": [
        "account",
    ],
    "data": [
        "data/account_chart_template.xml",
        "data/account_account_template.xml",
        "data/account_tax_template.xml",
        "data/account_chart_template_configure.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
