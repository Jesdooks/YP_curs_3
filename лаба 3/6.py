from decimal import Decimal, getcontext

getcontext().prec = 28  # установка точности Decimal 28 значащих цифр в вычислениях

def deposit_calculator(principal: str, annual_rate: str, years: int):
    P = Decimal(principal) / 100  # перевод копеек в рубли
    t = Decimal(annual_rate) / 100  # годовая ставка в виде десятичной дроби
    n = 12  # месячная капитализация

    S = P * (1 + t / n) ** (n * years)

    final_amount = S.quantize(Decimal('0.01'))  # округление до копеек
    profit = (final_amount - P).quantize(Decimal('0.01'))

    return final_amount, profit


final, earned = deposit_calculator('1000000', '7.5', 3)
print(f'Итоговая сумма: {final} руб.')
print(f'Прибыль: {earned} руб.')
