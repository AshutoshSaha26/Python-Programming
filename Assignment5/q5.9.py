month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Fall',
    10: 'Fall', 11: 'Fall', 12: 'Winter'
}
def get_season(month_number):
    return month_to_season.get(month_number, 'Invalid month number')
month_number = int(input("Enter the month number (1-12): "))
season = get_season(month_number)
print(f"The season for month {month_number} is: {season}")
