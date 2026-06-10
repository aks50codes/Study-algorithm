'''

Filename: graph_engine.py
Author: Aksh
Date: June 9, 2026

Description: This program initializes a DAG engine to navigate the users prerequisites for 
workloads using OOP

'''

class SyllabusEngine:
    def __init__(self):
        self.adjacency_list = {} # initialize a dictionary that contains lists of topics and their subtopics
    
    def add_topic(self, topic_name):
        if topic_name not in self.adjacency_list: # if the topic is not listed in the dictionary, add it
            self.adjacency_list[topic_name] = [] 

    def add_prerequisite(self, parent_topic, child_topic, weight = 1.0):

        if parent_topic == child_topic: # check for irreflexivity
            print(" Error: A topic cannot be a prerequisite for itself!") 
            return False

        self.add_topic(parent_topic)
        self.add_topic(child_topic)
        # Loop through every existing tuple with an index tracker
        for index, existing_child in enumerate(self.adjacency_list[parent_topic]):
            # Check if the topic name matches
            if existing_child[0] == child_topic:
                print(f"Updating weight for connection from {parent_topic} to {child_topic} to {weight}")
                # Overwrite the old tuple at this exact index position
                self.adjacency_list[parent_topic][index] = (child_topic, weight)
                return True
            
        # Append the child topic to the parent's list
        self.adjacency_list[parent_topic].append((child_topic, weight))  # connect the parent and child topics into one list

       # Loop through every existing tuple pair in the parent's list
        
        return True

def get_dependancy_weight():
    total_weight = 0.0
    
# This runs only when you execute this file directly
if __name__ == "__main__":
    # create an instance engine of this class
    engine = SyllabusEngine()
    
    print("--- Building a Chemistry Syllabus ---")
    #Add some topics and prerequisite samples
    engine.add_prerequisite("Atomic Structure", "Chemical Bonding", 1.0)
    engine.add_prerequisite("Chemical Bonding", "Thermodynamics", 0.6)
    
    print("\n--- Testing Irreflexivity Guardrail ---")
    #Try to break irreflexivity rule by linking a topic to itself
    engine.add_prerequisite("Organic Chemistry", "Organic Chemistry")
    
    print("\n--- Current Graph Structure (Adjacency List) ---")
    #Print out raw dictionary to test
    print(engine.adjacency_list)
