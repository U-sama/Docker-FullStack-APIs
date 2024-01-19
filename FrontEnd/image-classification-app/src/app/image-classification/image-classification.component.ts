import { Component, Inject } from '@angular/core';
import { ApiService } from '../api.service';
import { DOCUMENT } from '@angular/common';




@Component({
  selector: 'app-image-classification',
  templateUrl: './image-classification.component.html',
  styleUrls: ['./image-classification.component.css']
})
export class ImageClassificationComponent {
  selectedFile: File | null = null;
  imageUrl: string | null = null;
  prediction: any | null = null;

  constructor(private apiService: ApiService, @Inject(DOCUMENT) private document: any) { }

  onFileSelected(event: any): void {
    // Reset prediction information
    this.prediction = null;
    this.selectedFile = event.target.files[0];

    // Display the selected image
    this.imageUrl = this.selectedFile ? URL.createObjectURL(this.selectedFile) : null;
  }

  onPredict(): void {
    if (this.selectedFile) {
      this.apiService.predict(this.selectedFile, this.document.location.hostname)
        .subscribe(
          result => {
            this.prediction = result;
            // Display the selected image and predicted label
            this.imageUrl = this.selectedFile ? URL.createObjectURL(this.selectedFile) : null;
          },
          error => console.error('Error:', error)
        );
    }
  }
}
