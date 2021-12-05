use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut numbers: HashSet<String> = HashSet::new(); // I'm assuming no duplicate entries
    while let Some(line) = lines.next() {
        let num_str = line.unwrap();
        let prev = numbers.replace(num_str);
        assert!(prev.is_none()); // ensure there are no duplicates
    }
    let digit_cnt = numbers.iter().next().unwrap().len();

    let o2_rating = calc_rating(&mut numbers.clone(), digit_cnt,
                                |ones, total| ones * 2 >= total);
    let co2_rating = calc_rating(&mut numbers, digit_cnt,
                                 |ones, total| ones * 2 < total);

    println!("{}", o2_rating * co2_rating);
}

fn calc_rating(numbers: &mut HashSet<String>, digit_cnt: usize, keep_ones_if: fn(ones: u32, total: u32) -> bool) -> i32 {
    for pos in 0..digit_cnt {
        if keep_ones_if(count_ones(numbers, pos), numbers.len() as u32) {
            numbers.retain(|n| n.as_bytes()[pos] == b'1');
        } else {
            numbers.retain(|n| n.as_bytes()[pos] == b'0');
        }
        if numbers.len() == 1 {
            break;
        }
    }
    i32::from_str_radix(numbers.iter().next().unwrap(), 2).unwrap()
}

fn count_ones(numbers: &HashSet<String>, pos: usize) -> u32 {
    let mut count = 0;
    for num in numbers {
        if num.as_bytes()[pos] == b'1' {
            count += 1
        }
    }
    count
}
