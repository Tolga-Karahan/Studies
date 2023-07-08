package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func rot13sub(char rune) rune {
    if char >= 65 && char <= 90 {
		sub := char + 13
		if sub > 90 {
			sub = 65 + (sub % 90) - 1
		}
		return sub
	} else if char >= 97 && char <= 122 {
		sub := char + 13
		if sub > 122 {
			sub = 97 + (sub % 122) - 1
		}
		return sub
	} else {
		return 32
	}
}

func (v rot13Reader) Read (buff []byte) (int, error) {
	inter_buff := make([]byte, 8)
	nBytes, err := v.r.Read(inter_buff)
	
	if err == nil { 
		for i, val := range inter_buff {
			buff[i] = byte(rot13sub(rune(val)))
		}
		return nBytes, nil
	} else {
		return 0, nil
	}
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}