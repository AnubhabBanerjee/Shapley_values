# shapley-values

 This project compares four traditional ways of calculating Shapley values and compare their performances.
 
 Requirements: Python 3
 
 Usage:
 To use this tool, please go to the config.ini file and you will find a very detailed description there on how to use this tool.
 After you set everything in the config.ini file, please go to the main_worker_file.py file and run the file.
 
 One last thing to remember: We assumed a payoff function where the payoff for a subgraph is simply the summation of the node weights if the subgraph is connected. If you want to change the payoff, please look at the get_map_value() function inside traditional_shapley.py file.
 
 
