# pdf2in1_bound_right
Convert pdf to right-bound spread format.


pdf2in1_bound_right は、PDFファイル内のページを見開き形式で左右を入れ替えるPythonスクリプトです。コマンドラインから実行でき、入力PDFファイルを指定して、左右が入れ替わった見開きページの新しいPDFファイルを生成します。

## 必要条件

- Python 3.x
- pypdf

## インストール

pypdfをインストールしてください。

```
pip install pypdf
```

## 使い方

コマンドラインから次のように実行します。

```
python pdf_page_swapper.py -i <input_pdf> -o <output_pdf>
```

- `<input_pdf>`: 入力PDFファイルの名前
- `<output_pdf>`: 出力PDFファイルの名前 (オプション)

出力PDFファイル名を指定しない場合、入力PDFファイル名に`_swapped`が追加された名前が使用されます。

例:

```
python pdf_page_swapper.py -i example.pdf -o example_swapped.pdf
```

これにより、`example.pdf`ファイルのページを見開き形式で左右を入れ替え、新しいPDFファイル`example_swapped.pdf`を生成します。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
