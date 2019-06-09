import { Component, OnInit, OnDestroy } from '@angular/core';
import { ChartOptions } from 'chart.js';

@Component({
  selector: 'app-my-bar-chart',
  templateUrl: './my-bar-chart.component.html',
  styleUrls: ['./my-bar-chart.component.css']
})
export class MyBarChartComponent implements OnInit {

  id: any;
  constructor() { }


  public barChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true, 
    animation:{
      duration: 250,
      easing: 'linear'
    },
    scales: {
      xAxes: [{
        type: 'time',
      }]
    }
  };
  public barChartLabels = [];

  public barChartType = 'line';
  public barChartLegend = true;
  public barChartDatasets = [
    { data: [], 
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

  ngOnInit() {
    this.id = setInterval(() => {
      this.addData([Math.sin(Math.PI*(0.5-Math.random()))], new Date().toLocaleString());
    }, 500);
  }

  ngOnDestroy() {
    if (this.id) {
      clearInterval(this.id);
    }
  }
}