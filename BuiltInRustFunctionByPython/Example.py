#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
スクレイピングプログラム：Rast言語の組み込み関数をまとめて表示するWebページを作成するプログラム
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.6'
__date__ = '2022/03/09 (Created: 2022/03/07)'

import os
from bs4 import BeautifulSoup
import requests


def main():
    """
    Rustの組み込み関数のWebページをウェブスクレイピングするプログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """

    primitive_table, mod_table, macro_table, keyword_table = table_of_builtin_function_and_hyper_reference(
        "https://doc.rust-lang.org/std/index.html")
    if (primitive_table is None) or (mod_table is None) or (macro_table is None):
        return 1

    home_directory = os.path.expanduser('~')
    a_file = os.path.join(
        home_directory, 'python', 'BuiltInRustFunctionByPython', 'RustBuiltInFunction.html')

    with open(a_file, 'w', encoding='utf-8') as a_file:
        a_file.write(head_part())

        # プリミティブ型の表を出力
        a_file.write(
            '       <table class="content" summary="table">\n')
        a_file.write('           <tbody>\n')
        a_file.write('               <tr>\n')
        a_file.write(
            '                   <th class="center-border">プリミティブ型</th>\n')
        a_file.write('               </tr>\n')

        td_string = '                   <td class="center-border"><a href="{}" title="Primitive">{}</a></td>\n'

        for key, value in primitive_table.items():
            builtin_module = key
            a_file.write('               <tr>\n')
            hyper_reference = value
            a_file.write(td_string.format(hyper_reference, builtin_module))
            a_file.write('               </tr>\n')

        a_file.write('           </tbody>\n')
        a_file.write('       </table>\n')

    # モジュールの表を出力
        a_file.write(
            '       <table class="content" summary="table">\n')
        a_file.write('           <tbody>\n')
        a_file.write('               <tr>\n')
        a_file.write(
            '                   <th class="center-border">モジュール</th>\n')
        a_file.write('               </tr>\n')

        td_string = '                   <td class="center-border"><a href="{}" title="Module">{}</a></td>\n'

        for key, value in mod_table.items():
            builtin_module = key
            a_file.write('               <tr>\n')
            hyper_reference = value
            a_file.write(td_string.format(hyper_reference, builtin_module))
            a_file.write('               </tr>\n')

        a_file.write('           </tbody>\n')
        a_file.write('       </table>\n')

    # マクロの表を出力
        a_file.write(
            '       <table class="content" summary="table">\n')
        a_file.write('           <tbody>\n')
        a_file.write('               <tr>\n')
        a_file.write(
            '                   <th class="center-border">マクロ</th>\n')
        a_file.write('               </tr>\n')

        td_string = '                   <td class="center-border"><a href="{}" title="Macro">{}</a></td>\n'

        for key, value in macro_table.items():
            builtin_module = key
            a_file.write('               <tr>\n')
            hyper_reference = value
            a_file.write(td_string.format(hyper_reference, builtin_module))
            a_file.write('               </tr>\n')

        a_file.write('           </tbody>\n')
        a_file.write('       </table>\n')

    # キーワードの表を出力
        a_file.write(
            '       <table class="content" summary="table">\n')
        a_file.write('           <tbody>\n')
        a_file.write('               <tr>\n')
        a_file.write(
            '                   <th class="center-border">キーワード</th>\n')
        a_file.write('               </tr>\n')

        td_string = '                   <td class="center-border"><a href="{}" title="Keyword">{}</a></td>\n'

        for key, value in keyword_table.items():
            builtin_module = key
            a_file.write('               <tr>\n')
            hyper_reference = value
            a_file.write(td_string.format(hyper_reference, builtin_module))
            a_file.write('               </tr>\n')

        a_file.write('           </tbody>\n')
        a_file.write('       </table>\n')

        a_file.write(foot_part())

    return 0


def head_part():
    """
    HTMLファイルのヘッダー部分を応答します。
    """

    return """<!DOCTYPE html>

<html lang="ja">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="Content-Style-Type" content="text/css">
        <meta http-equiv="Content-Script-Type" content="text/javascript">
        <meta name="keywords" content="Rust,Rustacean,Program,Programmer,Object,Oriented,Programming,Functional">
        <meta name="description" content="組み込み関数-Rust 1.59.0">
        <meta name="author" content="Kobayashi Shun">
        <link rel="index" href="index-j.html">
        <style type="text/css">
        <!--
        body {
            background-color : #ffffff;
            margin : 20px;
            padding : 10px;
            font-family : serif;
            font-size : 12pt;
        }
        div {
        display: flex;
        }
        table.content {
            border-style : solid;
            border-width : 0px;
            border-color : #ffffff;
        }
        .center-border {
            text-align : center;
            vertical-align : middle;
            empty-cells : show;
            border-style : solid;
            border-width : 1px;
            border-color : #ffc080;
            width : 350px;
            height : 22px;
        }
        -->
        </style>
        <title>組み込み関数-Rust 1.59.0</title>
    </head>

    <body>
        <h1>Rust言語の組み込み関数</h1>
        <p>Rustの公式ドキュメントはこちら : <a href="https://doc.rust-lang.org/std/index.html">https://doc.rust-lang.org/std/index.html</a></p>
        <div>
"""


def foot_part():
    """
    HTMLファイルのフッター部分を応答します。
    """

    return """      </div>
    </body>
</html>"""


def table_of_builtin_function_and_hyper_reference(the_url_string):
    """
    Rustの組み込みアイテムのWebページをウェブスクレイピングし、組み込みアイテムとハイパーリンクの辞書を作って応答します。
    実際には、Webページを解析して、プリミティブ型やモジュールなど様々な表を作成し、応答しています。
    抽出できない場合には、Noneを応答します。
    """

    response = requests.get(the_url_string)
    if response.status_code != 200:
        return None

    response.encoding = response.apparent_encoding
    html_source = response.text

    beautiful_soup = BeautifulSoup(html_source, 'html.parser')

    div_tag_set = beautiful_soup.find_all(
        name='div', attrs={'class': 'item-row'})

    primitive_table = generate_table(div_tag_set, 'primitive', the_url_string)
    mod_table = generate_table(div_tag_set, 'mod', the_url_string)
    macro_table = generate_table(div_tag_set, 'macro', the_url_string)
    keyword_table = generate_table(div_tag_set, 'keyword', the_url_string)

    return primitive_table, mod_table, macro_table, keyword_table


def generate_table(div_tag_set, tag_name, the_url_string):
    """
    渡された<div>タグの集合とタグのクラス名から組み込みアイテムとハイパーリンクの辞書を作って応答します。
    実際には、指定されたページから、組み込みアイテムのtableタグを探し出し、組み込みアイテム名とハイパーリンクを抽出します。
    抽出できない場合には、Noneを応答します。
    """
    table = {}
    for div_an_item in div_tag_set:
        a_tag = div_an_item.find(name='a', attrs={'class': tag_name})
        if a_tag is not None:
            builtin_function = a_tag.string.strip()
            hyper_reference = the_url_string.replace(
                'index.html', '') + a_tag['href']
            # print('"{}" : "{}"'.format(builtin_function, hyper_reference))

            table[builtin_function] = hyper_reference
    return table


if __name__ == '__main__':
    import sys
    sys.exit(main())
