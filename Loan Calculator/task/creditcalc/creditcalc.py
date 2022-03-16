from math import log, ceil
import argparse


def get_plural_text(amount, text):
    if amount == 0:
        return ""
    elif amount == 1:
        return f"1 {text}"
    else:
        return f"{amount} {text}s"


def print_overpayment(count, pay, total):
    overpayment = round(count * pay - total)
    print(f"Overpayment = {overpayment}")


def diff_payment(total, count, percent, i):
    diff_pay = total * (1 / count + percent * (1 - (i - 1) / count))
    return ceil(round(diff_pay, 2))


def calc_diff_payment_amount(total, count, persent):
    pay_sum = 0
    for i in range(1, count + 1):
        monthly = diff_payment(total, count, persent, i)
        print(f"Month {i}: payment is {monthly}")
        pay_sum += monthly
    print(f"\nOverpayment = {round(pay_sum - total)}")


def get_factor(count, percent):
    k = (percent + 1) ** count
    return percent * k / (k - 1)


def calc_periods_count(total, pay, percent):
    month_count = ceil(log(pay / (pay - percent * total), percent + 1))
    years = get_plural_text(month_count // 12, "year")
    months = get_plural_text(month_count % 12, "month")
    conjunction = " and "
    if years == "" or months == "":
        conjunction = ""
    years_and_months = years + conjunction + months
    print(f"It will take {years_and_months} to repay this loan!")
    print_overpayment(month_count, pay, total)


def calc_payment_amount(total, count, percent):
    monthly = ceil(total * get_factor(count, percent))
    print(f"Your annuity payment = {monthly}!")
    print_overpayment(count, monthly, total)


def calc_loan_amount(monthly, count, percent):
    total = ceil(monthly / get_factor(count, percent))
    print(f"Your loan principal = {total}!")
    print_overpayment(count, monthly, total)


parser = argparse.ArgumentParser(description="Loan command line calculator")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interests")

args = parser.parse_args()
isArgsCorrect = args.type is not None and args.interests is not None
isArgsCorrect = isArgsCorrect and args.type in ("annuity", "diff")
arg_list = [float(i) if i is not None else i for i in (args.principal, args.payment, args.periods, args.interests)]
isArgsCorrect = isArgsCorrect and arg_list.count(None) == 1

if isArgsCorrect:
    if arg_list[2] is not None:
        arg_list[2] = round(arg_list[2])
    arg_list[3] = arg_list[3] / 1200

    if args.type == "annuity":
        if arg_list[0] is None:
            calc_loan_amount(arg_list[1], arg_list[2], arg_list[3])
        elif arg_list[1] is None:
            calc_payment_amount(arg_list[0], arg_list[2], arg_list[3])
        elif arg_list[2] is None:
            calc_periods_count(arg_list[0], arg_list[1], arg_list[3])
    elif args.type == "diff":
        calc_diff_payment_amount(arg_list[0], arg_list[2], arg_list[3])
else:
    print("Incorrect parameters")
