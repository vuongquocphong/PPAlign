# Modified Bertalign Sentence Alignment Approach to support Vietnamese (PPAlign)

## Introduction

This repository is a modified version of the original implementation of Bertalign to support Vietnamese.

## Requirements (MUST HAVE)

Python 3.10.11

## Installation

```bash
pip install -r requirements.txt
```

## Basic example

Just import *PPAlign* and initialize it with the source and target text, which will split both texts into sentences automatically. Then invoke the method *align_sents()*  to align sentences and print out the result with *print_sents()*.

```python
from ppalign import PPAlign
```

```python
src = """建宁二年四月望日，帝御温德殿。方升座，殿角狂风骤起。只见一条大青蛇，从梁上飞将下来，蟠于椅上。帝惊倒，左右急救入宫，百官俱奔避。须臾，蛇不见了。忽然大雷大雨，加以冰雹，落到半夜方止，坏却房屋无数。建宁四年二月，洛阳地震；又海水泛溢，沿海居民，尽被大浪卷入海中。光和元年，雌鸡化雄。六月朔，黑气十余丈，飞入温德殿中。秋七月，有虹现于玉堂；五原山岸，尽皆崩裂。种种不祥，非止一端。帝下诏问群臣以灾异之由，议郎蔡邕上疏，以为蜺堕鸡化，乃妇寺干政之所致，言颇切直。帝览奏叹息，因起更衣。曹节在后窃视，悉宣告左右；遂以他事陷邕于罪，放归田里。后张让、赵忠、封谞、段珪、曹节、侯览、蹇硕、程旷、夏恽、郭胜十人朋比为奸，号为“十常侍”。帝尊信张让，呼为“阿父”。朝政日非，以致天下人心思乱，盗贼蜂起。"""

tgt = """Ngày rằm tháng tư năm Kiến ninh thứ hai (một trăm sáu mươi bảy dương lịch) vua ngự điện Ôn Đức. Tự nhiên có cơn gió to ầm ầm từ góc điện nổi lên, rồi thấy một con rắn xanh lớn ở trên xà nhà quăng xuống quằn quại trên long án. Vua kinh hoàng ngã đùng ra, các quan tả hữu vội cứu vực vào cung; ở ngoài văn võ cũng sợ chạy cả. Được một lát con rắn biến mất và bỗng nhiên mưa to, sấm sét ầm ầm; lại thêm mưa đá rào rào mãi đến nửa đêm mới tạnh, đổ nhà đổ cửa không biết bao nhiêu mà kể. Tháng hai, năm Kiến ninh thứ tư (một trăm sáu mươi chín) tỉnh Lạc Dương có động đất, nước bể dâng lên ngập lưng trời, dân cư ở ven bể bị sóng lớn cuốn trôi đi mất cả. Năm Quang hóa thứ nhất (một trăm bảy mươi tám), một con gà mái tự dưng hóa ra gà trống. Mồng một tháng sáu năm ấy, một luồng khí đen dài chừng hơn mươi trượng bay vào trong điện Ôn Đức. Qua sang tháng bảy, lại có lắm điều gở lạ: Cầu vồng mọc ở giữa Ngọc đường; rặng núi Ngũ Nguyên bỗng dưng lở sụt xuống. Vua hạ chiếu, hỏi chư thần từ đâu mà sinh ra những điềm quái gở ấy. Có quan nghị lang là Sái Ung dâng sớ lên, lời lẽ thống thiết, nói rằng: "Cầu vồng sa xuống, gà mái hóa trống, ấy là bởi quyền chính trong nước ở tay đàn bà và ở tay hoạn quan". Vua xem sớ ngậm ngùi thở dài, đứng dậy thay áo. Tào Tiết khi ấy đứng hầu sau ngai nghe trộm thấy, trong lòng căm giận, bèn mách bảo đồng bọn, bàn mưu kiếm cớ vu hãm Sài Ung, cách quan đuổi về quê quán. Về sau bọn hoạn quan là Trương Nhượng, Triệu Trung, Phong Tư, Đoan Khuê, Tào Tiết, Hầu Lãm, Kiển Thạc, Trình Khoáng, Hạ Huy, Quách Thắng, cả thẩy mười người gọi là mười quan "Thường thị" bè đảng với nhau kéo cánh làm càn. Nhà vua tin dùng tôn trọng Trương Nhượng, gọi là "Á phụ" (nghĩa là vua coi như cha). Từ đấy chính sự trong triều ngày càng đổ nát, lòng người náo loạn, giặc cướp nổi lên như ong."""
```

```python
aligner = PPAlign(src, tgt)
aligner.align_sents()
```
    Source language: zh, Number of sentences: 17
    Target language: vi, Number of sentences: 15
    Embedding source and target text using LaBSE ...
    Preparing words list ...
    Performing first-step alignment ...
    Performing second-step alignment ...
    Finished! Successfully aligning 17 zh sentences to 15 vi sentences

```python
aligner.print_sents()
```

    建宁二年四月望日，帝御温德殿。
    Ngày rằm tháng tư năm Kiến ninh thứ hai (một trăm sáu mươi bảy dương lịch) vua ngự điện Ôn Đức.

    方升座，殿角狂风骤起。只见一条大青蛇，从梁上飞将下来，蟠于椅上。
    Tự nhiên có cơn gió to ầm ầm từ góc điện nổi lên, rồi thấy một con rắn xanh lớn ở trên xà nhà quăng xuống quằn quại trên long án.

    帝惊倒，左右急救入宫，百官俱奔避。
    Vua kinh hoàng ngã đùng ra, các quan tả hữu vội cứu vực vào cung; ở ngoài văn võ cũng sợ chạy cả.

    须臾，蛇不见了。忽然大雷大雨，加以冰雹，落到半夜方止，坏却房屋无数。
    Được một lát con rắn biến mất và bỗng nhiên mưa to, sấm sét ầm ầm; lại thêm mưa đá rào rào mãi đến nửa đêm mới tạnh, đổ nhà đổ cửa không biết bao nhiêu mà kể.

    建宁四年二月，洛阳地震；又海水泛溢，沿海居民，尽被大浪卷入海中。
    Tháng hai, năm Kiến ninh thứ tư (một trăm sáu mươi chín) tỉnh Lạc Dương có động đất, nước bể dâng lên ngập lưng trời, dân cư ở ven bể bị sóng lớn cuốn trôi đi mất cả.

    光和元年，雌鸡化雄。
    Năm Quang hóa thứ nhất (một trăm bảy mươi tám), một con gà mái tự dưng hóa ra gà trống.

    六月朔，黑气十余丈，飞入温德殿中。
    Mồng một tháng sáu năm ấy, một luồng khí đen dài chừng hơn mươi trượng bay vào trong điện Ôn Đức.

    秋七月，有虹现于玉堂；五原山岸，尽皆崩裂。种种不祥，非止一端。
    Qua sang tháng bảy, lại có lắm điều gở lạ: Cầu vồng mọc ở giữa Ngọc đường; rặng núi Ngũ Nguyên bỗng dưng lở sụt xuống.

    帝下诏问群臣以灾异之由，议郎蔡邕上疏，以为蜺堕鸡化，乃妇寺干政之所致，言颇切直。
    Vua hạ chiếu, hỏi chư thần từ đâu mà sinh ra những điềm quái gở ấy. Có quan nghị lang là Sái Ung dâng sớ lên, lời lẽ thống thiết, nói rằng: "Cầu vồng sa xuống, gà mái hóa trống, ấy là bởi quyền chính trong nước ở tay đàn bà và ở tay hoạn quan".

    帝览奏叹息，因起更衣。
    Vua xem sớ ngậm ngùi thở dài, đứng dậy thay áo.

    曹节在后窃视，悉宣告左右；遂以他事陷邕于罪，放归田里。
    Tào Tiết khi ấy đứng hầu sau ngai nghe trộm thấy, trong lòng căm giận, bèn mách bảo đồng bọn, bàn mưu kiếm cớ vu hãm Sài Ung, cách quan đuổi về quê quán.

    后张让、赵忠、封谞、段珪、曹节、侯览、蹇硕、程旷、夏恽、郭胜十人朋比为奸，号为“十常侍”。
    Về sau bọn hoạn quan là Trương Nhượng, Triệu Trung, Phong Tư, Đoan Khuê, Tào Tiết, Hầu Lãm, Kiển Thạc, Trình Khoáng, Hạ Huy, Quách Thắng, cả thẩy mười người gọi là mười quan "Thường thị" bè đảng với nhau kéo cánh làm càn.

    帝尊信张让，呼为“阿父”。
    Nhà vua tin dùng tôn trọng Trương Nhượng, gọi là "Á phụ" (nghĩa là vua coi như cha).

    朝政日非，以致天下人心思乱，盗贼蜂起。
    Từ đấy chính sự trong triều ngày càng đổ nát, lòng người náo loạn, giặc cướp nổi lên như ong.

## Batch processing & evaluation

The following example shows how to use PPAlign to align the Data corpus, and evaluate its performance with gold standard alignments. The evaluation script [eval.py](./ppalign/eval.py) is based on [Bertalign](https://github.com/bfsujason/bertalign).

Please see [aligner.py](./ppalign/aligner.py) for more options to configure PPAlign.

```python
import os
from ppalign import PPAlign
from ppalign.eval import *
```

```python
src_dir = "./Data/zh"
tgt_dir = "./Data/vi"
golden_dir = "./Data/golden"
```

```python
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
```

    Start aligning text+berg/de/001 to text+berg/fr/001
    Start aligning ./Data/zh/002.txt to ./Data/vi/002.txt
    Source language: zh, Number of sentences: 17
    Target language: vi, Number of sentences: 15
    Embedding source and target text using LaBSE ...
    Preparing words list ...
    Performing first-step alignment ...
    Performing second-step alignment ...
    Finished! Successfully aligning 17 zh sentences to 15 vi sentences

    Start aligning ./Data/zh/001.txt to ./Data/vi/001.txt
    Source language: zh, Number of sentences: 8
    Target language: vi, Number of sentences: 9
    Embedding source and target text using LaBSE ...
    Preparing words list ...
    Performing first-step alignment ...
    Performing second-step alignment ...
    Finished! Successfully aligning 8 zh sentences to 9 vi sentences

```python
scores = score_multiple(gold_list=gold_alignments, test_list=test_alignments)
log_final_scores(scores)
```

    ---------------------------------
    |             |  Strict |    Lax  |
    | Precision   |   1.000 |   1.000 |
    | Recall      |   1.000 |   1.000 |
    | F1          |   1.000 |   1.000 |
    ---------------------------------

## Citation

V.Q.Phong. L.V.Phuc: Bachelor Thesis: “AUTOMATIC SENTENCE ALIGNMENT FOR ANCIENT CHINESE AND VIETNAMESE TRANSLATION, University of Science, Vietnam National University, Ho Chi Minh City” 2025.

## Licence

Bertalign is released under the [GNU General Public License v3.0](./LICENCE)

## References
[PPAlign](https://github.com/vuongquocphong/PPAlign)

## Credits

##### Main Libraries

* [sentence-transformers](https://github.com/UKPLab/sentence-transformers)

* [faiss](https://github.com/facebookresearch/faiss)

* [underthesea](https://github.com/undertheseanlp/underthesea)

