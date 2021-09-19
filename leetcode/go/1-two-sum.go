func twoSum(nums []int, target int) []int {
    finding_dict := make(map[int]int)
	for i, num := range nums {
        remain := target - num
        if seenIndex, ok := finding_dict[remain]; ok {
            return []int{seenIndex, i}
        }
        finding_dict[num] = i
	}
    return []int{0, 0}
}