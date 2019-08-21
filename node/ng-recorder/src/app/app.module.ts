import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";

import { SocketIoConfig, SocketIoModule, Socket } from "ngx-socket-io";
import { ChathomeComponent } from './chathome/chathome.component';

const config: SocketIoConfig = {
  url: "localhost:3000",
  options: {
    autoConnect: true,
    reconnection: true
  }
};

@NgModule({
  declarations: [AppComponent, ChathomeComponent],
  imports: [BrowserModule, AppRoutingModule, SocketIoModule.forRoot(config)],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
