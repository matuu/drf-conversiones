import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class UserService {

    constructor(private http: HttpClient) {

    }

    get perfil() {
        try {
            return JSON.parse(localStorage.getItem('perfil'));
        } catch (ex) {
            console.error(ex);
            return {};
        }
    }

    get usuario() {
        try {
            return JSON.parse(localStorage.getItem('user'));
        } catch (ex) {
            console.error(ex);
            return {};
        }
    }
}
