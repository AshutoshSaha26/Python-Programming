def check_season(month):
    if(month=='Nov' or month=='Dec' or month=='Jan'):
        return "Winter"
    elif(month=='Feb' or month=='Mar' or month=='Apr'):
        return "Spring"
    elif(month=='May' or month=='Jun' or month=='Jul'):
        return "Summer"
    elif(month=='Aug' or month=='Sep' or month=='Oct'):
        return "Monsoon"
month=input("Enter month:")
r=check_season(month)
print(f"The season for the month {month} is {r}")