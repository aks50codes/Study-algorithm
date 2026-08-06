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

**Where:** 

$\frac{dR}{dt}$ : The instantaneous rate of memory loss (how fast you are actively forgetting right now).

Notice that as stability $S$ increases, the decay rate drops closer to zero, meaning memory loss slows down significantly.

3. Implicit Speed Latency FactorTo eliminate user self-reporting bias (e.g., "Easy / Medium / Hard" buttons), stability growth during correct reviews is weighted exponentially by response latency $L$ (measured in seconds):

$$S_{\text{new}} = S_{\text{old}} \cdot \left(1.0 + \alpha \cdot e^{-\beta \cdot L}\right)$$

**Where:** 

$\alpha$: Maximum stability scaling boost factor (default $= 0.5$).
$\beta$: Latency decay constant penalizing slow recall (default $= 0.1$).
$L$: User response latency in seconds.


# Architecture & Modules:

The system is split into three core algorithmic engines:

Engine 1: Calculus Decay Engine (decay_engine.py)(completed)
The main math engine behind the project. Tracks individual topic memory stability, nodes, and ranks topics by instantaneous retention score.

Engine 2: DAG Prerequisite Engine (graph_engine.py)(in progress)
Represents syllabi as Directed Acyclic Graphs (DAGs) using adjacency lists.Detects illegal circular dependencies via cycle detection.Performs Topological Sorting (Kahn's Algorithm) to enforce learning prerequisites.

Represents material/syllabi as DAGs using adjacency lists. Also detects circular dependencies via cycle detection to prevent logical fallacies. Uses topological sorting(Kahns algorithm) to enforce learning prerequisites. Enforces smart study sequencing.

Engine 3: Knapsack Scheduler (knapsack_engine.py)(upcoming)
Formulates daily study session planning as a Bounded Dynamic Programming Knapsack Problem. Maximizes global retention gains under strict user-defined daily time limits.
