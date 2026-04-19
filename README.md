# bringout_l10n_hr_demo — Croatia Demo Localization

Minimal Croatia (HR) localization **for demo / test-bed use only**.
NOT a production localization — ships ~12 accounts and the four dominant
PDV tax rates. Use real `l10n_hr` for actual Croatian accounting.

## What's inside

* A minimal **chart of accounts template** (`bringout_l10n_hr_demo.chart_template_hr_demo`)
  covering bank/cash/receivables/payables/income/expense/tax/payroll.
* **PDV tax templates**:
  * `hr_pdv_25` — 25% standard (sales + purchase)
  * `hr_pdv_13` — 13% reduced
  * `hr_pdv_5` — 5% super-reduced
  * `hr_pdv_0_export` — 0% export

## Intended consumer

`odoo-bringout-multi_company_example_ba_hr_si_data` — loads this CoA onto
`CompanyHR-1` and `CompanyHR-2`.

## License

AGPL-3
