func lengthOfLongestSubstring(s string) int {
    j, start, end, max := 0, 0, 0, 0

    for i := 0; i < len(s); i++ {
        repeat := false
        for j = start; j < end && repeat == false; j++ {
            repeat = (s[i] == s[j])
        }

        if repeat {
            start = j
        }

        end++

        if end - start > max {
            max = end - start
        }
    }

    return max
}