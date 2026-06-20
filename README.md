# Voltascript
Voltascript was created as a prototype, the real version will be made in C++ instead of Python for performance reasons.
This project **may not** receive future updates, although the C++ version is guaranteed to get further updates and be worked on.<br>
Not all functionality has been added yet, such as:
- Functions
- While loops
- For loops<br>

and more...<br>

Do **NOT** forget, this was already made in Python(an already slow language) and it has zero optimization, do not expect anything out of this that is fast.

Voltascript was created for our upcoming project, SCGE, and details about SCGE won't be made public.
Voltascript will be an open source project.

## Credits
This was created by CommandBeat(aka me) and Jezz.<br>
### Creators
- [CommandBeat](https://github.com/CommandBeat)
- Jezz

# Voltascript Syntax
The syntax for this and the C++ version will be the same<br>

## Numbers
In Voltascript, by default, numbers are floats(decimals). This is purely for ease of use and practicality.<br>

Yes, we hear you screaming "WHAT ABOUT MEMORY USAGE?!" and we have thought of a solution.<br>

Example:
```
// main.vs
log(10) // 10.0
log(~10) // 10
```

This prints 10.0 and 10

## Variable Declaration
You define a variable like this:<br>
*var variable_name = value*<br>

Example:
``var i = 0``<br>
This creates a variable named 'i' with a value of 0

## Function Call and Definition
You define a function like this:<br>
*func function_name() {...}*

Example:
```
func sayHi() {
    log("Hi!") // Output: Hi!
}
```
This creates a function that, when run, prints "Hi!"

## For and while loops
### For loops
You define a for loop like this:<br>
*for x in y {...}*

Example:
```
for i in range(1, 10) {
    log(i) // Output: 1.0, 2.0, 3.0... 10.0
}
```
This prints 1 → 10<br>

### While loops
You define a while loop like this:<br>
*while condition {...}*

Example:
```
x = 10 // Starting value
while x > 5 {
    print(x) // Output: 10.0, 9.0, 8.0, 7.0, 6.0
    x = x - 1 // Make sure to include this
}
```
This prints every number below x and higher than 5

# Libraries

## Built-in Libraries
Voltascript, like other programming languages, contains libraries by default<br>

### Random
Random is a library that creates pseudorandom values<br>
You can use Random like this:
```
import random // Get random library

log(random.randint(1, 100)) // Generate a random number between 1 and 100
```
This generates a random value between 1 and 100

### Math
Math is a library containing math functions and variables, such as pi or square root. You can use Math like this:
```
import math // Get math library

log(math.pi) // Output: 3.141...
```
Math also contains mathematical functions such as the square root or cube
```
import math // Get math library

log(math.sqrt(9)) // Output: 3.0
```

## Importing libraries and local files
### Built-in Libraries: Importing
To import a built-in library, you use this:<br>
*import library_name*

Example:
```
import math // This loads the math library

// Now you can use math functions and variables
log(math.pi) // Output: 3.141...
```
This imports the math library and prints math.pi

You can also use the "as" keyword to shorten library names
Example:
```
import module as m // module is now m

m.sayHi() // Output: Hi!
```

## Making custom libraries
To make a custom library, go to [A Guide To Libraries](libraries/guide-to-libraries.md)

Example:
```
// voltascript/library/doCoolStuff.vs
func coolStuff() {
    log("Doing something") // whatever you want
}
```
```
// main.vs
import doCoolStuff as dcs // import the library

dcs.coolStuff() // Output: Doing something
```

### Local files
To import a local file, you need to specify the file path:<br>
*import file_path*

Example:
```
// module.vs
func sayHi() {
    log("Hi!")
}
```
```
// main.vs
import module // Get local file

module.sayHi() // Output: Hi!
```

This imports a function from a local file and runs it.<br>
### <span style="color:red">WARNING:</span>
#### <span style="color:red">LOCAL FILES HAVE PRIORITY OVER GLOBAL LIBRARIES!</span><br>

#### <span style="color:red">DO **NOT** NAME LOCAL FILES AFTER **ANY** GLOBAL LIBRARIES.</span><br>

#### Example: naming your file math, random or any other of the default libraries.

## Run Voltascript
To test if Voltascript works, run:
```
python -m runtime.shell test.vs
```
