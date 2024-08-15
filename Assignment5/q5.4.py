it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_it_companies = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['LinkedIn', 'Netflix', 'Adobe'])
it_companies.remove('Oracle')
try:
    it_companies.remove('NonExistentCompany')
except KeyError:
    print("remove() raised a KeyError because the company was not found in the set.")
it_companies.discard('NonExistentCompany')  
print("Length of it_companies:", length_it_companies)
print("IT companies set after additions and removal:", it_companies)
