import genetic as g
import qap


had12 = qap.QAP("had12.dat")
genetic = g.GeneticAlgorithm(10, had12, 20, 0.1, 0.05)
best = genetic.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)

genetic2 = g.GeneticAlgorithm(100, had12, 100, 0.7, 0.01)
best = genetic2.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)

genetic3 = g.GeneticAlgorithm(1000, had12, 500, 0.5, 0.01)
best = genetic3.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)
print("Fitness as cost couting per second: ", genetic.fitness)

genetic3 = g.GeneticAlgorithm(100, had12, 500, 0.1, 0.05)
print(genetic3)
best = genetic3.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)