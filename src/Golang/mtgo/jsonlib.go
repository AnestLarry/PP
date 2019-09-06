package mtgo

import "encoding/json"

func Loads(jsonstr string) map[string]interface{} {
	var result map[string]interface{}
	json.Unmarshal([]byte(jsonstr), &result)
	return result
}

func dumps(dict map[string]interface{}) string {
	return "Not now.."
}
