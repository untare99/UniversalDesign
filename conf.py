# conf.py

# -- プロジェクト情報 -----------------------------------------------------
project = 'Universal Ddesign'
author = 'Untare99'
release = '0.1'

# -- 拡張機能の設定 -----------------------------------------------------
extensions = [
    'myst_parser',                  # Markdownサポート
    #'sphinxcontrib.mermaid',        # Mermaid図表描画
    #'sphinx_markdown_tables',       # Markdownテーブルのサポート
    #'sphinx_copybutton',            # コピーボタンの追加
    #'sphinx_diagrams',              # 図表描画
    # 他の拡張機能があればここに追加
]

language = 'ja'

# -- テーマの設定 ---------------------------------------------------------
#html_theme = 'furo'                 # Furoテーマを使用
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'

# -- ソースファイルの拡張子の設定 -----------------------------------------
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Masterドキュメントの設定 --------------------------------------------
master_doc = 'index'

# -- MyST-Parserの設定 ----------------------------------------------------
myst_enable_extensions = [
    "dollarmath",        # インラインおよびブロック数式のサポート
    "amsmath",           # AMS math機能のサポート
    "colon_fence",       # コロンフェンスのサポート
    "deflist",           # 定義リストのサポート
    "html_admonition",   # HTML警告のサポート
    "html_image",        # HTML画像のサポート
]

# -- sphinx_copybuttonの設定 ---------------------------------------------
copybutton_prompt_text = '>>> '    # コードブロックのプロンプトテキスト
copybutton_prompt_is_regexp = True  # プロンプトテキストを正規表現として扱う

# -- sphinxcontrib.mermaidの設定 -----------------------------------------
mermaid_output_format = 'svg'        # Mermaid図の出力形式

# -- sphinx_diagramsの設定 ------------------------------------------------
# sphinx_diagramsは特別な設定は不要ですが、必要に応じて設定を追加します

# -- HTML静的ファイルの設定 -----------------------------------------------
html_static_path = ['_static']

# -- カスタムCSSの設定 ----------------------------------------------------
html_css_files = [
    'custom.css',
]