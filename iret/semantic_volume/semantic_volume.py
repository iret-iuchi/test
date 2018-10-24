import re
import MeCab
import numpy as np
from gensim.models import Word2Vec

tokenizer = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
available_pos = ["名詞", "動詞-自立", "形容詞"]
not_available_pos = ["名詞-数"]

model = Word2Vec.load('word2vec.gensim.model')
features = 50

# MeCabで形態素に分割
def split_words(sentence):
    result = []
    chasen_result = tokenizer.parse(sentence)
    for line in chasen_result.split("\n"):
        elems = line.split("\t")
        if len(elems) < 4:
            continue
        word = elems[0]
        pos = elems[3]
        if True in [pos.startswith(w) for w in not_available_pos]:
            continue
        if True in [pos.startswith(w) for w in available_pos]:
            result.append(word)
    return result

# 文章をベクトルに変換（単語の平均ベクトルを用いる）
def wordvec2docmentvec(sentence,vec_model,num_features):
    doc_vec = np.zeros(num_features, dtype="float32")
    for word in sentence:
        try:
            temp = vec_model[word]
        except:
            continue
        doc_vec += temp
    if len(sentence)>0:
        doc_vec =  doc_vec / len(sentence)
    return doc_vec

original_data = []
corpus = []
corpus_vec = []
with open('spaia.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for sentence in data:
        sentence = sentence[:-1]
        if re.match(r"［", sentence):
            continue
        sentence = re.sub(r"《[^》]*》", "", sentence)
        h = split_words(sentence)
        if len(h) == 0:
            continue
        original_data.append(sentence)
        corpus.append(" ".join(h))
        corpus_vec.append(wordvec2docmentvec(h, model, features))

# Proj を計算
def projection(u, b):
    return np.dot(u,b) * b

# 基底ベクトル
def basis_vector(v):
    return v / np.linalg.norm(v)

#　Distance(u_i, B)
def span_distance(v, span_space):
    proj = np.zeros(features, dtype="float32")
    for span_vec in span_space:
        proj += projection(v, span_vec)
    return np.linalg.norm(v - proj)

# index of sentence that is farthest from the subspace of Span(B).
def compute_farthest_spanspace(sentences_vector, span_space, skip_keys):
    distance = 0
    farthest_key = 0
    for i, vec in enumerate(sentences_vector):
        if i in skip_keys:
            continue
        dist = span_distance(vec, span_subspace)
        if dist >= distance:
            distance = dist
            farthest_key = i
    return farthest_key

L = 100 # 要約したい文字数
yoyaku_index = [] # 要約対象の文章ID

# 重心を計算
centroid = np.zeros(features, dtype="float32")
for vec in corpus_vec:
    centroid += vec
centroid /= len(corpus_vec)

# index of sentence that is farthest from the cluster centroid
distance = 0
first_yoyaku_index = 0
for i, vec in enumerate(corpus_vec):
    dist = np.linalg.norm(centroid - vec)
    if dist >= distance:
        distance = dist
        first_yoyaku_index = i
yoyaku_index.append(first_yoyaku_index)

# index of sentence that is farthest from s_p
distance = 0
second_yoyaku_index = 0
for i, vec in enumerate(corpus_vec):
    if i in yoyaku_index:
        continue
    dist = np.linalg.norm(corpus_vec[first_yoyaku_index] - vec)
    if dist >= distance:
        distance = dist
        second_yoyaku_index = i
yoyaku_index.append(second_yoyaku_index)

# total length
total_length = len(original_data[first_yoyaku_index]) + len(original_data[second_yoyaku_index])

# first basis vector
first_basis_vector = basis_vector(corpus_vec[second_yoyaku_index])
span_subspace = [first_basis_vector]

while(True):
    farthest_index = compute_farthest_spanspace(corpus_vec, span_subspace, yoyaku_index)
    if len(original_data[farthest_index]) + total_length <= L:
        span_subspace.append(corpus_vec[farthest_index])
        total_length += len(original_data[farthest_index])
        yoyaku_index.append(farthest_index)
    else:
        break

print(yoyaku_index)

for i in yoyaku_index:
    print(original_data[i])
