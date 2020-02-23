package main

import (
	"fmt"
)

func main() {
	q, err := quote.Get("AAPL")
	if err != nil {
		// Uh-oh.
		panic(err)
	}

	// Success!
	fmt.Println(q)
}

func quote() {

}
