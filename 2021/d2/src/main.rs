use std::io::{self, BufRead};
use std::num::ParseIntError;
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
        let mut tokens = s.split(' ');
        let cmd: Command = if let Some(cmd) = tokens.next() {
            if let Some(amount_str) = tokens.next() {
                let amount: Result<u32, ParseIntError> = amount_str.parse();
                if amount.is_ok() {
                    match cmd {
                        "forward" => Command::Forward(amount.unwrap()),
                        "down" => Command::Down(amount.unwrap()),
                        "up" => Command::Up(amount.unwrap()),
                        _ => return Result::Err(CommandParseError::InvalidCommand),
                    }
                } else {
                    return Result::Err(CommandParseError::InvalidNumber);
                }
            } else {
                return Result::Err(CommandParseError::InvalidNumberOfTokens);
            }
        } else {
            return Result::Err(CommandParseError::InvalidNumberOfTokens);
        };
        return Result::Ok(cmd);
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