import numpy as np

def moran_process_scores(returns, pop_size=1000, steps=5000):
    """
    Simulate Moran process:
    - Fitness of each ETF = average return over the window (or Sharpe-like?).
    - Initial population uniformly distributed.
    - At each step: one individual reproduces (probability proportional to fitness),
      one individual dies (uniformly random or also proportional? Classic Moran: choose a random individual to die.
      We'll use classic: reproduce proportional to fitness, die uniformly among all.
    - After enough steps, the population converges to a stationary distribution.
    - Score for each ETF = final proportion of the population.
    """
    n = len(returns.columns)
    if n < 2:
        return {ticker: 0.0 for ticker in returns.columns}
    # Calculate fitness: use average return over the window (could also use Sharpe)
    fitness = returns.mean(axis=0).values
    # Ensure positive fitness (add constant if needed)
    min_fit = fitness.min()
    if min_fit <= 0:
        fitness = fitness - min_fit + 0.01
    # Initial population: equal distribution
    population = np.ones(n, dtype=int) * (pop_size // n)
    remainder = pop_size - sum(population)
    population[:remainder] += 1  # adjust for rounding
    # Run simulation
    for _ in range(steps):
        # Probability of reproducing for each type = fitness[i] * population[i] / sum(fitness * population)
        total_fitness = np.sum(fitness * population)
        if total_fitness == 0:
            break
        probs = (fitness * population) / total_fitness
        # Choose one individual to reproduce (type)
        reproducer = np.random.choice(n, p=probs)
        # Choose one individual to die uniformly at random
        die_choice = np.random.randint(pop_size)
        # Find which type that individual belongs to (cumulative distribution)
        cum_pop = np.cumsum(population)
        die_type = np.searchsorted(cum_pop, die_choice + 1)
        # Update population: reproducer gains one, die_type loses one
        population[reproducer] += 1
        population[die_type] -= 1
        # Ensure non-negative (should be fine)
    # Final proportions
    proportions = population / pop_size
    tickers = returns.columns
    return {ticker: float(proportions[i]) for i, ticker in enumerate(tickers)}
