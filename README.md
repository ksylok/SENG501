# SENG501

## Directory Layout
```
Assignment1\            --> contains three MapReduce programs for wordcount-type problems
  digram_map.py             --> program that produces unique two-word sequences
  digram_red.py
  index_map.py              --> program that maps words to file the words were found
  index_reducer.py
  sample.py                 --> samples dataset, randomly selects 10% of lines
  sort_mapper.py            --> program sorts words from dataset, using partitioners and multiple reducers
  sort_reducer.py
Assignment2\            --> contains more complex MapReduce problems
  graph.sh                  --> Script to automate entire graph traversal
  graph.txt                 --> Input graph
  graph_map.py              --> Parallel breadth first search MapReduce program, processes one level of nodes at a time
  graph_red.py
  normal_map.py             --> program to normalize a co-occurence word matrix using MapReduce
  normal_red.py
  transpose.py              --> program to transpose a matrix using MapReduce
  transpose_red.py          
wordcount\              --> basic wordcount using MapReduce
  mapper.py
  reducer.py
Spark_Projects\         --> Apache Spark projects
  SENG501_Spark_Project1.py      --> parses dataset into useful information using Spark RDDs
  SENG501_Spark_Project_2.py     --> performs logistic regression on dataset
  SENG501_Spark_Project_2.ipynb  --> Pyspark notebook version
  
```