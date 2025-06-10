**`argparse`** is a Python module that parses command-line arguments passed to a script, allowing programs to accept user-defined options and values.

It handles how to parse arguments, generates help messages, and reports errors when users give invalid arguments.


## Run the example codes
Open a CLI and Use the `cd` (change directory) command to move into the folder where your Python `.py` file is saved.
```
cd /path_to_your_script/package_argparse
```

Execute the Python Script: use the `python` command followed by the name of your script.

### Simple example
```bash
python argparse_greet.py Lulu

python argparse_greet.py -h
python argparse_greet.py -help

python argparse_greet.py Lulu --polite
python argparse_greet.py Lulu --polite --age 25
```
Output:
```
Greetings, noble Lulu!
Lulu is 25 years old.
```

### Example with nargs and choices
```bash
python complex_args.py -h
python complex_args.py file1.txt file2.txt

python complex_args.py document.pdf --mode write
```

Output:

```
Processing files: ['document.pdf']
Using mode: write
```