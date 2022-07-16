func longestCommonPrefix(strs []string) string {
    var common = ""

	for i := 0; i < len(strs[0]); i++ {
		for j := 0; j < len(strs); j++ {
			if i >= len(strs[j]) || strs[j][i] != strs[0][i] {
				return common
			}
		}
		common += string(strs[0][i])
	}

	return common
}