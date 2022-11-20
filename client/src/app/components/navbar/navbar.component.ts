import { AuthService } from 'src/app/services/auth.service';

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  navRoutes = ['', 'articles'];
  navLabels = ['Home', 'Generate'];

  constructor(
    public readonly authService: AuthService,
    private readonly router: Router
  ) {}

  ngOnInit(): void {}

  goToArticles() {
    if (this.authService.isLoggedIn) {
      this.router.navigate(['articles']);
    }
  }
}
