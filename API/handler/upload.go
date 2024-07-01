package handler

import (
	"io"
	"net/http"
	"os"
	"path/filepath"
)

const (
	UPLOAD_DIR = "./uploads"
)

func UploadHandler(w http.ResponseWriter, r *http.Request) {
	// Parse the multipart form, with a maximum upload size of 10 MB
	err := r.ParseMultipartForm(10 << 20)
	if err != nil {
		http.Error(w, "Unable to parse form", http.StatusBadRequest)
		return
	}

	// Retrieve the file from form data
	file, handler, err := r.FormFile("image")
	if err != nil {
		http.Error(w, "Unable to retrieve file", http.StatusBadRequest)
		return
	}
	defer file.Close()

	// Create the uploads directory if it doesn't exist
	if _, err := os.Stat(UPLOAD_DIR); os.IsNotExist(err) {
		err = os.MkdirAll(UPLOAD_DIR, os.ModePerm)
		if err != nil {
			http.Error(w, "Unable to create uploads directory", http.StatusInternalServerError)
			return
		}
	}

	// Create a destination file
	dst, err := os.Create(filepath.Join(UPLOAD_DIR, handler.Filename))
	if err != nil {
		http.Error(w, "Unable to create destination file", http.StatusInternalServerError)
		return
	}
	defer dst.Close()

	// Copy the uploaded file to the destination file
	if _, err := io.Copy(dst, file); err != nil {
		http.Error(w, "Unable to save file", http.StatusInternalServerError)
		return
	}

	// Return success message
	w.Write([]byte("File uploaded successfully"))
}
