# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.


pwd - print working directory<br> 
hostname - my computer's network name<br> 
mkdir - make directory<br>
cd - change directory<br>
ls - list directory<br>
rmdir - remove directory<br>
rm - remove a file or directory (-r is recursive)<br>
pushd - push directory - don't forget '.' for current directory<br>
popd - pop directory<br>
touch - make an empty file<br>
cp - copy a file or directory<br>
mv - move a file or directory<br>
cat - print the whole file, i.e. stream the the whole file to stdout<br>
less - scroll through a file - nicer more because its scrollable like vi<br>
more - scroll through a file line by line<br>
tree - graphically view folder heirarchy (a DOS favorite, install via sudo apt-get install tree)<br>
env - what's in the shell environment<br>
localvarable = value - bash can have local variables as well as environment variables
$ - expand whats is next, i.e. echo $$ shows PID of shell, echo$((3+4)) shows 7<br>
find - find files<br>
xargs - execute arguments:<br>
grep - find things inside files<br>
man  - read a manual page<br>
apropos -  find what man page is appropriate<br>
env - look at your environment<br>
echo - print some arguments<br>
export - export/set a new environment variable<br>
exit - exit the shell<br>
sudo - DANGER! become super user root DANGER!<br>
chmod - change permission modifiers<br>
chown - change ownership<br> 
sed - linux stream editor<br>
Additionally an advance bash-scripting guid is available here:<br>
     [http://tldp.org/LDP/abs/html](http://tldp.org/LDP/abs/html)<br>

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls shows a list of what is in current directory<br>
ls -a shows all the files in the directory, including .
ls -l uses the long listing format <br>

---


---

What does `xargs` do? Give an example of how to use it.

    xargs assists in building command and excuting a command line
    it can typically be used by piping long lists to it
    example: - replace "old" with "young" in text files in dir<br>
    files=$(grep -rl old *.txt) && echo $files | xargs sed -i 's/old/young/g'

---

