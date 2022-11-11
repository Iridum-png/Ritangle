// a to j are the digits from 0 to 9 in some order.
// (a) % 1 == 0
// (a*10 + b) % 2 == 0
// (a*100 + b*10 + c) % 3 == 0
// (a*1000 + b*100 + c*10 + d) % 4 == 0
// (a*10000 + b*1000 + c*100 + d*10 + e) % 5 == 0
// (a*100000 + b*10000 + c*1000 + d*100 + e*10 + f) % 6 == 0
// (a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 + g) % 7 == 0
// (a*10000000 + b*1000000 + c*100000 + d*10000 + e*1000 + f*100 + g*10 + h) % 8 == 0
// (a*100000000 + b*10000000 + c*1000000 + d*100000 + e*10000 + f*1000 + g*100 + h*10 + i) % 9 == 0
// (a*1000000000 + b*100000000 + c*10000000 + d*1000000 + e*100000 + f*10000 + g*1000 + h*100 + i*10 + j) % 10 == 0
// Each number must be a unique digit from 0-9

use std::process::exit;

fn main() {
    println!("HH");
    let e: u64 = 5;
    let j: u64 = 0;
    let even: Vec<u64> = vec![2, 4, 6, 8];
    let odd: Vec<u64> = vec![1, 3, 7, 9];

    for a in &odd {
        println!("{}", a);
        for b in &even {
            println!("{}{}", a, b);
            for c in &odd {
                if (a + b + c) % 3 != 0 {
                    continue;
                }
                println!("{}{}{}", a, b, c);
                for d in &even {
                    if (a * 1000 + b * 100 + c * 10 + d) % 4 != 0 {
                        continue;
                    }
                    println!("{}{}{}{}", a, b, c, d);
                    for f in &even {
                        if (a * 100000 + b * 10000 + c * 1000 + d * 100 + 50 + f) % 6 != 0 {
                            continue;
                        }
                        println!("{}{}{}{}{}{}", a, b, c, d, e, f);
                        for g in &odd {
                            if (a * 1000000
                                + b * 100000
                                + c * 10000
                                + d * 1000
                                + e * 100
                                + f * 10
                                + g)
                                % 7
                                != 0
                            {
                                continue;
                            }
                            println!("{}{}{}{}{}{}{}", a, b, c, d, e, f, g);
                            for h in &even {
                                if (a * 10000000
                                    + b * 1000000
                                    + c * 100000
                                    + d * 10000
                                    + e * 1000
                                    + f * 100
                                    + g * 10
                                    + h)
                                    % 8
                                    != 0
                                {
                                    continue;
                                }
                                for i in &odd {
                                    if (a * 100000000
                                        + b * 10000000
                                        + c * 1000000
                                        + d * 100000
                                        + e * 10000
                                        + f * 1000
                                        + g * 100
                                        + h * 10
                                        + i)
                                        % 9
                                        != 0
                                    {
                                        continue;
                                    }
                                    println!("{}{}{}{}{}{}{}{}{}{}", a, b, c, d, e, f, g, h, i, j,);
                                    exit(0);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
