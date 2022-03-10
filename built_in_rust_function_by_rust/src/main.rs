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
    for element in elements {
        function_name = element.text().next().unwrap();

        function_url = format!(
            "{}{}",
            "https://doc.rust-lang.org/std/",
            element.value().attr("href").unwrap()
        );

        output_to_html.push_str(&format!("{} : {}\n", function_name, function_url));
        println!("{} : {}", function_name, function_url);
    }

    let mut file = File::create("RustBuiltInFunction.html").unwrap();
    write!(file, "{}", output_to_html).unwrap();
    file.flush().unwrap();
}
