package mtgo

import (
	"os"
	"path/filepath"
)

func WriteFileByBytes(writedata []byte, filename string) bool {
	f, e := os.OpenFile(filename, os.O_CREATE|os.O_TRUNC|os.O_RDWR, 0666)
	if e == nil {
		f.Write(writedata)
		defer f.Close()
		return true
	} else {
		defer f.Close()
		return false
	}
}

func GetAllFileName(path string) string {
	result := ""
	filepath.Walk(path,
		func(path string, f os.FileInfo, err error) error {
			if f == nil {
				return err
			}
			if f.IsDir() {
				return nil
			}
			result += "file:" + path + "\n"
			return nil
		})
	return result
}
