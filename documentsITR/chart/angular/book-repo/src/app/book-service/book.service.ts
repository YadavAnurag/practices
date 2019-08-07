import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { IBook } from './book';

@Injectable({providedIn: 'root'})
export class BookService {
  constructor(private httpClient: HttpClient) { }

  private bookURL = 'http://starlord.hackerearth.com/books';

  getBooks(): Observable<IBook[]> {
    console.log('finds');
    return this.httpClient.get<IBook[]>(this.bookURL).pipe(tap(bookData => {
      console.log('All: ' + JSON.stringify(bookData));
    }),
    catchError(this.handleError));
  }

  private handleError(err: HttpErrorResponse) {
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      errorMessage = `An error occurred: ${err.error.message}`;
    } else {
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage);
    return throwError(errorMessage);
  }

}
