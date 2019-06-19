import { Component, OnInit, OnDestroy } from '@angular/core';
import { DataInterface } from '../interfaces/dataInterface';
import { DataService } from '../data-service/data.service';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { Label, Color } from 'ng2-charts';
import { saveAs } from 'file-saver';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  x: number;
  y: number;
  dataLength:number = 15;

  xmax:number = 2500000;
  xmin:number = 0;

  ymax:number = 1000000;
  ymin:number = 0;

  constructor(private dataService: DataService) { }


  public lineChartData: ChartDataSets[] = [
    { data: [], borderWidth:0.5,fill: false,borderColor:'red',lineTension: 0, label: 'Real-Time Data' },
    { data: [], borderWidth:0.5,fill: false,borderColor:'red',lineTension:0, label: 'Nominal Data' },
  ];
  public lineChartLabels: Label[ ] = [];  
  public lineChartOptions: ChartOptions = {
    responsive: true, 
    elements: {
      point: {
        radius: 1
      }
    },

    scales: {
      xAxes: [{
        display: false,
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


  ngOnInit() {}
  ngOnDestroy() {}

  getNominalData(){
    this.dataService.getNominalData().subscribe(serverData =>{
      console.log(serverData);
      this.x = serverData['x'];
      this.y = serverData['y'];
      this.lineChartData[1].data.push(this.y);
      this.lineChartLabels.push(this.x.toString());
    });

    this.dataService.getCompletionMessage().subscribe(serverData=>{
      console.log('client: All nominal data has been received');
    });

  }

  getRealTimeData(){
    this.dataService.getRealTimeData().subscribe(serverData =>{
      console.log(`server: realtime data ${serverData['x']}, ${serverData['y']}`);
      this.x = serverData['x'];
      this.y = serverData['y'];
      this.lineChartData[0].data.push(this.y);
    });

    this.dataService.getCompletionMessage().subscribe(serverData=>{
      console.log('client: All real time data has been received');
    });

  }


  saveFile(){
    console.log('saving');
    saveAs.saveAs('http://localhost:9898/file', 'plainText.txt');
  }

}

