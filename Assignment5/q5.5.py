A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_union_B = A.union(B)
A_intersection_B = A.intersection(B)
is_A_subset_of_B = A.issubset(B)
are_A_and_B_disjoint = A.isdisjoint(B)
A_join_B = A.union(B)  
B_join_A = B.union(A)  
A_symmetric_difference_B = A.symmetric_difference(B)
del A
del B
print("Join A and B:", A_union_B)
print("A intersection B:", A_intersection_B)
print("Is A subset of B:", is_A_subset_of_B)
print("Are A and B disjoint sets:", are_A_and_B_disjoint)
print("Symmetric difference between A and B:", A_symmetric_difference_B)
try:
    print(A)  
except NameError:
    print("Set A has been deleted.")   
try:
    print(B)  
except NameError:
    print("Set B has been deleted.")
