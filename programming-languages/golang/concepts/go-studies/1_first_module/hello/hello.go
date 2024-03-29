package main

import (
	"fmt"
	"log"

	"greetings"
)

func main(){
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	names := []string{
		"Tolga",
		"Mike",
		"Sarah",
	}

	messages, err := greetings.Hellos(names)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(messages)
}	
