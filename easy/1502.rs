impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        arr.sort();
        let diff = arr[1] - arr[0];
        arr.windows(2).all(|chunk| chunk[1] - chunk[0] == diff)
    }
}
