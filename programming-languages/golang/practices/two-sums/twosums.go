func twoSum(nums []int, target int) []int {
    for i:=0; i < len(nums)-1; i++ {
        first_elem := nums[i]
        for j:=i+1; j < len(nums); j++ {
            second_elem := nums[j]
            if (first_elem + second_elem) == target {
                return []int{i, j}
            }
        }
    }
    return []int{}
}