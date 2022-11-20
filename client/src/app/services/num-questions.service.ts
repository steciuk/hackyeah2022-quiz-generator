import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class NumQuestionsService {
  numQuestions: number = 10;

  constructor() {}

  setNumQuestions(numQuestions: number) {
    this.numQuestions = numQuestions;
  }

  getNumQuestions() {
    return this.numQuestions;
  }
}
