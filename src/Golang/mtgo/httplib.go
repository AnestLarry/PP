package mtgo

import (
	"io/ioutil"
	"net/http"
)

func Temp_Get_Byte(url string) []byte {
	resp, e := http.Get(url)
	if e == nil {
		return_byte, _ := ioutil.ReadAll(resp.Body)
		return return_byte
	} else {
		return nil
	}
}
