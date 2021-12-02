use std::io::{self, BufRead};
use std::collections::VecDeque;

fn main() {
    let mut cnt = 0;
    let stdin = io::stdin();
    let mut prev: VecDeque<u32> = VecDeque::with_capacity(3);
    let mut lines = stdin.lock().lines();
    while let Some(line) = lines.next() {
        let x: u32 = line.unwrap().parse().expect("Failed to parse input");
        if prev.len() == 3 && x > prev.pop_front().unwrap() {
            cnt += 1;
        }
        prev.push_back(x);
    }

    println!("{}", cnt);
}
