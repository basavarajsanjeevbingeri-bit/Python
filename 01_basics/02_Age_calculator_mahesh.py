present_age = int(input("Enter your age :  "))
final_age = 90



no_day_left = (final_age * 365) - (present_age * 365)
no_week_left = no_day_left//7

no_month_left = no_week_left//5

print("No of days left for u to leave in this earth is : " , no_day_left)
print("No of weeks left for u to leave in this earth is : ", no_week_left)
print("No of months left for u to leave in this earth is : ", no_month_left)