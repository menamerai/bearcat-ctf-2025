# Bonkers Flag Innit

> I recently discovered an obscure Windows filename function! So I picked a random word from the dictionary (with British inspirations) as the flag, and ran it through. Here's the output! --> FLD20C~1 <--

Some Google digging reveal that this is Windows 8.3 filename. The [wiki](https://en.wikipedia.org/wiki/8.3_filename) page says that they keep the first two letters and use an "undocumented hash" on the word to obtain the next 4 characters. Digging in the references lead to this [blog post](https://web.archive.org/web/20230825135743/https://tomgalvin.uk/blog/gen/2015/06/09/filenames/) that reimplemented the hashing with a C file attached. Refer to `8dot3checksum.c` in the same foler.

Now, it's just a matter of obtaining a bunch of words that start with "FL" and run the hash on it. I used this [python package](https://pypi.org/project/english-words/) to obtain massive word lists, filter it and save it to a word file. I later also augmented the word file with lowercase and first capitalized forms. It turns out this was necessary because the actual hash came from a lowercase word despite the first two letters of the file being uppercase.