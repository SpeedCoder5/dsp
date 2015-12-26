# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

    >> Both lists and tuples are zero-based-indexed sequences of items.
    Items in both can be accessed via indexing, slicing, and checking for membership.
     
    A tuple is a immutable sequence -- whereas items in and the sequence of a list are mutable.
    An inline explicit initializer of a list is bracketed by square brackets [], i.e.
    
        lst = ['a', 'b']
    
    An inline explicit initializer of a tuple is bracketed by parenthesis (), i.e.
    
        tup = ('a', 'b')
        
    A tuple can work as a key in a dictionary.  Dictionary keys are immutable.
    
    There are also other types of collections in Python.
    
    Strings are immutable. Literals are initialized bracketed with ' or ".
    
        str = 'ab'
        str = "ab"
    
    A set is a collection of unique items.  Literals are are bracketed by {}.
    
        set = {'a', 'b'}
        
    A dictionary is a collection of pairs each with a unique key.  ':' is added to set literal notation.
    
        dict = {'a':'A', 'b':'B'}

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>Both list and set in Python can be iterated.<br/>
A list is a sequence and a set is  a class in which each contained item is unique.<br/>
The follwing code show set containment and iteration operations benchmark faster than list operations. 

Example:

    # store Python executable setup statements in strings for timeit testing
    make_lst = """\
    lst = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g',
    'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l',
    'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']
    """
    set_from_lst = "st = set(lst)"
    make_st = make_lst + '\n' + set_from_lst
    lst15_from_lst = "lst15 = lst[:15]"
    make_lst15 = make_lst + '\n' + lst15_from_lst
    
    # as a pre-check locally execute the setup statments and show the results
    exec make_st
    exec make_lst15
    
    print "lst contains %d chars" % len(lst)
    print "lst: %r" % lst
    print "st contains %d chars" % len(st)
    print "st: %r" % st
    print "lst15 contains %d chars" % len(lst15)
    print "lst15: %r" % lst15
    
    # benchmark simple timings for containment and iteration for list and set
    lst_contains = "'o' in lst"
    st_contains = "'o' in st"
    lst15_iter = 'for i in lst : i'
    st_iter = 'for i in st : i'
    
    import timeit
    print "%s takes %f sec" % (lst_contains, timeit.timeit(lst_contains, make_lst, timeit.default_timer, 10000))
    print "%s takes %f sec" % (st_contains, timeit.timeit(st_contains, make_st, timeit.default_timer, 10000))
    print "%s takes %f sec" % (lst15_iter, timeit.timeit(lst15_iter, make_lst, timeit.default_timer, 10000))
    print "%s takes %f sec" % (st_iter, timeit.timeit(st_iter, make_st, timeit.default_timer, 10000))
   
 Following is the output:
 
    lst contains 34 chars
    lst: ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']
    st contains 15 chars
    st: set(['a', 'c', 'e', 'd', 'g', 'f', 'i', 'l', 'o', 'p', 's', 'r', 'u', 't', 'x'])
    lst15 contains 15 chars
    lst15: ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l']
    'o' in lst takes 0.021795 sec
    'o' in st takes 0.008727 sec
    for i in lst : i takes 0.062827 sec
    for i in st : i takes 0.013510 sec

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A  *lambda* expression is an anonymous function that can be defined locally and passed to or returned from a function.<br/>
Lambda expressions are tools that aid conciseness in *functional programming*.<br/>
<br/>
Functional programming is a declarative programming model that favors mathematical transformation of arguments to results.<br/>
It differs from imperative programming which favors state change based on commands in the source language.<br/>
It is useful for recursion, flexibility, and scalability.

Example:

    lst = "SuperCaliFragiListicExpiAliDocioius"
    st = set(lst)
    ord_set_capsfirst = sorted(st, key=lambda i:(i))
    ord_set_byletter = sorted(st, key=lambda i:(i.upper()))
    print lst
    print st
    print ord_set_capsfirst
    print ord_set_byletter

Output:

    SuperCaliFragiListicExpiAliDocioius
    set(['a', 'A', 'C', 'e', 'D', 'g', 'F', 'i', 's', 'c', 'l', 'o', 'L', 'p', 'S', 'r', 'u', 't', 'x', 'E'])
    ['A', 'C', 'D', 'E', 'F', 'L', 'S', 'a', 'c', 'e', 'g', 'i', 'l', 'o', 'p', 'r', 's', 't', 'u', 'x']
    ['a', 'A', 'C', 'c', 'D', 'e', 'E', 'F', 'g', 'i', 'l', 'L', 'o', 'p', 'r', 's', 'S', 't', 'u', 'x']

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a simple syntax for creating lists.
 
Code:

    # data for answering Q4
    lst = "SuperCaliFragiListicExpiAliDocioius"
    ord_set = sorted(set(lst), key=lambda i: (i.upper()))
    
    # filter allows using a lambda to select contents from a sequence
    lowers = filter(lambda x: x.lower() == x, ord_set)
    uppers = filter(lambda x: x.upper() == x, ord_set)
    
    # map transforms each element in a sequence
    letters = set(map(lambda x: x.lower(), ord_set))
    
    # list comprehensions provide syntactic sugar wrapping lambdas for creating lists in a natural way
    LETTERS = set([x.upper() for x in ord_set])
    
    # set comprehension can be used to create a set
    upperAndLowers = {x for x in lowers for y in uppers if x.upper() == y}
    
    # a dictionary comprehension can be used to create a dictionary
    uppersByLowers = {x:y for x in lowers for y in uppers if x.upper() == y}


Output:

    lst: SuperCaliFragiListicExpiAliDocioius
    ord_set: ['a', 'A', 'C', 'c', 'D', 'e', 'E', 'F', 'g', 'i', 'l', 'L', 'o', 'p', 'r', 's', 'S', 't', 'u', 'x']
    lowers: ['a', 'c', 'e', 'g', 'i', 'l', 'o', 'p', 'r', 's', 't', 'u', 'x']
    uppers: ['A', 'C', 'D', 'E', 'F', 'L', 'S']
    letters: set(['a', 'c', 'e', 'd', 'g', 'f', 'i', 'l', 'o', 'p', 's', 'r', 'u', 't', 'x'])
    LETTERS: set(['A', 'C', 'E', 'D', 'G', 'F', 'I', 'L', 'O', 'P', 'S', 'R', 'U', 'T', 'X'])
    upperAndLowers: set(['a', 's', 'c', 'e', 'l'])
    uppersByLowers: {'a': 'A', 's': 'S', 'c': 'C', 'e': 'E', 'l': 'L'}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





