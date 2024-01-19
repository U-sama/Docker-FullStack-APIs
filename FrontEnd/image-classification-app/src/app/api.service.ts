import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})

export class ApiService {
  // private apiUrl = this.router.URL; // Update with your fast API URL or provide a default value


  constructor(private http: HttpClient) { }

  predict(file: File, url: string): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name,);
    console.log(url+ "/predict");
    return this.http.post<any>("/predict", formData);
  }
}
