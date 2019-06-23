import { Socket } from 'ngx-socket-io';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { DataInterface } from '../interfaces/dataInterface';
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';


@Injectable({
    providedIn: 'root'
})
export class DataService {
    constructor(private http: HttpClient, private socket: Socket) { }

    connect() {
        // console.log();
        this.socket.ioSocket.connect({ forceNew: false });
    }

    disconnect() {
        this.socket.ioSocket.disconnect();
    }

    sendData(data: string) {
        console.log('in sendData');
        this.socket.emit("clientMessage", 'client data sent to server');
    }

    sendMessageToServerToSendNominalData(data: string) {
        console.log('in sendNominalData');
        this.socket.emit('sendNominalData', data);
    }

    getNominalData(): Observable<DataInterface> {
        this.socket.emit('getNominalData', 'please send nominal data');
        return this.socket.fromEvent<DataInterface>('serverNominalData');
    }

    getCompletionMessage(): Observable<string> {
        return this.socket.fromEvent<string>('serverNominalDataCompleted');
    }

    getRealTimeData(): Observable<DataInterface> {
        this.socket.emit('getRealTimeData', 'client: please send realtime data');
        return this.socket.fromEvent<DataInterface>('serverRealTimeData');
    }


    getFile(url: string): Observable<string> {
        return this.http.get<string>(url, { responseType: 'text' as 'json' });
    }


    private handleError(err: HttpErrorResponse) {
        // in a real world app, we may send the server to some remote logging infrastructure
        // instead of just logging it to the console
        let errorMessage = '';
        if (err.error instanceof ErrorEvent) {
            // A client-side or network error occurred. Handle it accordingly.
            errorMessage = `An error occurred: ${err.error.message}`;
        } else {
            // The backend returned an unsuccessful response code.
            // The response body may contain clues as to what went wrong,
            errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
        }
        console.error(errorMessage);
        return throwError(errorMessage);
    }
}