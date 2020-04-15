import math

r = int(input("Enter radius of the sphere:"))
print("Volume of the sphere is:" + str(4 / 3 * math.pi * (r ** 3)))

# ---------------------------------------------

price = 24.95 * 0.6
ship_cost = 3
ship_cost_copy = 0.75
total_cost = price + ship_cost + (price + ship_cost_copy) * 59
print('Total wholesale cost for 60 copies is {0:.2f}'.format(total_cost))
#print("Total cost copy is : "+str(total_cost))

# ---------------------------------------------

start_time = (6*60 + 52)*60
easy = (8*60 + 15)*2
tempo = (7*60 + 12)*3

reach_time = start_time + easy + tempo/(60*60)

breakfast_hour = (start_time + easy + tempo)/(60*60)
breakfast_int_hour = int(breakfast_hour)

breakfast_minute  = (breakfast_hour - breakfast_int_hour)*60
breakfast_int_minute = int(breakfast_minute)

print('Breakfast is at {}:{}'.format(breakfast_int_hour,breakfast_int_minute))

