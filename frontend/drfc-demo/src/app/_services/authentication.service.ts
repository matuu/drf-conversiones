import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Perfil } from '../_models/perfil';

@Injectable({ providedIn: 'root' })
export class AuthenticationService {

    user: any = {};
    perfil: Perfil;

    constructor(private http: HttpClient) { }

    login(username: string, password: string) {
        const encodeAuth = window.btoa(username + ':' + password);
        const headers = {
            Authorization: `Basic ${encodeAuth}`
        };
        console.log(headers);
        return this.http.get<Perfil>(`http://127.0.0.1:8000/api/perfil/`, { headers: headers })
            .pipe(map(perfil => {
                if (perfil) {
                    // store user details and basic auth credentials in local storage
                    // to keep user logged in between page refreshes
                    this.user = {
                        username: username,
                        password: password,
                        authdata: encodeAuth
                    };
                    this.perfil = perfil;
                    localStorage.setItem('user', JSON.stringify(this.user));
                    localStorage.setItem('perfil', JSON.stringify(this.perfil));
                }

                return this.user;
            }));
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('user');
        localStorage.removeItem('perfil');
    }

}
