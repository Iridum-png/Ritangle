use std::f32;

fn p_inverse(x: u8) -> u8 {
    180 * (1 - x / 10)
}

fn main() {
    let point = vec![9, 8, 7, 6, 5, 4, 3];
    let mut angles = Vec::new();
    let mut length: f32 = 1.0;
    let mut prev = 0.0;

    for i in 0..point.len() {
        angles.push(p_inverse(point[i]));
    }

    // for angle in angles:
    //     x = angle - (prev/2)
    //     length += 1/cos(x * (pi/180))
    //     prev = angle

    for i in 0..angles.len() {
        let angle: f32 = angles[i].into();
        let x: f32 = prev / 2.0;
        length += 1.0 / (angle - x).cos();
        prev = angle;
        println!("({}, {})", length, length * 0.74);
    }
}
