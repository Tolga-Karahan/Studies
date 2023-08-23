package main

import (
	"fmt"
	"strings"
)

func romanToInt(s string) int {
	sum := 0
	substr := ""

	for i := 0; len(s) >= 2; {
		if i+2 > len(s) {
			substr = s[i:]
		} else {
			substr = s[i : i+2]
		}

		if substr == "IV" {
			sum += 4
			s = strings.Replace(s, substr, "", 1)
		} else if substr == "IX" {
			sum += 9
			s = strings.Replace(s, substr, "", 1)
		} else if substr == "XL" {
			sum += 40
			s = strings.Replace(s, substr, "", 1)
		} else if substr == "XC" {
			sum += 90
			s = strings.Replace(s, substr, "", 1)
		} else if substr == "CD" {
			sum += 400
			s = strings.Replace(s, substr, "", 1)
		} else if substr == "CM" {
			sum += 900
			s = strings.Replace(s, substr, "", 1)
		} else {
			i++
		}

		if i == len(s) {
			break
		}
	}

	for i := 0; i <= len(s)-1; i++ {
		substr := s[i : i+1]

		if substr == "I" {
			sum += 1
		} else if substr == "V" {
			sum += 5
		} else if substr == "X" {
			sum += 10
		} else if substr == "L" {
			sum += 50
		} else if substr == "C" {
			sum += 100
		} else if substr == "D" {
			sum += 500
		} else if substr == "M" {
			sum += 1000
		}
	}

	return sum
}

func main() {
	fmt.Println(romanToInt("MCMXCIV"))
	fmt.Println(romanToInt("CIV"))
	fmt.Println(romanToInt("CMXC"))
	fmt.Println(romanToInt("DCXXI"))
}
