func fib(n int) int {
    if n <= 1 {
        return n
    } else {
        return fib(n - 1) + fib(n - 2)
    }
    
    // Second method
    // a, b := 0, 1

	// for i := 0; i < n; i++ {
	// 	b, a = a + b, b
	// }

	// return a
}