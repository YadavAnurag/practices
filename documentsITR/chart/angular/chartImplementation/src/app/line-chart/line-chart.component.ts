import { Component, OnInit, OnDestroy } from '@angular/core';
import { DataInterface } from '../interfaces/dataInterface';
import { DataService } from '../data-service/data.service';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  first: number;
  second: number;
  constructor(private dataService: DataService) { }


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


  ngOnInit() {
    // this.dataService.sendData(this.first);
    this.dataService.getData().subscribe(data => {
      console.log(data);
      this.first = data['first'];
      this.second = data['second'];
      this.addData([this.first], this.second.toString());
      console.log(data);
    });
  }
  ngOnDestroy() {
    console.log('completed');
  }
}

