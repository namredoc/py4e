hours = float(input("Enter hours worked: "))
rate = float(input("Enter the rate: "))
reg_rate = hours * rate

def computepay(hours, rate):
    if hours <= 40:
        return reg_rate

    elif hours > 40:
        overtime_h = hours - 40
        overtime_r = overtime_h * (rate * 1.5) 
        total_ov = (hours - overtime_h) * rate + overtime_r
        return total_ov

pay = computepay(hours, rate)
print("Pay", pay)
