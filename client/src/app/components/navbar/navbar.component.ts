import { BaseComponent } from 'src/app/components/base.component';
import { AuthService } from 'src/app/services/auth.service';
import { ContrastService } from 'src/app/services/contrast.service';

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent extends BaseComponent implements OnInit {
  navRoutes = ['', 'articles'];
  navLabels = ['Home', 'Generate'];

  inverted = false;

  constructor(
    public readonly authService: AuthService,
    public readonly contrastService: ContrastService,
    private readonly router: Router
  ) {
    super();
  }

  ngOnInit(): void {
    this.subs.sink = this.contrastService.contrast$.subscribe(
      (isHighContrast) => {
        this.inverted = isHighContrast;
      }
    );
  }

  goToArticles() {
    if (this.authService.isLoggedIn) {
      this.router.navigate(['articles']);
    }
  }
}
