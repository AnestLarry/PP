package mtgo

import (
	"fmt"
	"strconv"
)

func Input_string(tip string) string {
	temp := ""
	if tip == "" {
		fmt.Scanln(&temp)
		return temp
	} else {
		fmt.Print(tip)
		fmt.Scanln(&temp)
		return temp
	}
}

func Input_int(tip string) int {
	temp := ""
	if tip == "" {
		fmt.Scanln(&temp)
		result, _ := strconv.Atoi(temp)
		return result
	} else {
		fmt.Print(tip)
		fmt.Scanln(&temp)
		result, _ := strconv.Atoi(temp)
		return result

	}
}
