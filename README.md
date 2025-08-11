# Scalable Markov Chains

Uses _Python 3_
Comments in _German_

The program _Scalable Markov Chains_ was created while teaching the seminar »Programming in Python as AI Critique« in 2025 at the University Regensburg. It analyzes arbitrary input text and stores the probabilities for symbols to follow after a specific group of other symbols. The length of this group of symbols is scalable by the user. The program then creates new text randomly by using these probabilities.

The program was developed to study the output of simple discrete-time Markov Chains for different depths of analysis, i.e., lengths of groups of symbols, inspired by Claude E. Shannon’s work on the matter and Friedrich A. Kittler’s reference to it. The design of the program followed the didactic idea to be easily accessible and understandable for newcomers to _Python_. For instance, the program does not use numerical values to store the probabilities of symbols following each other. Instead, all combinations of symbols up to the chosen length are stored in a dictionary and together represent these probabilities without the need for counting them and thereby adding another level of abstraction to the program’s structure.
