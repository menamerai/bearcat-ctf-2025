# Curly Password

> A modern approach to secure passwords is to use passphrases to create easy to remember and long passwords. A user used this techinque however they picked 3 words from our home page to use separated by underscores ("_"). They also thought it would be funny to wrap it in our slug. The flag is the password `eb02e84ccdc45f873c633846efa027b4726a9552a7dad42927ec627e929a500d`

Fairly straightforward, scrape the main site, extract words and permutate them, then construct a flag, hash it and compare until you find the correct combination.