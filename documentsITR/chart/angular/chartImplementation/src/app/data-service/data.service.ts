import { Socket } from 'ngx-socket-io';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { DataInterface } from '../interfaces/dataInterface';

@Injectable({
    providedIn: 'root'
})
export class DataService {
    constructor(private socket: Socket) { }

    sendData(data: string) {
        console.log('in sendData');
        this.socket.emit("clientMessage", 'client data sent to server');
    }

    getData(): Observable<DataInterface> {
        return this.socket.fromEvent<DataInterface>('serverMessage');
    }
}