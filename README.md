# Base64 Distribution

Little project I was working on to determine the distribution of uppercase, lowercase, and numerical characters in Base64. I was talking to a coworker trying to figure out how to detect exfiltration attempts in DNS logs, when this idea occured to me. I figured since Base64 regex is pretty bad (considering it's just plain-text), I wanted a better way to figure out how to determine Base64 from plain-text, without having to muck around in AI/ML/NN.

Huge thanks to the following sources for allowing me to grab their data:
	
* [Guttenburg Project](https://www.gutenberg.org/)
* [CPython](https://codeload.github.com/python/cpython/zip/master)
* [cURL Project](https://codeload.github.com/curl/curl/zip/master)
* [Microsoft Terminal](https://codeload.github.com/microsoft/terminal/zip/master)
* [PowerShell Empire](https://codeload.github.com/EmpireProject/Empire/zip/master)
* [Microsoft Powershell](https://codeload.github.com/PowerShell/PowerShell/zip/master)


# Distributions

The distribution for English books (akak plain old English text) is:

```
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


Here is a code breakdown:

```
.py Plain Text:
	Uppercase: 1426221 - 4.79%
	Lowercase: 14627787 - 49.12%
	Digits: 609286 - 2.05%
	Other: 13115742 - 44.04%
.py Base64 Encoded:
	Uppercase: 20803623 - 52.39%
	Lowercase: 15453495 - 38.92%
	Digits: 3430589 - 8.64%
	Other: 17677 - 0.04%


.c Plain Text:
	Uppercase: 561185 - 10.12%
	Lowercase: 2581084 - 46.56%
	Digits: 87542 - 1.58%
	Other: 2313340 - 41.73%
.c Base64 Encoded:
	Uppercase: 3803898 - 51.47%
	Lowercase: 2842024 - 38.45%
	Digits: 736343 - 9.96%
	Other: 8603 - 0.12%


.cpp Plain Text:
	Uppercase: 653910 - 11.01%
	Lowercase: 2878811 - 48.47%
	Digits: 50933 - 0.86%
	Other: 2356217 - 39.67%
.cpp Base64 Encoded:
	Uppercase: 4174443 - 52.71%
	Lowercase: 2901204 - 36.63%
	Digits: 839873 - 10.60%
	Other: 4308 - 0.05%


.ps1 Plain Text:
	Uppercase: 7871359 - 46.37%
	Lowercase: 5532829 - 32.60%
	Digits: 1285180 - 7.57%
	Other: 2284692 - 13.46%
.ps1 Base64 Encoded:
	Uppercase: 13922688 - 61.52%
	Lowercase: 6467575 - 28.58%
	Digits: 2240937 - 9.90%
	Other: 880 - 0.00%


.cs Plain Text:
	Uppercase: 1720048 - 5.65%
	Lowercase: 14758065 - 48.47%
	Digits: 115172 - 0.38%
	Other: 13857055 - 45.51%
.cs Base64 Encoded:
	Uppercase: 21804730 - 53.71%
	Lowercase: 15203864 - 37.45%
	Digits: 3548486 - 8.74%
	Other: 43376 - 0.11%


All languages Plain Text:
	Uppercase: 12232723 - 13.79%
	Lowercase: 40378576 - 45.53%
	Digits: 2148113 - 2.42%
	Other: 33927046 - 38.26%
All languages Base64 Encoded:
	Uppercase: 64509382 - 54.55%
	Lowercase: 42868162 - 36.25%
	Digits: 10796228 - 9.13%
	Other: 74844 - 0.06%
```
