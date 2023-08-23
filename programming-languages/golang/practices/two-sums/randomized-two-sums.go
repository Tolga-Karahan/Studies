import "math/rand"

func twoSum(nums []int, target int) []int {
    for {
        i := rand.Intn(len(nums))
        j := rand.Intn(len(nums))

        if (nums[i] + nums[j] == target && i != j) {
            return []int{i, j}
        }
    }
    return []int{}
}
