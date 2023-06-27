func twoSum(nums []int, target int) []int {
    dict := make(map[int][]int)

    for i, v := range nums {
        if _, ok := dict[v]; !ok {
            dict[v] = []int{i}
        } else {
            dict[v] = append(dict[v], i)
        }
    }

    for _, v := range nums {
        i := dict[v][0]

        if indices, ok := dict[target - v]; ok {
            j := indices[0]
            if len(indices) > 1 {
                j = indices[1]
            }

            if i != j{
                return []int{i, j}
            }
        }   
    }

    return []int{}
}