# Study-algorithm

This project is an ASRE (Algorithmic Spaced Repetition Engine) that is intended to make studying material more efficient and replace traditional flashcards with 
a mathematically superior engine that uses calculus-driven decay modeling, graph theory prerequisite mapping, and dynamic programming optimization. Unlike standard 
repetition software, an ASRE treats knowledge retention as a continuous state system. 

# Mathematics behind the ASRE

1. Retention R(t) for any given topic is modeled as an exponential decay curve governed by the differential equation of memory stability S: 

$$
R(t) = e^{-\frac{t}{S}}
$$

**Where:**
* $t$: Elapsed time in days since last review.
* $S$: Memory stability index (measured in days until retention drops to $1/e \approx 36.8\%$).
* $R(t)$: Instantaneous retention probability $R(t) \in (0.0, 1.0]$.
