import utils as utils
import qap as qap

# count sample cos for 12 x 12
print("\n12 x 12")
permHad12 = [int(x) for x in "3,10,11,2,12,5,6,7,8,1,4,9".split(",")]
had12 = qap.QAP("had12.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had12.D, had12.F, permHad12), ",", permHad12)
print("Random Search: ")
print(had12.random_search(1000))
print("Greedy Algorithm: ")
print(had12.greedy_algorithm())


# count sample for 14 x 14
print("\n14 x 14")
permHad14 = [int(x) for x in "8,13,10,5,12,11,2,14,3,6,7,1,9,4".split(",")]
had14 = qap.QAP("had14.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had14.D, had14.F, permHad14), ",", permHad14)
print("Random Search: ")
print(had14.random_search(2000))
print("Greedy Algorithm: ")
print(had14.greedy_algorithm())

# count sample for 16 x 16
print("\n16 x 16")
permHad16 = [int(x) for x in "9,4,16,1,7,8,6,14,15,11,12,10,5,3,2,13".split(",")]
had16 = qap.QAP("had16.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had16.D, had16.F, permHad16), ",", permHad16)
print("Random Search: ")
print(had16.random_search(3000))
print("Greedy Algorithm: ")
print(had16.greedy_algorithm())

# count sample for 18 x 18
print("\n18 x 18")
permHad18 = [int(x) for x in "8,15,16,6,7,18,14,11,1,10,12,5,3,13,2,17,9,4".split(",")]
had18 = qap.QAP("had18.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had18.D, had18.F, permHad18), ",", permHad18)
print("Random Search: ")
print(had18.random_search(4000))
print("Greedy Algorithm: ")
print(had18.greedy_algorithm())

# count sample for 20 x 20
print("\n20 x 20")
permHad20 = [int(x) for x in "8,15,16,14,19,6,7,17,1,12,10,11,5,20,2,3,4,9,18,13".split(",")]
had20 = qap.QAP("had20.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had20.D, had20.F, permHad20), ",", permHad20)
print("Random Search: ")
print(had20.random_search(5000))
print("Greedy Algorithm: ")
print(had20.greedy_algorithm())