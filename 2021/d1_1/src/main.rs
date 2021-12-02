use std::io::{self, BufRead};

fn main() {
    let mut cnt = 0;
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut prev: i32 = lines.next().unwrap().unwrap().parse().expect("Failed to parse first line");
    while let Some(line) = lines.next() {
        let x: i32 = line.unwrap().parse().expect("Failed to parse input");
        if x > prev {
            cnt += 1;
        }
        prev = x;
    }

    println!("{}", cnt);
}
