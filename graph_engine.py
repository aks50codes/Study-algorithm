'''

Filename: graph_engine.py
Author: Aksh
Date: June 9, 2026

Description: This program initializes a DAG engine to navigate the user's prerequisites for 
workloads using OOP.

'''

class SyllabusEngine:
    def __init__(self):
        self.adjacency_list = {} # initialize a dictionary that contains lists of topics and their subtopics
    
    def add_topic(self, topic_name):
        if topic_name not in self.adjacency_list: # if the topic is not listed in the dictionary, add it
            self.adjacency_list[topic_name] = [] 

    def add_prerequisite(self, parent_topic, child_topic, weight=1.0):

        if parent_topic == child_topic: # check for irreflexivity
            print(" Error: A topic cannot be a prerequisite for itself!") 
            return False

        self.add_topic(parent_topic)
        self.add_topic(child_topic)

        # Loop through every existing tuple with an index tracker
        for index, existing_child in enumerate(self.adjacency_list[parent_topic]):
            # Check if the topic name matches
            if existing_child[0] == child_topic:
                print(f"🔄 Updating weight for connection from {parent_topic} to {child_topic} to {weight}")
                # Overwrite the old tuple at this exact index position
                self.adjacency_list[parent_topic][index] = (child_topic, weight)
                return True
            
        # Append the child topic to the parent's list if it's a new link
        self.adjacency_list[parent_topic].append((child_topic, weight))
        return True

    def get_dependency_weight(self, target_topic):
        total_weight = 0.0
        
        # Outer loop: scan every list of edge tuples across all parents
        for edge_list in self.adjacency_list.values():
            # Inner loop: inspect each individual tuple (child, weight)
            for child, weight in edge_list:
                # If this connection points to our target topic, sum its weight
                if child == target_topic:
                    total_weight += weight
                    
        return total_weight

    def has_cycled(self, 

# This runs only when you execute this file directly
if __name__ == "__main__":
    # create an instance engine of this class
    engine = SyllabusEngine()
    
    print("--- Building a Chemistry Syllabus ---")
    # Add some topics and prerequisite samples
    engine.add_prerequisite("Atomic Structure", "Chemical Bonding", 1.0)
    engine.add_prerequisite("Chemical Bonding", "Thermodynamics", 0.6)
    
    print("\n--- Testing Irreflexivity Guardrail ---")
    # Try to break irreflexivity rule by linking a topic to itself
    engine.add_prerequisite("Organic Chemistry", "Organic Chemistry")

    print("\n--- Testing Dynamic Weight Updating ---")
    # Update an existing prerequisite edge with a new weight coefficient
    engine.add_prerequisite("Chemical Bonding", "Thermodynamics", 0.95)
    
    print("\n--- Current Graph Structure (Adjacency List) ---")
    # Print out raw dictionary to test structural accuracy
    print(engine.adjacency_list)

    print("\n--- Testing Dependency Metrics ---")
    # Calculate inbound weight landing on Thermodynamics
    thermo_weight = engine.get_dependency_weight("Thermodynamics")
    print(f"Total prerequisite dependency weight for 'Thermodynamics': {thermo_weight}")
