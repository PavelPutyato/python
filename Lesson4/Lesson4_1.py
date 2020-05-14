from sys import argv

script_name, earnings, rate, prize = argv
def salary(earnings, rate, prize):
    salary_full = float(earnings) * float(rate) + float(prize)
    print(f'Расчет заработной платы: {earnings} часов Х {rate} руб за час + пермия {prize} руб = '
          f'{round(salary_full, 2)} руб')
    return
salary(earnings, rate, prize)