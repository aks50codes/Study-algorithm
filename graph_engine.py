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
        if topic_name not in self.adjacency_list:
            self.adjacency_list[topic_name] = []

    def add_prerequisite(self, parent_topic, child_topic):

        if parent_topic == child_topic:
            print(" Error: A topic cannot be a prerequisite for itself!")
            return False

        self.add_topic(parent_topic)
        self.add_topic(child_topic)

        # Append the child topic to the parent's list
        self.adjacency_list[parent_topic].append(child_topic)

        return True

if __name__ == "__main__":
    # 1. Instantiate your engine object 
    engine = SyllabusEngine()
    
    print(" Building a Chemistry Syllabus ")
    engine.add_prerequisite("Atomic Structure", "Chemical Bonding")
    engine.add_prerequisite("Chemical Bonding", "Thermodynamics")
  
    # test irreflexivity
    engine.add_prerequisite("Organic Chemistry", "Organic Chemistry")
    
    print("\nCurrent Graph Structure (Adjacency List)")
    print(engine.adjacency_list)
