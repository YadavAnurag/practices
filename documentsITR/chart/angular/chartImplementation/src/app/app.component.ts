import { Component, OnInit, OnDestroy } from '@angular/core';
import { DataService } from './data-service/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'chartImplementation';

  constructor(private dataService: DataService) { }

  ngOnInit() { }
  ngOnDestroy() { }
}
