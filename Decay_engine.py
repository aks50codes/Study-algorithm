import time
import math

'''
Filename: Decay_engine.py
Author: Aksh P
Date: Aug 6, 2026

Description: 
The forgetting curve is represented by R(t) = e^-(t/s). T represents the time lapsed since the last time a user last reviewed a topic. S is a quantity
representing the memory stability(how strong the memory trace is in your brain), and the function R(t) is a retention score between 0.0 and 1.0 
where 1.0 is 100% remembered. 
'''

class MemoryNode: 
  def __init__(self, topic_name, initial_stability = 1.0): 
    self.topic_name = topic_name
    self.stability = initial_stability
    self.last_reviewed_timestamp = time.time()

  def get_elapsed_days(self):
    current_time = time.time()
    seconds_passed = current_time - self.last_reviewed_timestamp
    days_passed = seconds_passed/86400
    return days_passed

  def calculate_retention(self, t_days=None):
    if t_days == None:
      t_days = self.get_elapsed_days()
    retention = math.exp(-t_days / self.stability)
    return retention

  def calculate_forgetting_rate(self, t_days = None):
    if t_days == None:
      t_days = self.get_elapsed_days()
    retention = self.calculate_retention(t_days)
    rate = -(1.0 / self.stability) * retention
    return rate

  def process_review(self, score, latency_seconds, alpha=0.5, beta=0.1):
        if score == 1:
            # Calculate how fast they answered (closer to 1.0 for fast answers)
            latency_factor = math.exp(-beta * latency_seconds)
            
            # Boost stability based on speed
            growth = 1.0 + (alpha * latency_factor)
            self.stability = self.stability * growth
        else:
            # Cut stability in half if they missed it, model uses half-life formula
            self.stability = max(0.1, self.stability * 0.5)

       
        self.last_reviewed_timestamp = time.time()
class CognitiveDecayEngine:
  def __init__(self):
    self.memory_nodes = {}

  def register_topic(self, topic_name, initial_stability = 1.0):
    if topic_name not in self.memory_nodes:
      self.memory_nodes[topic_name] = MemoryNode(topic_name, initial_stability)
    return self.memory_nodes[topic_name]

  def get_decay_rankings(self, simulated_days_passed = 0.0):
    TRS = [] #Topic retention scores
    for topic_name, node in memory_nodes.items():
      retention_score = node.calculate_retention(simulated_days_passed)
      TRS.append((topic_name, retention_score))
    TRS.sort(key=lambda x: x[1]) # lambda is an inline function that helps sort based on a specific key of the tuple
    return TRS
if __name__ == "__main__":
    node = MemoryNode("Atomic Structure", initial_stability=1.0)
    print(f"Topic: {node.topic_name}")
    print(f"Initial Stability: {node.stability} days")
    print(f"Initial Retention: {node.calculate_retention() * 100:.1f}%")

    print("\n Simulating a Fast Correct Review (2.0 seconds)")
    node.process_review(score=1, latency_seconds=2.0)
    print(f"New Stability: {node.stability:.2f} days")

    print("\n--- Simulating an Incorrect Review (8.0 seconds)")
    node.process_review(score=0, latency_seconds=8.0)
    print(f"Penalized Stability: {node.stability:.2f} days")
