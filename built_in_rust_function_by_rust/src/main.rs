use reqwest;
//use scraper::{Html, Selector};
use std::fs::File;
//use std::io::{self, prelude::*, Write};
use std::io::Write;

fn main() {
    let body = reqwest::blocking::get("https://doc.rust-lang.org/std/index.html")
        .unwrap()
        .text()
        .unwrap();

    let mut file = File::create("RustBuiltInFunction.html").unwrap();
    let str = String::from(body);

    write!(file, "{}", str).unwrap();
    file.flush().unwrap();
}
