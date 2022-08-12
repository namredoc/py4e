hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
standart_pay = 40 * rate
if hours <= (40):
    print(standart_pay)

if hours > (40):
    overtime_h = hours - 40
    overtime_r = (rate * 1.5) * overtime_h
    print(overtime_r + standart_pay)
    
