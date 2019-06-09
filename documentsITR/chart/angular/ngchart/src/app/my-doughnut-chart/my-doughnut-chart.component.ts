import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-my-doughnut-chart',
  templateUrl: './my-doughnut-chart.component.html',
  styleUrls: ['./my-doughnut-chart.component.css']
})
export class MyDoughnutChartComponent implements OnInit {

  public doughnutChartLabels = ['Sales 01', 'Sales 02','Sales 03','Sales 04'];
  public doughnutChartData = [128, 158, 180, 90];
  public doughnutChartType = 'doughnut';
  constructor() { }

  ngOnInit() {
  }

}
