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

def get_pred(input_ids, model, past, p=0.7):  #pylint: disable=invalid-name
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


SAMPLE_TEXT = 'And the man answered, saying "My name is legion, for we are'
WORD = torch.tensor(TOKENIZER.encode(SAMPLE_TEXT))
PAST_CACHE = None
print("Starting input...")
GENERATED = TOKENIZER.encode(SAMPLE_TEXT)
for i in range(0, 20):
    WORD, PAST_CACHE = get_pred(WORD, MODEL, PAST_CACHE)
    GENERATED += [WORD]
print(TOKENIZER.decode(GENERATED))
