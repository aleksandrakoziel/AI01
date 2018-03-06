import genetic as g
import qap


had12 = qap.QAP("had12.dat")

genetic = g.GeneticAlgorithm(10, had12, 20, 0.1, 0.05, "roulette")
print(genetic)
best = genetic.performGeneticAlgorithm()
print("Best: ", best.permutation, best.cost)
print("Fitness as cost couting per second: ", genetic.fitness)

genetic2 = g.GeneticAlgorithm(100, had12, 100, 0.7, 0.01, "roulette")
print(genetic2)
best = genetic2.performGeneticAlgorithm()
print("Best: ", best.permutation, best.cost)
print("Fitness as cost couting per second: ", genetic2.fitness)

genetic3 = g.GeneticAlgorithm(1000, had12, 500, 0.5, 0.01, "roulette")
print(genetic3)
best = genetic3.performGeneticAlgorithm()
print("Best: ", best.permutation, best.cost)
print("Fitness as cost couting per second: ", genetic3.fitness)

genetic4 = g.GeneticAlgorithm(100, had12, 500, 0.5, 0.05, "roulette")
print(genetic4)
best = genetic4.performGeneticAlgorithm()
print("Best: ", best.permutation, best.cost)
print("Fitness as cost couting per second: ", genetic4.fitness)