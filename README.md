# Scalable Markov Chains

- _Python 3_
- commentary in German
- instructions on how to use the program in English in the `Instructions.md` file

The program _Scalable Markov Chains_ was created while teaching the seminar »Programming in Python as AI Critique« in 2025 at the University of Regensburg. It analyzes arbitrary input text and stores the probabilities for symbols to follow after a specific group of other symbols. The length of this group of symbols is scalable by the user. The program then creates new text randomly by using these probabilities.

Inspired by Claude E. Shannon’s [[1]](#_ftn1) work on the matter and Friedrich A. Kittler’s [[2]](#_ftn2) reference to it, the program was developed to study the output of simple discrete-time Markov chains for different depths of analysis, i.e., lengths of groups of symbols. How would the quality of the output text of the program change in response to different input texts and changes in the length of the n-grams of symbols? The program renders it possible to answer this question in a hands-on fashion.

The design of the program followed the didactic idea to be easily accessible and understandable for newcomers to _Python_. For instance, the program does not use numerical values to store the probabilities of symbols following each other. Instead, all combinations of symbols up to the chosen length are stored in a dictionary and together represent these probabilities without the need to add another level of abstraction to the program’s structure.

For instructions on how to use the program, see the `Instructions.md` file.

To understand what these simple Markov chains are about from the perspective of Media Studies, a suitable starting point is the aforementioned texts of Shannon [[3]](#_ftn3) and Kittler [[4]](#_ftn4).

[[1]](#_ftnref1) Shannon, Claude E. (2000): _Ein/Aus. Ausgewählte Schriften zur Kommunikation- und Nachrichtentheorie_. Berlin: Brinkmann und Bose.

[[2]](#_ftnref2) Kittler, Friedrich A. (1993): ‚Die Welt des Symbolischen - eine Welt der Maschine‘. In: _Draculas Vermächtnis. Technische Schriften_. 1. Auflage. Leipzig: Reclam, S. 58–80.

[[3]](#_ftnref3) You might, e.g., compare the output created by your program with the historical results from Shannon as seen in Shannon (2000): _Ein/Aus_, p. 20.

[[4]](#_ftnref4) Kittler (1993): ‚Die Welt des Symbolischen - eine Welt der Maschine‘, p. 73.
