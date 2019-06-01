import random

from math import ceil
from numpy import mean, median

from EvolvingNet import EvolvingNet


class EvolutionSpeciationDriver:
    def __init__(self, population_size, survivor_ratio, simlulation, generation_size, mutability=0.5,
                 evolving_class=EvolvingNet):
        self.InDem = simlulation.InDem
        self.OutDem = simlulation.OutDem
        self.PopulationSize = population_size
        self.Mutability = mutability
        self.SurvivorRatio = survivor_ratio
        self.Simulation = simlulation
        self.EvolvingClass = evolving_class
        self.GenerationSize = generation_size
        self.Median = 0.0
        self.Average = 0.0
        self.Maximum = 0.0
        self.Minimum = 0.0
        self.Species = []

        self.Population = []
        for i in range(self.PopulationSize):
            self.Population.append(self.EvolvingClass(self.InDem, self.OutDem, 1, mutability=mutability))

    def run(self):
        self.Simulation.restart()
        Fitness = self.Simulation.run_generations(self.Population, self.GenerationSize)
        self.Average = mean(Fitness)
        self.Median = median(Fitness)
        self.Maximum = max(Fitness)
        self.Minimum = min(Fitness)
        self.repopulate(Fitness)

    def draw(self, screen, row_size, row_count, x, y, width, height, dot_size=10):
        for i in range(row_count * row_size):
            self.Population[i].draw(screen,
                                    x + (i % row_size) * (width // row_size),
                                    y + (i // row_size) * (height // row_count),
                                    width // row_size,
                                    height // row_count,
                                    dot_size)

    def run_visual(self, screen, row_size, row_count, x, y, width, height, dot_size=10):
        self.Simulation.restart()
        Fitness = self.Simulation.run_generations_visual(self.Population, self.GenerationSize, self, screen, row_size,
                                                       row_count, x, y, width, height, dot_size)
        self.Average = mean(Fitness)
        self.Median = median(Fitness)
        self.Maximum = max(Fitness)
        self.Minimum = min(Fitness)
        self.repopulate(Fitness)

    def draw(self, screen, row_size, row_count, x, y, width, height, dot_size=10):
        for i in range(row_count * row_size):
            self.Population[i].draw(screen,
                                    x + (i % row_size) * (width // row_size),
                                    y + (i // row_size) * (height // row_count),
                                    width // row_size,
                                    height // row_count,
                                    dot_size)

    def repopulate(self, Fitness):
        for i in range(len(Fitness)):
            self.Population[i].Score = Fitness[i]
        print(sum(self.Population))
        population_total = sum(self.Population)
        species_ratio = []
        for specie in self.Species:
            species_ratio.append(sum(specie)/population_total)