# 孤島開発　施設一覧

## 影響範囲とは

例えば影響範囲「３」と書いたときにその施設が影響する範囲は、以下の０～３の範囲です。

（即ちマンハッタン距離が３以下のマスに影響します）

![スクリーンショット 2023-12-13 221830](https://github.com/kabipoyo/island_development/assets/53305235/90a64dd3-ac4a-435a-9895-7fc10431d677)

## 特殊な施設・コマンド

|建物名|キー|建設コスト|地価|
|:--|:--|--:|--:|
|空地|` `|0|0|
|解体|`-`|0|0|

## 人口を増加させる施設

最初に建設すべき施設です。そのマスに所定の人口が発生します。人口 × 収入の額が、毎時得られます。

|建物名|キー|ラベル|建設コスト|収入|人口|地価|
|:--:|:--:|:--:|--:|--:|--:|--:|
|住宅|`家`|`house`|1,000|15|4|1|
|マンション|`マ`|`house`|50,000|20|15|5|
|タワーマンション|`タ`|`house`|1,000,000|40|50|20|

## 収入を増加させる施設

「影響範囲」内に存在する人口 × 収入の額が、毎時得られます。

|建物名|キー|ラベル|建設コスト|影響範囲|収入|地価|
|:--:|:--:|:--:|--:|--:|--:|--:|
|発電所|`電`|`electricity`|5,000|10|10|1|
|原子力発電所|`原`|`electricity`|70,000|10|30|5|
|上下水道局|`水`|`water`|5,000|10|10|1|
|上下水道処理施設|`処`|`water`|70,000|10|30|5|
|電波塔|`波`|`network`|50,000|10|20|5|
|東京スカイツリー|`東`|`network`|2,000,000|15|50|15|
|駅|`駅`|`station`|100,000|5|40|10|
|ターミナル駅|`S`|`station`|1,000,000|7|80|20|
|スーパー|`ス`|`shop`|5,000|3|20|2|
|商店街|`商`|`shop`|100,000|5|40|5|
|デパート|`デ`|`shop`|500,000|5|80|10|
|小・中学校|`学`|`school1`|10,000|5|15|2|
|高等学校|`高`|`school2`|30,000|7|15|3|
|大学キャンパス|`大`|`university`|100,000|10|20|5|
|畑|`畑`|`factory`|20,000|5|20|2|
|牧場|`牧`|`factory`|50,000|5|20|3|
|工場|`工`|`factory`|100,000|7|30|5|
|ITクラスター|`I`|`factory`|700,000|8|70|10|
|診療所|`診`|`hospital`|10,000|5|15|2|
|病院|`病`|`hospital`|200,000|7|30|5|
|交番|`交`|`police`|15,000|7|15|2|
|警察本部|`警`|`police`|300,000|10|40|5|
|消防署|`消`|`fire`|40,000|5|25|3|
|消防ヘリポート|`防`|`fire`|500,000|8|50|7|
|ゴミ埋立地|`ゴ`|`trash`|3,000|8|10|1|
|ゴミ焼却場|`焼`|`trash`|60,000|8|20|5|
|墓地|`墓`|`ceremony`|4,000|10|10|1|
|教会|`教`|`ceremony`|80,000|10|20|5|
|前方後円墳|`墳`|`ceremony`|500,000|10|40|10|
|ピラミッド|`ピ`|`ceremony`|2,000,000|10|70|20|
|映画館|`映`|`entertainment`|50,000|5|20|5|
|植物園|`植`|`entertainment`|300,000|7|30|7|
|水族館|`A`|`entertainment`|1,000,000|10|50|10|
|動物園|`Z`|`entertainment`|1,000,000|10|50|10|
|遊園地|`遊`|`entertainment`|1,000,000|10|50|10|
|ディズニーランド|`D`|`entertainment`|10,000,000|20|100|50|
|記念碑|`M`|`monument`|30,000,000|10|10|30|
