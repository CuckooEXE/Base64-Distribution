# Base64 Distribution

Little project I was working on to determine the distribution of uppercase, lowercase, and numerical characters in Base64. I was talking to a coworker trying to figure out how to detect exfiltration attempts in DNS logs, when this idea occured to me. I figured since Base64 regex is pretty bad (considering it's just plain-text), I wanted a better way to figure out how to determine Base64 from plain-text, without having to muck around in AI/ML/NN. The results are below, but the short of it is, the distribution in Base64 encoded text, typically lies in around 46% uppercase, 44% lowercase, and 10% digits.

Huge thanks to the [Guttenburg Project](https://www.gutenberg.org/) for the corpus of text used! Check them out!

# Distributions

The output of the script is:

```
Moby Dick Plain Text:
	Uppercase: 23966 - 1.88%
	Lowercase: 954353 - 74.78%
	Digits: 1129 - 0.09%
	Other: 296753 - 23.25%
Moby Dick B64 Encoded:
	Uppercase: 792513 - 45.73%
	Lowercase: 761382 - 43.94%
	Digits: 178455 - 10.30%
	Other: 534 - 0.03%


Pride and Prejudice Plain Text:
	Uppercase: 14260 - 1.78%
	Lowercase: 542679 - 67.86%
	Digits: 418 - 0.05%
	Other: 242381 - 30.31%
Pride and Prejudice B64 Encoded:
	Uppercase: 523466 - 48.24%
	Lowercase: 457198 - 42.13%
	Digits: 104211 - 9.60%
	Other: 257 - 0.02%


Frankenstein Plain Text:
	Uppercase: 8011 - 1.78%
	Lowercase: 341022 - 75.65%
	Digits: 306 - 0.07%
	Other: 101444 - 22.50%
Frankenstein B64 Encoded:
	Uppercase: 279943 - 46.24%
	Lowercase: 261862 - 43.25%
	Digits: 63567 - 10.50%
	Other: 96 - 0.02%


A Modest Proposal Plain Text:
	Uppercase: 1469 - 3.67%
	Lowercase: 29770 - 74.38%
	Digits: 190 - 0.47%
	Other: 8595 - 21.47%
A Modest Proposal B64 Encoded:
	Uppercase: 24393 - 45.68%
	Lowercase: 23273 - 43.58%
	Digits: 5731 - 10.73%
	Other: 3 - 0.01%


A Strange Case of Dr. Jekyll and Hyde Plain Text:
	Uppercase: 4113 - 2.52%
	Lowercase: 119799 - 73.29%
	Digits: 185 - 0.11%
	Other: 39366 - 24.08%
A Strange Case of Dr. Jekyll and Hyde B64 Encoded:
	Uppercase: 102859 - 46.21%
	Lowercase: 96204 - 43.22%
	Digits: 23447 - 10.53%
	Other: 78 - 0.04%


All Books Plain Text:
	Uppercase: 51819 - 1.90%
	Lowercase: 1987623 - 72.80%
	Digits: 2228 - 0.08%
	Other: 688539 - 25.22%
All Books B64 Encoded:
	Uppercase: 1723174 - 46.58%
	Lowercase: 1599919 - 43.25%
	Digits: 375411 - 10.15%
	Other: 968 - 0.03%
```
