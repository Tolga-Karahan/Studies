package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	str_x := strconv.Itoa(x)
	len_str_x := len(str_x)
	is_palindrome := true

	for i := 0; i < len_str_x/2; i = i + 1 {
		if str_x[i] != str_x[len_str_x-i-1] {
			is_palindrome = false
		}
	}

	return is_palindrome
}

func main() {
	an_integer := 1221
	fmt.Println(isPalindrome(an_integer))

	a_string := "abc"
	for _, char := range a_string {
		fmt.Println((char == 'a'))
	}
}
