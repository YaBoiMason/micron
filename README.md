# micron
A tiny, portable scripting language.

# What is it for?
Anywhere where you need the ability to give users access to scripting. For example, a macro in an office application or 
mod support for a game.

# What can it do?
As of release 1, not much. There is a set of built-in functions:
TODO: ADD LIST

# Example
An example program is in Example.mi

# Language info
Here's a rundown of the language if you don't want to read the program:
let - set a variable. Variables do not have types, and are global.
Example:
  let a 50
  ; defines a to 50

set - sets the content of a variable after it is defined
Example:
  let a 50
  ; defines a to 50
  set a 75
  ; sets a to 75