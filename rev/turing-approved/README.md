# Turing Approved

> I wrote a flag verification program for this challenge so when you find the flag, you can confirm it's correct! Aren't I just the kindest?

Big bf file that verify an input flag. This means that the program MUST build up some sort of representation in the tape to then compare with the result later. This could be done in one big batch where the whole flag is written down, then compared in one go, or one character by one. I used [this bf debugger](https://dagans.dev/projects/BrainfuckDebugger/) to find out.

It turns out that the program is doing the former, which is tremendous for us. Specifically, this program is writing ASCII numbers into each memory slot incrementally with a step of 2 NULL slots (0 -> 3 -> 6, ....). Writing down those numbers and translating them to ASCII give us some letters that looks like the flag in reverse.