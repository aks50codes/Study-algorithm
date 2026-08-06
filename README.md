# Study-algorithm

This project is an ASRE (Algorithmic Spaced Repetition Engine) that is intended to make studying material more efficient and replace traditional flashcards with 
a mathematically superior engine that uses calculus-driven decay modeling, graph theory prerequisite mapping, and dynamic programming optimization. Unlike standard 
repetition software, an ASRE treats knowledge retention as a continuous state system. 

# Mathematics behind the ASRE

1. Retention R(t) for any given topic is modeled as an exponential decay curve driven by the differential equation of memory stability S: 

$$
R(t) = e^{-\frac{t}{S}}
$$

**Where:**
* $t$: Elapsed time in days since last review.
* $S$: Memory stability index (measured in days until retention drops to $1/e \approx 36.8\%$).
* $R(t)$: Instantaneous retention probability $R(t) \in (0.0, 1.0]$.

2. Instantaneous forgetting rate

The rate at which memory decays at any exact moment is the first derivative of retention with respect to time $\frac{dR}{dt}$:

$$\frac{dR}{dt} = -\frac{1}{S} \cdot e^{-\frac{t}{S}}$$

Where: $\frac{dR}{dt}$ : The instantaneous rate of memory loss (how fast you are actively forgetting right now).
Notice that as stability $S$ increases, the decay rate drops closer to zero, meaning memory loss slows down significantly.
