//use reqwest;
//use scraper::{Html, Selector};
use std::fs::File;
//use std::io::{self, prelude::*, Write};
use std::io::Write;

fn main() {
    let mut file = File::create("RustBuiltInFunction.html").unwrap();
    let str = String::from("temporary string");

    write!(file, "{}", str).unwrap();
    file.flush().unwrap();
}
