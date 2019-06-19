import { Socket } from 'ngx-socket-io';
import { Injectable } from '@angular/core';
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

    sendMessageToServerToSendNominalData(data: string){
        console.log('in sendNominalData');
        this.socket.emit('sendNominalData', data);
    }

    getNominalData(): Observable<DataInterface>{
        this.socket.emit('getNominalData', 'please send nominal data');
        return this.socket.fromEvent<DataInterface>('serverNominalData');
    }

    getCompletionMessage():Observable<string>{
        return this.socket.fromEvent<string>('serverNominalDataCompleted');
    }

    getRealTimeData(): Observable<DataInterface> {
        this.socket.emit('getRealTimeData', 'client: please send realtime data');
        return this.socket.fromEvent<DataInterface>('serverRealTimeData');
    }
}