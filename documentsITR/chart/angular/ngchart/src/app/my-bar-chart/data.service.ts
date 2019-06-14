import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Injectable({
  providedIn: 'root'
})
export class DataService{
  constructor(private socket: Socket){}

  sendData(data: string){
    this.socket.emit('clientData', data);
  }
}



















// import { Injectable } from '@angular/core';
// import { Observable } from 'rxjs';
// import { Observer } from 'rxjs';
// import { map, catchError } from 'rxjs/operators';
// import * as socketIo from 'socket.io-client';

// import { Socket } from '../shared/interfaces';

// declare var io : {
//   connect(url: string): Socket;
// };

// @Injectable()
// export class DataService {

//   socket: Socket;
//   observer: Observer<number>;

//   getData() : Observable<number> {
//     this.socket = socketIo('http://localhost:8080');

//     this.socket.on('data', (res) => {
//       this.observer.next(res.data);
//     });

//     return this.createObservable();
//   }

//   createObservable() : Observable<number> {
//       return new Observable<number>(observer => {
//         this.observer = observer;
//       });
//   }

//   private handleError(error) {
//     console.error('server error:', error);
//     if (error.error instanceof Error) {
//         let errMessage = error.error.message;
//         return Observable.throw(errMessage);
//     }
//     return Observable.throw(error || 'Socket.io server error');
//   }

// }
