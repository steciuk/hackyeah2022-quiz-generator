import { BehaviorSubject } from 'rxjs';

import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ContrastService {
  private isHighContrast: boolean = false;
  private contrast = new BehaviorSubject<boolean>(this.isHighContrast);

  toggleContrast() {
    this.isHighContrast = !this.isHighContrast;
    this.contrast.next(this.isHighContrast);
    if (this.isHighContrast) {
      document.body.style.backgroundColor = 'black';
      document.body.style.color = 'white';
    } else {
      document.body.style.backgroundColor = 'white';
      document.body.style.color = 'black';
    }
  }

  get contrast$() {
    return this.contrast.asObservable();
  }
}
