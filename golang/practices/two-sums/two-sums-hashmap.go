func twoSum(nums []int, target int) []int {
    numIndices := make(map[int]int)
    
    for i, num := range nums {
        complement := target - num
        
        if idx, ok := numIndices[complement]; ok {
            return []int{idx, i}
        }
        
        numIndices[num] = i
    }
    
    return []int{}
}