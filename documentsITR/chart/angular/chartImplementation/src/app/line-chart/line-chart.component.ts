import { Component, OnInit, OnDestroy, ViewChild } from '@angular/core';
import { DataInterface } from '../interfaces/dataInterface';
import { DataService } from '../data-service/data.service';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { Label, Color, BaseChartDirective } from 'ng2-charts';



@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  @ViewChild(BaseChartDirective, { static: false }) chart: BaseChartDirective;

  x: number;
  y: number;
  dataLength: number = 15;

  xmax: number = 2207000;
  xmin: number = 0;

  ymax: number = 1006367;
  ymin: number = -1000;

  constructor(private dataService: DataService) { }


  public lineChartData: ChartDataSets[] = [
    { data: [], borderWidth: 0.5, fill: false, borderColor: 'red', lineTension: 0, label: 'Real-Time Data' },
    { data: [], borderWidth: 0.5, fill: false, borderColor: 'blue', lineTension: 0, label: 'Nominal Data' },
  ];
  public lineChartLabels: Label[] = [];
  public lineChartOptions: ChartOptions = {
    animation: {
      duration: 0
    },
    responsive: true,
    elements: {
      point: {
        radius: 1
      }
    },

    scales: {
      xAxes: [{
        display: true,
        ticks: {
          max: this.xmax,
          min: this.xmin,

        }
      }],
      yAxes: [{
        display: true,
        ticks: {
          max: this.ymax,
          min: this.ymin
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


  ngOnInit() { }
  ngOnDestroy() { }


  getNominalData() {

    this.dataService.getNominalData().subscribe(serverData => {
      console.log(`${this.j}th`);
      this.x = serverData['x'];
      this.y = serverData['y'];
      this.lineChartData[1].data.push(this.y);
      this.lineChartLabels.push(this.x.toString());


    });

    this.dataService.getCompletionMessage().subscribe(serverData => {
      console.log('client: All nominal data has been received');
    });

  }

  j = 0
  d = new Date();
  e = new Date();
  total: any;
  getRealTimeData() {
    // this.d = new Date();
    this.j = 0
    this.dataService.getRealTimeData().subscribe(serverData => {
      //console.log(`server: realtime data ${serverData['x']}, ${serverData['y']}`);
      // this.x = serverData['x'];
      // this.y = serverData['y'];
      this.lineChartData[0].data.push(serverData['y']);
      //this.lineChartLabels.push(this.x.toString());
      this.chart.chart.update();

      // this.e = new Date();
      // this.total = <any>this.d - <any>this.e;
      // console.log('time ', (this.total) / 1000);
      console.log(this.j);

      this.j += 1;
    });

    this.dataService.getCompletionMessage().subscribe(serverData => {
      this.e = new Date();
      this.total = <any>this.d - <any>this.e;
      console.log('client: All real time data has been received', (this.total) / 1000);
    });

  }

  totalx: Array<string> = [];
  totaly: Array<number> = []

  getFile() {
    this.dataService.getFile('http://localhost:4200/assets/dataFile/newdata.txt').subscribe(res => {
      for (const line of res.split(/[\r\n]+/)) {
        this.totalx.push(line.split(" ")[0]);
        this.totaly.push(Number(line.split(" ")[1]));
        //console.log(line.split(" "));
      }
      //console.log(this.totalx, this.totaly);
      setTimeout(() => {
        this.lineChartData[1].data.push(...this.totaly);
        this.lineChartLabels.push(...this.totalx);
        //console.log(this.lineChartData[1].data, this.lineChartLabels, this.totaly);
      }, 1000)
    });
  }

  connect() {
    this.dataService.connect();
  }
  disconnect() {
    this.dataService.disconnect();
  }

}

