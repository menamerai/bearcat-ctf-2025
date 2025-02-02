# What You See

> Inspect, Extract, Reveal

For some reason, this one took me a while to get. It was an image with the text slightly hidden, reads:

> the password is: "ctf"

The solution was straightforward, just use `steghide` with the passphrase as "ctf". Specifically, use the command

```terminal
steghide extract -sf CtfProblem.jpeg
```

Can read more about steghide [here](https://medium.com/the-kickstarter/steganography-on-kali-using-steghide-7dfd3293f3fa).