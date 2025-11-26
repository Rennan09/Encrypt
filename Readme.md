# Encrypt
 I created a simple program to encrypt some messages, for now it's only capable of enconding messages, more updates will come soon with the decoding function.
## How it works?
Firstly, it chooses the variability, one random (randint) value between 1 and 20. The variability is only applied to the consonants and will be the distance between the real letter and the coded letter. e.g., if the letter "b" was written with the value 1, in the coded message a "c" will appear instead.<div>
On the vowel process, each vowel (and space) is assigned to a digit, with distinction between lowercases and uppercases, as shown in the table below:


| Input    |     Output      |
|----------|:-------------:|
| a |    1   |
| e |    2   |
| i |    3   |
| o |    4   |
| u |    5   |
| U |    6   |
| O |    7   |
| I |    8   |
| E |    9   |
| A |    1-  |
|   |    0   |

##
## How to know the variability of my text?
The variability is shown at the end of the text, followed by a mandatory 0. <div>
### Example:
Hello World (variability 5)
<div>
n2rr40c4xrk05