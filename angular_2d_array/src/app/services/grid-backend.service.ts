import { Injectable }          from '@angular/core';
import { Observable, of }      from 'rxjs';
import { HttpClient }          from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class GridBackendService {
    private baseUrl                          = 'http://69.16.201.27:8001'
    constructor(private http: HttpClient) { }
 
    get_initial_arr(): Observable<Array<{}>>  {
        let url_end_point = `${this.baseUrl}/grid/init/`
        return this.http.get<Array<{}>>(url_end_point );
    }

    rotate_now(): Observable<Array<{}>>  {
        let url_end_point = `${this.baseUrl}/grid/rotate/1/`
        return this.http.get<Array<{}>>(url_end_point );
    }

}




