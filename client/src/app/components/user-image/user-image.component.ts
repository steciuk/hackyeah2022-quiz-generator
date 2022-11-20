import { AuthService } from 'src/app/services/auth.service';

import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-image',
  templateUrl: './user-image.component.html',
  styleUrls: ['./user-image.component.scss'],
})
export class UserImageComponent implements OnInit {
  @Input() public size = 100;

  constructor(public readonly authService: AuthService) {}

  ngOnInit(): void {}
}
