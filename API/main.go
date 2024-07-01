package main

import (
	"API/handler"
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/upload", handler.UploadHandler)

	fmt.Println("Server started at http://127.0.0.1:8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Error starting server:", err)
	}
}
