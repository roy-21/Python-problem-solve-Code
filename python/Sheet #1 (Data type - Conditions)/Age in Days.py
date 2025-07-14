N=int(input())

years = N // 365
remain_days= N % 365
months = remain_days // 30
days=remain_days % 30

print(f"{years} years, {months} months, {days} days")
