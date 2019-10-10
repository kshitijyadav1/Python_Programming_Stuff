#! python3
# This file is dedicated to the interesting facts of python
'''
1. Python was a hobby project
=> In december 1989, python's creater Guido Van Rossum  was looking for a hobby project to keep him occupied in the week round Christmas. He had been thinking of writing a new scripting language that'd be a descendent of ABC and also appeal to Unix/C hackers. He chose to call it python.
2. Why it was called python
=> The language's name isn't about snakes, but about the popular British comedy troupe Monty Python (from the 1970s). Guido himself is a big fan of Monty Python's Flying Circus. Being in a rather irreverent mood, he named the project 'Python'.
3. The Zen of Python
=> Tim peters, a major contributor to the python community, wrote this poem to highlight the philosphies of python. If you type in "import this" in your python IDLE, you'll find this poem.
4. Flavors of python
=> CPython, JPython, IronPython, Brython, RubyPython, PyPy, MicroPython
5. Big companies using python
=> NASA, Google, Nokia, IBM, Yahoo!Maps, Walt Disney Feature Animation, Facebook, Netflix, Expedia, Reddit, Quora, MIT, Disqus, Hike, Spotify, Udemy, Shutterstock, Uber, Amazon, Mozilla, Dropbox, Pinterest, Youtube
6. No braces
=> Unlike, Java and C++, Python does not use braces to delimit code. Indentation is mandatory with python. If you choose to import it from the __future__ package, it give you a witty error. e.g. (from __future__ import braces)
7. Functions can return multiple values
=> In python, a function can return more than one value. Take a look at  the following code:-
def func():
	return 8, "Brahm" 11
	
roll, name, score = func()
8. Python supports multiple assignment in one statement
=> Ex- a = b = 8
a, b = 8, 9
9. With slicing, it's easier to reverse a list
=> num = [1,2,3,4,5]
print(num[::-1]) #[5,4,3,2,1] 
10. You can chain comparison
=> 1<3<4<5 # True
11. String literals concatenate
=> 'Hello' 'World' '!' # HelloWorld!
12. Antigravity
=> import antigravity
It will open up a webpage with the comic about the antigravity module.
13. Python influenced javascript
=> Python is one of the 9 language that influenced the design of javascript. Others include AWK, C, HyperTalk, Java, Lua, Perl, Scheme, and Self.
14. for-and-while loops can have else statements
=> Take a look- 
for i in range(0,10):
	print("Hello world")
else:
	print("Nothing to say.")
15. _gets the value of the last expression
=> Take a look- 
>>>2*3+5 #11
>>> 7*_ # 77 (here _ it take last expression, means 7 * 11)
16. People prefer python over french
=> According to the recent survey, in the UK in 2015, Python overtook French to be the most popular language.
'''
# Fact No. 3 The zen of python
import this

print('\n'*2)
# Fact No. 12 Antigravity
import antigravity
print("Explore the antigravity")

# python future artifact
