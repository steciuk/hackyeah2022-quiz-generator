import { AuthService } from 'src/app/services/auth.service';

import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  navRoutes = ['articles'];
  navLabels = ['Articles'];

  constructor(public readonly authService: AuthService) {}

  ngOnInit(): void {}
}
