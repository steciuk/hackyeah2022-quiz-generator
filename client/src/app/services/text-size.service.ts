import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class TextSizeService {
  private isTextBig = false;

  constructor() {}

  toggleTextSize() {
    if (this.isTextBig) {
      document.body.style.fontSize = '16px';
      this.isTextBig = false;
    } else {
      document.body.style.fontSize = '20px';
      this.isTextBig = true;
    }
  }
}
