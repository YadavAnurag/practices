import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { SocketIoConfig, SocketIoModule } from 'ngx-socket-io';
import { ChartsModule } from 'ng2-charts';
import { HttpClientModule } from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LineChartComponent } from './line-chart/line-chart.component';




const config: SocketIoConfig = {
  url: 'localhost:9898',
  options: {
    autoConnect: true,
    reconnection: true,
    reconnectionDelay: 50,
    reconnectionAttempts: Infinity,
    forceNew: false
  }
};

@NgModule({
  declarations: [
    AppComponent,
    LineChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ChartsModule,
    SocketIoModule.forRoot(config),
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
