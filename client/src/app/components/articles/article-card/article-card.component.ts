import { Article } from 'src/app/model/Article';
import { GenerateService } from 'src/app/services/generate.service';

import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-article-card',
  templateUrl: './article-card.component.html',
  styleUrls: ['./article-card.component.scss'],
})
export class ArticleCardComponent implements OnInit {
  @Input() article!: Article;

  constructor(private readonly generateService: GenerateService) {}

  ngOnInit(): void {}

  generate() {
    this.generateService
      .generate(this.article.url, this.article.title)
      .subscribe(() => {
        console.log('Generated');
      });
  }
}
