import { Component, OnInit, OnDestroy } from '@angular/core';
import { DataInterface } from '../interfaces/dataInterface';
import { DataService } from '../data-service/data.service';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  firstData:string;
  constructor(private dataService: DataService) { }




  ngOnInit() {
    this.dataService.sendData(this.firstData);
    this.dataService.getData().subscribe(data => {
      console.log(data);
      this.firstData = data['msg'];
      console.log(this.firstData);
    });
  }
  ngOnDestroy() { }

}
