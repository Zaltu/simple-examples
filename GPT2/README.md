# GPT2
This example is an AI text generator based on the GPT2 model. From an input phrase, it generates the 20 text componants it believes could follow that phrase.

To keep a sense of random to the response and to guarentee different responses to the same input, a top-p algorithm is used on the potential returned text componants, configured at 70%.

Note that it will take a long-ass time to download, and a long-ass time to load, since this uses the 1558M model of GPT-2. There's a baseline requirement of around 20GB RAM because of this.


## speak.py
This is the very basic example of generating text itself. It's not very user-friendly, but gives an overview of what the actual AI module needs in order to run.  
The number of generated words is set in the range for-loop. High numbers will undoubtably kill the machine, since no optimization is done.


## iterative_speak.py
This is an example of a more user-friendly (ie import friendly) wrapper around the functionality. It also has a generator version of the function allowing more intuitive use in loops. The number of iterations is passed to whichever function. There is still no real optimization done for long texts, so high numbers of iterations are generally a bad idea.


## long_speak.py
When using the previous examples with high numbers of iterations (200+) to generate small paragraphs, there's a small issue where it takes like shittons of RAM. Approximately 8-9GB per 100 words. Since loading the gpt2-xl model itself takes a solid 10GB+, this quickly adds up to more than a home PC could reasonably be expected to have. This file adds a metric by which each N words, the cached calculations and the source text are reset. This means the model is never processing more than N words, essentially.

While this is good for RAM, it also has two major downsides. The first is that it's longer. Because the past calculations are reset, every N words the model will need to recalculate the current selection from scratch. The second, more obvious, is that this makes it technically less intelligent in terms of text generation. As you would expect, the more text it has to base itself off, the more accurate and realistic it generally turns out to be. Not only does this set a cap on that metric, but for each time the past is recalculated, so for each multiple of N in the length of the words, there's a bigger chance it will "get distracted" and recalculate something that wasn't quite following it's previous trend. With a decently high N, (default 50), the GPT2-XL model still provides a very solid generation, without using egregious amounts of RAM.

*As a side note, setting the N to 50 actually means that a maximum of 99 words are processed at once, since there will be 50 past words and 49 generated words before it's reset again.*


## Requirements
- PyTorch (Deep Learning Library): `pip install torch`
- transformers (Trained model loader): `pip install transformers`


## Sources
This example is built based on the following resources:  
- [Build a Text Generator in 50 lines](https://towardsdatascience.com/build-a-text-generator-web-app-in-under-50-lines-of-python-9b63d47edabb)
- [PyTorch Transformers Quickstart](https://huggingface.co/transformers/quickstart.html)
