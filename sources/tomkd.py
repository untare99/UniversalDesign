from markitdown import MarkItDown  # MarkItDownモジュールからMarkItDownクラスをインポート
#import os  # OS関連の操作を行うためのモジュールをインポート

markitdown = MarkItDown()
result = markitdown.convert("UniversalDesign.pptx")  # ファイルをMarkdown形式に変換
text_file = "UniversalDesign.md"  # 出力するMarkdownファイルの名前を作成

with open(text_file, "w", encoding="utf-8") as f:  # MarkdownファイルをUTF-8エンコーディングで書き込みモードで開く
    f.write(result.text_content)  # 変換結果のテキストコンテンツを書き込む
