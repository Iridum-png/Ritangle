// with open('primes.txt', 'r') as f:
//     primes = [int(x) for x in f.read().split() if len(x) == 5]
    
// for a in range(1, 10000):
//     for b in range(1, a):
//         if str(a-b) + str(a+b) in primes:
//             print(str(a-b)+str(a+b))
//             exit()

// use std::env;
use std::fs;

fn main() {
    let contents = fs::read_to_string(r"C:\Users\ed9ba\Documents\Coding\Python\Ritangle\primes.txt").expect("Something went wrong reading the file");
    let mut primes: Vec<u16> = Vec::new();
    for num in contents.split("\n") {
        if num.len() == 5 {
            primes.push(num.parse::<u16>().unwrap());
        }
    }
    println!("With text:\n{:?}", primes);
}
