import { BaseComponent } from 'src/app/components/base.component';
import { ContrastService } from 'src/app/services/contrast.service';

import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-button',
  templateUrl: './button.component.html',
  styleUrls: ['./button.component.scss'],
})
export class ButtonComponent extends BaseComponent implements OnInit {
  @Input() disabled: boolean = false;

  activeColorClass: string = 'bg-blue-100';
  disabledColorClass: string = 'bg-gray-100';

  constructor(private readonly contrastService: ContrastService) {
    super();
  }

  ngOnInit(): void {
    this.subs.sink = this.contrastService.contrast$.subscribe(
      (isHighContrast) => {
        if (isHighContrast) {
          this.activeColorClass = 'bg-yellow-400';
          this.disabledColorClass = 'bg-yellow-200';
        } else {
          this.activeColorClass = 'bg-blue-100';
          this.disabledColorClass = 'bg-gray-100';
        }
      }
    );
  }
}
