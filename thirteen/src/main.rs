fn g(x_vals: Vec<i32>) {
    let floor = -200;
    let ceil = 200;
    for a in floor..ceil {
        for b in floor..ceil {
            for c in floor..ceil {
                for d in floor..ceil {
                    let mut count = 0;
                    for x in &x_vals {
                        if (x.pow(2) + c * x + d).abs() == a * x + b {
                            count += 1;
                        }
                        if count == 4 {
                            println!("{} {} {} {}", a, b, c, d);
                            println!("{}", a.pow(2) + b.pow(2) + c.pow(2) + d.pow(2));
                            println!(
                                "{}",
                                (a.pow(2) + b.pow(2) + c.pow(2) + d.pow(2)) as f32 * 0.054
                            );
                        }
                    }
                }
            }
        }
        println!("{}", a);
    }
}

fn main() {
    let x_vals = vec![1, 4, 9, 16];
    g(x_vals);
}
