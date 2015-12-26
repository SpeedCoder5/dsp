## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 7 different degrees with frequenices:<br/>
0 : 1 <br/>
ScD : 5 <br/>
JD MA MPH MS PhD : 1 <br/>
PhD : 27 <br/>
BSEd MS PhD : 1 <br/>
MD MPH PhD : 1 <br/>
PhD ScD : 1 <br/>


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> There are 4 different titles with frequenices:<br/>
Assistant Professor of Biostatistics : 11 <br/>
Professor of Biostatistics : 13 <br/>
Assistant Professor is Biostatistics : 1 <br/>
Associate Professor of Biostatistics : 12 <br/>


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> Email addreses are:<br/>
bellamys@mail.med.upenn.edu <br/>
warren@upenn.edu <br/>
bryanma@upenn.edu <br/>
jinboche@upenn.edu <br/>
sellenbe@upenn.edu <br/>
jellenbe@mail.med.upenn.edu <br/>
ruifeng@upenn.edu <br/>
bcfrench@mail.med.upenn.edu <br/>
pgimotty@upenn.edu <br/>
wguo@mail.med.upenn.edu <br/>
hsu9@mail.med.upenn.edu <br/>
rhubb@mail.med.upenn.edu <br/>
whwang@mail.med.upenn.edu <br/>
mjoffe@mail.med.upenn.edu <br/>
jrlandis@mail.med.upenn.edu <br/>
liy3@email.chop.edu <br/>
mingyao@mail.med.upenn.edu <br/>
hongzhe@upenn.edu <br/>
rlocalio@upenn.edu <br/>
nanditam@mail.med.upenn.edu <br/>
knashawn@mail.med.upenn.edu <br/>
propert@mail.med.upenn.edu <br/>
mputt@mail.med.upenn.edu <br/>
sratclif@upenn.edu <br/>
michross@upenn.edu <br/>
jaroy@mail.med.upenn.edu <br/>
msammel@cceb.med.upenn.edu <br/>
shawp@upenn.edu <br/>
rshi@mail.med.upenn.edu <br/>
hshou@mail.med.upenn.edu <br/>
jshults@mail.med.upenn.edu <br/>
alisaste@mail.med.upenn.edu <br/>
atroxel@mail.med.upenn.edu <br/>
rxiao@mail.med.upenn.edu <br/>
sxie@mail.med.upenn.edu <br/>
dxie@upenn.edu <br/>
weiyang@mail.med.upenn.edu <br/>


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> There are 4 different email domains:<br/>
email.chop.edu <br/>
upenn.edu <br/>
cceb.med.upenn.edu <br/>
mail.med.upenn.edu <br/>

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> REPLACE THIS WITH YOUR RESPONSE

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>> REPLACE THIS WITH YOUR RESPONSE

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

