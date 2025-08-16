To use the Scalable Markov Chains program and to create output texts, please follow these instructions.

The instructions are designed with newcomers to Python and programming in mind.

You need Python 3 installed on your computer to execute the program.

## Preparations

1) __Choose or create a folder__ on your hard drive where you want to store the program. Name it any way you want, e.g., `Markov-Chains`.

2) Either a) __download the program__ from GitHub by loading the file `SMC_Program.py` to the folder created in step 1. Then proceed to step 2. Or b) __create a new file__ within the folder you created in step 1. Save the file under the name `SMC_Program.py`. As always in programming, it is essential to type this name without any deviations or errors. Then you __copy the contents__ of the same-named file `SMC_Program.py` from GitHub into the file you just created and __save the file__ after doing this. To create the file, you can use almost any text editor. My personal choice is the text editor [Sublime](https://www.sublimetext.com/), which you can download and use for free (I am not affiliated with them by any means).

3) __Create the input file__ `input.txt`. This file will contain the text the program uses as training data. Here, again, you can use any text editor of your choosing or the editor _Sublime_ mentioned in step 2. __Create a new file__ in your text editor and __save the file__ under the name `input.txt` to the folder created in step 1. As before, it is crucial to type the exact name without any deviations or errors. Otherwise, the program will not be able to open the input file later on. Please check that the file `SMC_Program.py` from step 2 and the input file you just created __are in the same folder__, the one created in step 1. For now, the input file you created is empty. We are going to change this, now.

4) __Copy some text__ into the input file `input.txt` you have created in step 3. What kind of text that is, is up to you. It is advisable to use long texts as input, e.g., the content of a whole book. You can, of course, start with some short random text like even `asdfasdf`. This is sufficient to test whether the program works in the setting you have created. After copying the text into `input.txt`, __save the file__.

## Executing the Program

5) To execute the program, first __open the console__: a) On Windows Systems, in the search bar at the bottom left, type `PowerShell` and then start PowerShell. b) On Mac OS, press `Command + Space` to open the search bar. Here, type `terminal` and start the terminal.

6) In the console now running, we have to __navigate to the folder__ you have created in step 1. This is the folder where our two files – `SMC_Program.py` from step 2 and `input.txt` from step 3 – are stored. To navigate to this folder, you need to know its location on your hard drive, i.e., the path to the folder. Knowing where the file is stored, we are able to open folder by folder within the console until we are inside the folder you created in step 1. To see the contents of the folder you are currently in, use the command `ls` followed by hitting `Enter`. This might help to determine which folder to open next to eventually reach the folder we want to navigate to. To open a specific folder, type `cd` followed by the name of the folder you want to open. (For example, to open the folder `Documents`, type `cd Documents`. Of course, this arbitrary example only works if the folder you are currently in contains a folder named `Documents`.) Again, use the command `ls` to check the contents of the folder you are currently in. If you have to close a folder and go one level up again, use the command `cd ..`. By using these commands, you should be able to navigate to the folder you created in step 1. If you have reached and opened this folder, type `ls` once again. If the files `SMC_Program.py` and `input.txt` are in this folder, you have done everything right. If they aren’t, check a) if you are in the correct folder in the console, and b) if you have created these files in the correct folder in steps 2 and 3.

7) Having navigated to the correct folder within the console, you are ready to __start the program__. In the console, type `python SMC_Program.py`. Again, every single sign has to be correct to execute the program stored under the name `SMC_Program.py`. Check if you have typed the proper command and hit `Enter`. If everything worked out fine, the console will show some info on the parameters chosen in the program and present to you the result we wanted: Some randomly created output text. But it might also be the case that you encounter an __error__. There are many reasons for this. I will discuss one of the most fundamental ones in the following step 8.

8) If the program has worked, you can proceed to step 9. If it has not, you have to do some __troubleshooting__. One of the most basic issues to check is whether the command `python` that you used when trying to start the program in step 7 is the correct one for your computer. If, on Windows, instead of delivering the desired output, the console responded to you with something like `Python was not found but can be installed from the Microsoft Store:` – or on Mac OS with something like `python: command not found` –, you might have to __use a different command__ to tell the computer to start Python. On Windows, instead of the command from step 7, try just `py SMC_Program.py`. On Mac, try `python3 SMC_Program.py` and thereby tell the Computer which version of Python you want to start. If these commands are not producing the correct outcome either, __copy the error message from the console and search online for a solution__. This kind of troubleshooting is part of learning how to program (and of programming itself), and by no means an indicator of your ability to master it.

### Experimenting with the Program’s Variables

I am not delving into the basic concepts of Markov chains here. For this, compare the texts referenced in the `README.md` file. After that, you can study the code of the program and the comments to get an understanding of what is happening here.

Still, experimenting with some parameters is also a good thing to grasp the functionality of the program. You run the program with varying input texts and different lengths of the group of symbols the Markov chain should look at to determine how likely it is for another symbol to follow after them, and see how the quality of the output changes.

9) 
