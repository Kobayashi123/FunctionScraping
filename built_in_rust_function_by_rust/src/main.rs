use reqwest;
use scraper::{Html, Selector};
use std::fs::File;
use std::io::Write;

fn main() {
    let selector = Selector::parse("div.item-left > a.primitive").unwrap();

    let body = reqwest::blocking::get("https://doc.rust-lang.org/std/index.html")
        .unwrap()
        .text()
        .unwrap();

    let document = Html::parse_document(&body);

    let elements = document.select(&selector);

    let mut function_url;
    let mut function_name;

    let mut output_to_html = String::new();
    output_to_html.push_str(head_part());
    for element in elements {
        function_name = element.text().next().unwrap();

        function_url = format!(
            "{}{}",
            "https://doc.rust-lang.org/std/",
            element.value().attr("href").unwrap()
        );

        output_to_html.push_str(&format!(
            "            {} : {}\n",
            function_name, function_url
        ));
        println!("{} : {}", function_name, function_url);
    }
    output_to_html.push_str(foot_part());

    let mut file = File::create("RustBuiltInFunction.html").unwrap();
    write!(file, "{}", output_to_html).unwrap();
    file.flush().unwrap();
}

fn head_part() -> &'static str {
    //静的ライフタイムにしている
    //ライフタイムを考える必要あり
    return r#"<!DOCTYPE html>
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
"#;
}

fn foot_part() -> &'static str {
    //静的ライフタイムにしている
    //ライフタイムを考える必要あり
    return r#"        </div>
    </body>
</html>"#;
}
