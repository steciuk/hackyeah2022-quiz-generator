import { BaseComponent } from 'src/app/components/base.component';
import { Article } from 'src/app/model/Article';
import { GenerateService } from 'src/app/services/generate.service';

import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-article-card',
  templateUrl: './article-card.component.html',
  styleUrls: ['./article-card.component.scss'],
})
export class ArticleCardComponent extends BaseComponent implements OnInit {
  @Input() article!: Article;

  constructor(private readonly generateService: GenerateService) {
    super();
  }

  ngOnInit(): void {}

  generate() {
    this.subs.sink = this.generateService
      .generate(this.article.url, this.article.title)
      .subscribe(() => {
        console.log('Generated');
      });
  }
}
