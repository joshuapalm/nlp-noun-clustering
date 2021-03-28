import nltk
from nltk.probability import FreqDist


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')



def single_freqs(tags, prefix='', top_n=0):
    freqs = dict(FreqDist(tags))
    total = sum([v for k,v in freqs.items()])
    norm_freqs = dict([(prefix+k,v/total) for k,v in freqs.items()])
    if top_n > 0:
        return dict(sorted(norm_freqs.items(), key=lambda x: x[1], reverse=True)[:top_n])
    return norm_freqs


def double_freqs(tags, prefix='', top_n=10):
    res = []
    i = 0
    while(i < (len(tags) - 1)):
        res.append(tags[i] + '_' + tags[i+1])
        i += 1
    freqs = dict(FreqDist(res))
    total = sum([v for k,v in freqs.items()])
    norm_freqs = dict([(prefix+k,v/total) for k,v in freqs.items()])

    if top_n > 0:
        return dict(sorted(norm_freqs.items(), key=lambda x: x[1], reverse=True)[:top_n])
    return norm_freqs


def triple_freqs(tags, prefix='', top_n=10):
    res = []
    i = 0
    while(i < (len(tags) - 2)):
        res.append(tags[i] + '_' + tags[i+1] + '_' + tags[i+2])
        i += 1
    freqs = dict(FreqDist(res))
    total = sum([v for k,v in freqs.items()])
    norm_freqs = dict([(prefix+k,v/total) for k,v in freqs.items()])

    if top_n > 0:
        return dict(sorted(norm_freqs.items(), key=lambda x: x[1], reverse=True)[:top_n])
    return norm_freqs


def apply_on_parts(tags, functions, splits):
    delta = len(tags) // splits

    res = dict()
    i = 1
    current_idx = 0
    while (i <= splits):
        content = tags[current_idx:current_idx+delta]
        for f in functions:
            prefix_str = 'freq_{}ov{}_'.format(i, splits)
            features = f(content, prefix=prefix_str)
            res.update(features)
        current_idx += delta
        i += 1
    return res

