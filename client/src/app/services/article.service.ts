import { Observable } from 'rxjs';
import { Article } from 'src/app/model/Article';
import { SERVER_URL } from 'src/app/services/SERVER_URL';

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ArticleService {
  constructor(private readonly http: HttpClient) {}

  getArticles(query: string): Observable<Article[]> {
    return this.http.get<Article[]>(`${SERVER_URL}search/${query}`);
    // const articles: Article[] = [
    //   {
    //     url: 'https://www.google.com',
    //     title: 'Google',
    //     description:
    //       "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
    //   },
    //   {
    //     url: 'https://www.google.com',
    //     title: 'Google',
    //     description:
    //       "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
    //   },
    //   {
    //     url: 'https://www.google.com',
    //     title: 'Google',
    //     description:
    //       "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
    //   },
    //   {
    //     url: 'https://www.google.com',
    //     title: 'Google',
    //     description:
    //       "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
    //   },
    // ];

    // return of(articles);
  }
}
