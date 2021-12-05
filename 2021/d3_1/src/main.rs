use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut one_counts = Vec::new();
    let mut total_count = 0;
    while let Some(line) = lines.next() {
        let num_str = line.unwrap();
        if one_counts.is_empty() {
            one_counts = vec![0;num_str.len()];
        }
        for (i, c) in num_str.chars().enumerate() {
            if c == '1' {
                one_counts[i] += 1
            }
        }
        total_count += 1;
    }
    let mut gamma_bin_str = "".to_owned();
    let mut epsilon_bin_str = "".to_owned();
    for one_count in one_counts {
        if one_count*2 > total_count {
            gamma_bin_str += "1";
            epsilon_bin_str += "0";
        } else {
            gamma_bin_str += "0";
            epsilon_bin_str += "1";
        }
    }
    let gamma = i32::from_str_radix(&gamma_bin_str, 2).unwrap();
    let eps = i32::from_str_radix(&epsilon_bin_str, 2).unwrap();
    println!("{} {} {}", &gamma_bin_str, &epsilon_bin_str, gamma*eps);
}
