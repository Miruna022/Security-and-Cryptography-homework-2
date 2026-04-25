# Security-and-Cryptography-homework-2
This assignment requires the application of cryptanalysis to decrypt a file encrypted with a Caesar cipher (unknown shift key)

## Steps
1. Using the code written for the previous assignment, the functions for reading/writing from/to a file, and decrypting a Caesar cipher, were reused.

2. The `signatures` file was used as a dictionary to hold the hex signatures of each given file type. As some of them used the same hex (therefore, had a common parent container), they were placed in the same category, as was done here, for example:
```
DOC/PPT/XLS, D0 CF 11 E0 A1 B1 1A E1
```

3. After loading and splitting the `signatures` file, the `brute_force` function was used to look through the first 20 bytes of the header and shifting with different values (up to 256), and search if there is a match with anything in the dictionary.

4. Upon running the code, I found out that the used shift value was **111 bytes**. In the console it was also printed that the given type is **DOC/PPT/XLS**. The next step was to look for keywords like 'word', 'excel', or 'slide' to find out exactly which of the 3 is the concrete file type. I was having trouble at this part since I couldn't tell why the program couldn't find these words, but the solution was a simple `.lower()` call due to case sensitivity.

5. Finally, the concrete file type was found to be a **Microsoft Excel Workbook (.xls)**.
