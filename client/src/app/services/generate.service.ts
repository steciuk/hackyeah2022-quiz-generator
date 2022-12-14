// @ts-ignore
import FileSaver from 'file-saver';
import { Observable, tap } from 'rxjs';
import { GenerateRequestDTO } from 'src/app/model/GenerateRequestDTO';
import { NumQuestionsService } from 'src/app/services/num-questions.service';
import { SERVER_URL } from 'src/app/services/SERVER_URL';

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class GenerateService {
  constructor(
    private readonly http: HttpClient,
    private readonly numQuestionsService: NumQuestionsService
  ) {}

  generate(sourceUrl: string, title: string): Observable<ArrayBuffer> {
    const request = new GenerateRequestDTO(
      sourceUrl,
      title,
      this.numQuestionsService.getNumQuestions()
    );
    return this.http
      .post(SERVER_URL + 'generate', request, { responseType: 'arraybuffer' })
      .pipe(
        tap((blob) => {
          this.saveFile(blob);
        })
      );
  }

  private saveFile(text: ArrayBuffer) {
    const data = new Blob([text], { type: 'application/pdf;charset=latin-1' });
    FileSaver.saveAs(data, 'ipn-quiz.pdf');
  }
}
