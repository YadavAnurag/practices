import { Component, OnInit, OnDestroy } from '@angular/core';
import { DataInterface } from '../interfaces/dataInterface';
import { DataService } from '../data-service/data.service';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { Label, Color } from 'ng2-charts';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  x: number;
  y: number;
  constructor(private dataService: DataService) { }


  
  public lineChartData: ChartDataSets[] = [
    { data: [], label: 'Series A' },
    { data: [-3, -5, 5, 50, -15, 20, 12, 56, 6,3,1], label: 'Series B' },
  ];
  public lineChartLabels: Label[ ] = ['0', '3','7','11','15', '19','23', '27', '31', '35', '39'];  
  public lineChartOptions: ChartOptions = {
    responsive: true, 
    scales: {
      xAxes: [{
        display: true,
        ticks: {
          beginAtZero: true,
          max: 150,
          min: -150,
          stepSize: 10

        }
      }],
      yAxes: [{
        display: true,
        ticks: {
          beginAtZero: true,
            stepSize:5,
            max: 150,
            min: -150
        }
      }]
    }
  };
  public lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0,0.3)',
    },
  ];

  
  public lineChartLegend = true;
  public lineChartType = 'line';

  // addData(dataArr: Array<number>, label: number) {
  //   this.lineChartData.forEach((dataset, index) => {
  //     this.lineChartData[index] =
  //       Object.assign({}, this.lineChartData[index], { data: [...this.lineChartData[index].data, dataArr[index]] });
  //   });

  //   this.lineChartLabels = [...this.lineChartLabels, label];
  // };


  ngOnInit() {
    this.dataService.getData().subscribe(serverData => {
      console.log(serverData);
      this.x = serverData['x'];
      this.y = serverData['y'];
      // this.addData([this.first], this.second);
      this.lineChartData[0].data.push(this.y);
      //this.lineChartLabels.push(this.x.toString());
      console.log(serverData);
    });
  }
  ngOnDestroy() {
    console.log('completed');
  }
}

