import { Registro } from './../_models/registro';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({ providedIn: 'root' })
export class RegistrosService {

    constructor(private http: HttpClient) {

    }

    getRegistros() {
        return this.http.get<Array<Registro>>(`http://127.0.0.1:8000/api/registro/`);
    }

    postRegistro(registro: Registro) {
        const body = JSON.stringify(registro);
        return this.http.post<Registro>(`http://127.0.0.1:8000/api/registro/`, body, {headers: { 'Content-Type': 'application/json' }});
    }
}
