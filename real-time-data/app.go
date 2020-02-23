package main

import (
	"fmt"

	"github.com/piquette/finance-go/chart"
	"github.com/piquette/finance-go/datetime"
	"github.com/piquette/finance-go/quote"
)

func main() {
	
}

func historic_quotes() {
	params := &chart.Params{
		Symbol:   "TWTR",
		Interval: datetime.OneHour,
	}
	iter := chart.Get(params)

	for iter.Next() {
		fmt.Println(iter.Bar())
	}
	if err := iter.Err(); err != nil {
		fmt.Println(err)
	}
}
