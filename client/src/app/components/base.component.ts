import { SubSink } from 'subsink';

import { ChangeDetectionStrategy, Component, OnDestroy } from '@angular/core';

@Component({
  template: '',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export abstract class BaseComponent implements OnDestroy {
  protected subs = new SubSink();

  protected finalize(): void {}

  ngOnDestroy(): REQUIRED_SUPER {
    this.finalize();
    this.subs.unsubscribe();
    return new REQUIRED_SUPER();
  }
}

class REQUIRED_SUPER {}
