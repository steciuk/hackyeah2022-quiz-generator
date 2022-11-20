import { BaseComponent } from 'src/app/components/base.component';
import { Article } from 'src/app/model/Article';
import { GenerateService } from 'src/app/services/generate.service';

import { Component, Input, OnInit, Output } from '@angular/core';
import { ContrastService } from 'src/app/services/contrast.service';

@Component({
  selector: 'app-article-card',
  templateUrl: './article-card.component.html',
  styleUrls: ['./article-card.component.scss']
})
export class ArticleCardComponent extends BaseComponent implements OnInit {
  @Input() article!: Article;

  isLoading: boolean = false;
  highContrastColorClass: string = ''

  constructor(
    private readonly generateService: GenerateService, 
    private readonly contrastService: ContrastService
  ) {
    super();
  }

  ngOnInit(): void {
    this.subs.add(this.contrastService.contrast$.subscribe((isHighContrast) => {
          console.log('isHighContrast', isHighContrast)
          if (isHighContrast) {
            this.highContrastColorClass = 'hover:bg-yellow-400 hover:text-black';
          } else {
            this.highContrastColorClass = '';
          }
        }
      ));
  }

  generate() {
    this.isLoading = true

    this.subs.add(this.generateService
      .generate(this.article.url, this.article.title)
      .subscribe(() => {
        this.isLoading = false;
        console.log('Generated');
      }));
  }
}
