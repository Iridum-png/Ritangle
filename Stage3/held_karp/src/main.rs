use std::collections::HashMap;

fn held_karp(distances: &Vec<Vec<f64>>) -> Vec<usize> {
    let n = distances.len();

    // Initialize the distance matrix
    let mut dp = vec![vec![std::f64::INFINITY; 1 << n]; n];
    for i in 0..n {
        dp[i][1 << i] = 0.0;
    }

    // Initialize the parent matrix
    let mut parent = vec![vec![0; 1 << n]; n];

    // Iterate over the subsets of cities
    for i in 0..(1 << n) {
        // Check if the subset contains at least two cities
        if i.count_ones() < 2 {
            continue;
        }

        // Iterate over the cities in the subset
        for j in 0..n {
            // Check if the city is in the subset
            if (i & (1 << j)) == 0 {
                continue;
            }

            // Iterate over the cities not in the subset
            for k in 0..n {
                // Check if the city is in the subset
                if (i & (1 << k)) != 0 {
                    continue;
                }

                // Calculate the distance of the new path
                let mut distance = dp[k][i ^ (1 << j)] + distances[k][j];

                // Update the distance and parent if the new path is better
                if distance < dp[j][i] {
                    dp[j][i] = distance;
                    parent[j][i] = k;
                }
            }
        }
    }

    // Initialize the minimum distance and the last city
    let mut min_distance = std::f64::INFINITY;
    let mut last_city = 0;

    // Iterate over the cities to find the minimum distance and last city
    for i in 0..n {
        if dp[i][(1 << n) - 1] < min_distance {
            min_distance = dp[i][(1 << n) - 1];
            last_city = i;
        }
    }

    return parent;
}

fn main() {
    let distances = vec![
        vec![0.0, 20.0, 42.0, 35.0],
        vec![20.0, 0.0, 30.0, 34.0],
        vec![42.0, 30.0, 0.0, 12.0],
        vec![35.0, 34.0, 12.0, 0.0],
    ];

    let path = held_karp(&distances);
    println!("{:?}", path);
}