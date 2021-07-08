import "strconv"

func reverse(x int) int {
	var output string
	input := x

	if x < 0 {
		x = x * -1
	}
    
	for _ = 0; x != 0; x = x / 10 {
        output = output + strconv.Itoa(x % 10)
	}
    
    i, _ := strconv.Atoi(output)

    if i > 2147483648 {
    	return 0
    }
	if input < 0 {
		return i / -1
	}
	return i
}