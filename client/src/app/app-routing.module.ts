import { ArticlesComponent } from 'src/app/components/articles/articles.component';
import { DashboardComponent } from 'src/app/components/auth/dashboard/dashboard.component';
import { ForgotPasswordComponent } from 'src/app/components/auth/forgot-password/forgot-password.component';
import { SignInComponent } from 'src/app/components/auth/sign-in/sign-in.component';
import { SignUpComponent } from 'src/app/components/auth/sign-up/sign-up.component';
import { VerifyEmailComponent } from 'src/app/components/auth/verify-email/verify-email.component';
import { HomeComponent } from 'src/app/components/home/home.component';
import { AuthGuard } from 'src/app/services/auth-guard.service';

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'sign-in', component: SignInComponent },
  { path: 'register-user', component: SignUpComponent },
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuard],
  },
  { path: 'forgot-password', component: ForgotPasswordComponent },
  { path: 'verify-email-address', component: VerifyEmailComponent },
  { path: 'articles', component: ArticlesComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
