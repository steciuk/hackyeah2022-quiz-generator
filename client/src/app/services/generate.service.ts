import { Observable } from 'rxjs';
import { GenerateRequestDTO } from 'src/app/model/GenerateRequestDTO';
import { SERVER_URL } from 'src/app/services/SERVER_URL';

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class GenerateService {
  constructor(private readonly http: HttpClient) {}

  generate(sourceUrl: string, title: string): Observable<void> {
    const request = new GenerateRequestDTO(sourceUrl, title);
    return this.http.post<void>(SERVER_URL + 'generate', request);
  }
}
