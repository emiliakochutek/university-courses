# Symulacja dryfu genetycznego

# [Dryf genetyczny](https://en.wikipedia.org/wiki/Genetic_drift) to zjawisko polegające na losowej zmianie częstości allelu w populacji. 
# Jest to ważny przykład procesu prowadzącego do ewolucji nieadaptatywnej. 

# Celem tego ćwiczenia jest stworzenie symulacji ilustrującej działanie dryfu genetycznego.

# Niech *A*, *a* będą dwoma allelami (wariantami) jednego genu. Zakładamy, że:
# * Dana jest populacja osobników, w której każdy osobnik ma dwie kopie genu w dowolnych wariantach (czyli są to osobniki diploidalne). 
# * Zmiana jednego allelu na drugi nie ma żadnego znaczenia adaptacyjnego. 
# * W populacji pokolenia nie zachodzą na siebie, kojarzenie jest płciowe i całkowicie losowe a każda para organizmów rodzicielskich ma dwa organizmy potomne. 
# * W organizmie potomnym warianty genu dobierane są losowo, z równym prawdopodobieństwem, po jednym od każdego z organizmów rodzicielskich. 
# Przykład: dla organizmów rodzicielskich o genotypach *aA*, *AA*, mamy cztery możliwe genotypy potomne *aA*, *aA*, *AA*, *AA* 
# odpowiadające wylosowaniu pozycji (1, 1), (1, 2), (2, 1), (2, 2).

# Napisz program, który losowo utworzy populację o ustalonej z góry liczbie osobników (najlepiej parzystej) 
# a następnie wykona dla tej populacji symulację pewnej liczby cykli życiowych.



import random

# Funkcja tworząca losową populację o podanej liczbie osobników
def create_population(size):
    population = []
    for _ in range(size):
        genotype = random.choice(['A', 'a']) + random.choice(['A', 'a'])
        population.append(genotype)
    return population

# Funkcja symulująca dryf genetyczny dla danej populacji przez określoną liczbę cykli życiowych
def genetic_drift_simulation(population, num_cycles):
    for cycle in range(num_cycles):
        new_population = []
        for _ in range(len(population)//2):
            parents = random.sample(population, 2)  # Losowe wybieranie 2 osobników z populacji
            offspring = parents[0][random.randint(0, 1)] + parents[1][random.randint(0, 1)]
            new_population.extend([offspring, offspring])
        population = new_population
    return population

# Parametry symulacji
population_size = 100  # Liczba osobników w populacji (najlepiej parzysta)
num_cycles = 10  # Liczba cykli życiowych do przeprowadzenia

# Tworzenie populacji
population = create_population(population_size)

# Wykonanie symulacji dryfu genetycznego
final_population = genetic_drift_simulation(population, num_cycles)

# Wyświetlenie wyników
print(f"Populacja początkowa: {population}")
print(f"Populacja końcowa po {num_cycles} cyklach: {final_population}")
