import { AuthenticationService } from './_services/authentication.service';
import { UserService } from './_services/user.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  constructor(
    public usuarioService: UserService,
    private authServ: AuthenticationService) {
  }

  get perfil() { return this.usuarioService.perfil; }
  get usuario() { return this.usuarioService.usuario; }

  logout() {
    this.authServ.logout();
    location.reload(true);
  }
}
