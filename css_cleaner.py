import glob

# .cssを探す
css_files = glob.glob("/Users/shigeho/Documents/GitHub/vivito_renew/src/assets/css/**.css", recursive=True)
# print(css_files)
# print(css_files[0])

# セレクタを探してリスト化する
file = open(css_files[0])
contents = file.read()
selectors_all = contents.split()

selectors = [s for s in selectors_all if s.startswith('.')]
selectors = list(set(selectors))


file.close()



# htmlを探す
# htmlファイルをリストで保持する
# セレクタでhtmlを検索する
# 全く使われないセレクタを抽出する
# セレクタを削除する


# TODO
# そもそも宣言すらされていないcssを洗い出す
# cssが間違ってたら？
# 別ファイルで同一セレクタがあったら？(同一ファイルなら上書きでOK(CSSの仕様による))
# 連想配列で持たせて、キーは枝番をつける。
# 1行に複数のセレクタが存在する場合




