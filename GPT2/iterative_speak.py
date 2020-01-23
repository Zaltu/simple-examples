"""
Sample implementation of generating text using GPT-2 1558M data model.
Absolute poggers.
"""
from random import choice
import torch
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2LMHeadModel

TOKENIZER = GPT2Tokenizer.from_pretrained("gpt2-xl")
MODEL = GPT2LMHeadModel.from_pretrained("gpt2-xl")

def _model(input_ids, model, past, p=0.7):  #pylint: disable=invalid-name
    """
    Generate a text component that may fit following the text sample given as input.

    :param str input_ids: input text
    :param GPTLMHeadModel model: the ML model to use
    :param torch.Tensor past: the past computational tensor of previous runs
    :param float p: top-p value used for randomization of selection

    :returns: text component that may follow the input text
    :rtype: str
    """
    input_ids = input_ids.unsqueeze(0)
    output, past = model(input_ids, past)
    logits = output[:, -1]
    probs = F.softmax(logits, dim=-1).squeeze()
    idxs = torch.argsort(probs, descending=True)
    res, cumsum = [], 0.
    for idx in idxs:
        res.append(idx)
        cumsum += probs[idx]
        if cumsum > p:
            pred_idx = idxs.new_tensor([choice(res)])
            break
    return pred_idx, past


def xspeak(starting_text, iterations=20):
    word = torch.tensor(TOKENIZER.encode(starting_text))
    past_cache = None
    yield starting_text
    for _ in range(0, iterations):
        word, past_cache = _model(word, MODEL, past_cache)
        yield TOKENIZER.decode([word])


def speak(starting_text, iterations=20):
    word = torch.tensor(TOKENIZER.encode(starting_text))
    past_cache = None
    generated = TOKENIZER.encode(starting_text)
    for _ in range(0, iterations):
        word, past_cache = _model(word, MODEL, past_cache)
        generated += [word]
    return TOKENIZER.decode(generated)

print("Iterator=True")
for chunk in xspeak("Though I walk in the valley of the shadow of death, I shall fear no"):
    print(chunk, end="", flush=True)

print()
print("Iterator=False")
print(speak("Though I walk in the valley of the shadow of death, I shall fear no"))
