import { Article } from 'src/app/model/Article';
import { ArticleService } from 'src/app/services/article.service';

import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-articles',
  templateUrl: './articles.component.html',
  styleUrls: ['./articles.component.scss'],
})
export class ArticlesComponent implements OnInit {
  query = new FormControl('');
  articles: Article[] = [];

  constructor(private readonly articleService: ArticleService) {}

  ngOnInit(): void {}

  search() {
    this.articleService.getArticles(this.query.value).subscribe((articles) => {
      this.articles = articles;
    });
  }
}
