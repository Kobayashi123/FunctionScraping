# FunctionScraping

Rust の組み込み関数を表として出力するプログラムである。
Rust の公式ドキュメントからスクレイピングを行い、HTML ファイルを生成した。

# Features

Python を用いてプログラムを作成した。
スクレイピングを行うのが初めてで、試行錯誤しながら、プログラムを作成した。

# Requirement

- BeautifulSoup
- requests

# Installation

```zsh
pip install requests
pip install bs4
```

# Usage

```zsh
git clone https://github.com/Kobayashi123/FunctionScraping.git
cd BuiltInRustFunctionByPython

<1つ目のやり方>
python Example.py
open -a 'ブラウザ名' ~/BuiltInRustFunctionByPython/RustBuiltInFunction.html

<2つ目のやり方>
make test

RustFunctionByPythonディレクトリに移動した後は、どちらの方法でもよい。
実行後RustFunctionByPythonディレクトリにHTMLファイルが出力される。
```

# Author

- 小林舜

- 京都産業大学 情報理工学部

- E-mail: shun123k@gmail.com
