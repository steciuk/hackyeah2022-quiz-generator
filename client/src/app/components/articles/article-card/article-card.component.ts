import { BaseComponent } from 'src/app/components/base.component';
import { Article } from 'src/app/model/Article';
import { GenerateService } from 'src/app/services/generate.service';

import { Component, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-article-card',
  templateUrl: './article-card.component.html',
  styleUrls: ['./article-card.component.scss']
})
export class ArticleCardComponent extends BaseComponent implements OnInit {
  @Input() article!: Article;

  isLoading: boolean = false;

  constructor(private readonly generateService: GenerateService) {
    super();
  }

  ngOnInit(): void {}

  generate() {
    this.isLoading = true

    this.subs.sink = this.generateService
      .generate(this.article.url, this.article.title)
      .sub
