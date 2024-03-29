use std::io::{self, BufRead};
use std::str::FromStr;

enum Command {
    Forward(u32),
    Down(u32),
    Up(u32),
}

#[derive(Debug)]
enum CommandParseError {
    InvalidNumberOfTokens,
    InvalidCommand,
    InvalidNumber,
}

impl FromStr for Command {
    type Err = CommandParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let result = if let Some((cmd, number_str)) = s.split_once(' ') {
            match number_str.parse() {
                Ok(number) => match cmd {
                    "forward" => Command::Forward(number),
                    "down" => Command::Down(number),
                    "up" => Command::Up(number),
                    _ => return Result::Err(CommandParseError::InvalidCommand)
                },
                Err(_) => return Result::Err(CommandParseError::InvalidNumber)
            }
        } else {
            return Result::Err(CommandParseError::InvalidNumberOfTokens);
        };
        Ok(result)
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut h = 0;
    let mut d1 = 0;
    let mut d2 = 0;
    let mut aim = 0;
    while let Some(line) = lines.next() {
        let cmd: Command = line.unwrap().parse().unwrap();
        match cmd {
            Command::Forward(x) => {
                h += x;
                d2 += aim * x;
            }
            Command::Up(x) => {
                d1 -= x;
                aim -= x;
            }
            Command::Down(x) => {
                d1 += x;
                aim += x;
            }
        }
    }

    println!("{} {}", h * d1, h * d2);
}