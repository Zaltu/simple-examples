# GPT2
This example is an AI text generator based on the GPT2 model. From an input phrase, it generates the 20 text componants it believes could follow that phrase.

To keep a sense of random to the response and to guarentee different responses to the same input, a top-p algorithm is used on the potential returned text componants, configured at 70%.

Note that it will take a long-ass time to download, and a long-ass time to load, since this uses the 1558M model of GPT-2.


## Requirements
- PyTorch (Deep Learning Library): `pip install torch`
- transformers (Trained model loader): `pip install transformers`


## Sources
This example is built based on the following resources:  
- [Build a Text Generator in 50 lines](https://towardsdatascience.com/build-a-text-generator-web-app-in-under-50-lines-of-python-9b63d47edabb)
- [PyTorch Transformers Quickstart](https://huggingface.co/transformers/quickstart.html)
