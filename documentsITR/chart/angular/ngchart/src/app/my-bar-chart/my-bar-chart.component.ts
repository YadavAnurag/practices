import { Component, OnInit, OnDestroy } from '@angular/core';
import { ChartOptions } from 'chart.js';
import { Subscription } from 'rxjs';
import { DataService } from './data.service';

@Component({
  selector: 'app-my-bar-chart',
  templateUrl: './my-bar-chart.component.html',
  styleUrls: ['./my-bar-chart.component.css']
})
export class MyBarChartComponent implements OnInit, OnDestroy {

  // constructor(private dataService: DataService){}
  constructor(){}

  myData:string;
  ngOnInit(){
    
  }
  ngOnDestroy(){

  }


  data: number;

  public barChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true, 
    animation:{
      duration: 250,
      easing: 'linear'
    },
    scales: {
      // xAxes: [{
      //   type: 'time',
      // }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
          stepSize: 1
        }
      }]
    }
  };
  public barChartLabels = ['first', 'second'];

  public barChartType = 'line';
  public barChartLegend = true;
  public barChartDatasets = [
    { data: [48,40,40], 
      label: 'Series A',
      lineTension: 0.1,
      pointRadius: 0,
      fill: false
    },
    // { data: [28, 48, 40, 19, 86, 27, 90, 7], label: 'Series B' }
  ];



  onChartClick(event: MouseEvent): void { }

  onChartHover(event: MouseEvent): void { }

  addData(dataArr: Array<number>, label: string) {
    this.barChartDatasets.forEach((dataset, index) => {
      this.barChartDatasets[index] =
        Object.assign({}, this.barChartDatasets[index], { data: [...this.barChartDatasets[index].data, dataArr[index]] });
    });


    this.barChartLabels = [...this.barChartLabels, label];
  };

  
}

