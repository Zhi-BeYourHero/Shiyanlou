# -*- coding: utf-8 -*-
from collections import namedtuple


IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

Insurance = {
    "yanglao": 0.08,
    "yiliao": 0.02,
    "shiye": 0.005,
    "gongshang": 0.00,
    "shengyu": 0.00,
    "gongjijin": 0.06
}


def calc_income_tax_and_remain(income):
    total_insurance_part = income * sum(Insurance.values())
    real_income = income - total_insurance_part
    taxable_part = real_income - INCOME_TAX_START_POINT
    if taxable_part <= 0:
        return '0.00','{:.2f}'.format(real_income)
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax),'{:.2f}'.format(real_income - tax)


def main():
    import sys
    for arg in sys.argv[1:]:
        employee_id, income_string = arg.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
        _, remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id,remain))
        


if __name__ == '__main__':
    main()
