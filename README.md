# Scalable Markov Chains

- _Python 3_
- commentary in German

For instructions on how to use the program, go to the `Instructions.md` file.

The program _Scalable Markov Chains_ was created while teaching the seminar _Programming in Python as AI Critique_ at the University of Regensburg in 2025. It analyzes arbitrary input text and stores the probabilities for symbols to follow after a specific group of other symbols. The length of this group of symbols is scalable by the user. The program then creates new text randomly by using these probabilities.

For example, the program goes through the input text and collects all symbols following the letter `e`. It does this for every letter or symbol in the input text, until it has information about any instance of a symbol following another in the text. This information then represents the probability of any specific symbol in the input text to follow another one. There might have been many instances of the letter `n` following the letter `e`. Therefore, when the program later on creates new output text, it would put the letter `n` with a higher probability than, e.g., the letter `q`. In this way, the program creates output text with similar _transition probabilities_ between symbols as in the input text. This simple method of analyzing and then using the probabilities within the input text enables the program to create language-like output text.

The length of the group of symbols that the program looks at to collect all symbols following this group in the input text is scalable. This means, depending on the parameters set in the code, the program does not only look at a single letter like `e` and collects all symbols following. It also looks at groups of two symbols, like `er`, and collects all symbols following such 

To understand what these simple Markov chains are about from the perspective of Media Studies, a suitable starting point is the texts of Claude E. Shannon [[1]](#_ftn1) and Friedrich A. Kittler [[2]](#_ftn2). Taking up on this work, the program was developed to study the output of simple discrete-time Markov chains for different depths of analysis, i.e., lengths of groups of symbols. How would the quality of the output text of the program change in response to different input texts and changes in the length of the n-grams of symbols? What can this process tell us about the functionalities and limitations of contemporary forms of LLMs? The program renders it possible to explore such questions in a hands-on fashion.

As it is intended for didactic purposes and newcomers to _Python_, the program is easily accessible and understandable. For instance, the program does not use numerical values to store the probabilities of symbols following each other. Instead, all combinations of symbols up to the chosen length are stored in a dictionary and together represent these probabilities without the need to add another level of abstraction to the program’s structure.

For a deeper understanding of the subject matter, see the `Instructions.md` file and read the commentary in the program in the `SMC_Program.py` file (albeit in German).

## References

[[1]](#_ftnref1) Shannon, Claude E. (2000): _Ein/Aus. Ausgewählte Schriften zur Kommunikation- und Nachrichtentheorie_. Edited by Kittler, Friedrich A./Berz, Peter/Hauptmann, David/Roch, Axel. Berlin: Brinkmann und Bose, p. 20.

[[2]](#_ftnref2) Kittler, Friedrich A. (1993): ‚Die Welt des Symbolischen - eine Welt der Maschine‘. In: _Draculas Vermächtnis. Technische Schriften_. 1. Auflage. Leipzig: Reclam, S. 58–80, here: p. 73
