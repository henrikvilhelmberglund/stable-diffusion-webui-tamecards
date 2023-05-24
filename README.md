# Tamecards

Like wildcards but not as wild.

Allows you to use `___name___` syntax in your prompt to get the first line from a file named `name.txt` in the tamecards directory. The next time you will get the next line.

The index resets after each generation which means if you don't have a batch size greater than 1 this extension will just generate the first line over and over.

This extension is made for running a list of prompts sequentially in batch mode.