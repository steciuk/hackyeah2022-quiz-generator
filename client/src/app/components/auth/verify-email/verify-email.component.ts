import { AuthService } from 'src/app/services/auth.service';

import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-verify-email',
  templateUrl: './verify-email.component.html',
  styleUrls: ['./verify-email.component.scss'],
})
export class VerifyEmailComponent implements OnInit {
  constructor(public readonly authService: AuthService) {}
  ngOnInit() {}
}
