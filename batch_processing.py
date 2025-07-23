import os
from ppalign import PPAlign
from ppalign.eval import *

src_dir = "./Data/zh"
tgt_dir = "./Data/vi"
golden_dir = "./Data/golden"

test_alignments = []
gold_alignments = []

for file in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file).replace("\\","/")
    tgt_file = os.path.join(tgt_dir, file).replace("\\","/")
    src = open(src_file, 'rt', encoding='utf-8').read()
    tgt = open(tgt_file, 'rt', encoding='utf-8').read()

    print("Start aligning {} to {}".format(src_file, tgt_file))
    aligner = PPAlign(src, tgt)
    aligner.align_sents()
    test_alignments.append(aligner.result)

    gold_file = os.path.join(golden_dir, file)
    gold_alignments.append(read_alignments(gold_file))

scores = score_multiple(gold_list=gold_alignments, test_list=test_alignments)
log_final_scores(scores)

