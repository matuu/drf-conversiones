import { Perfil } from './../_models/perfil';
import { UserService } from './../_services/user.service';
import { Component, OnInit } from '@angular/core';
import { RegistrosService } from '../_services/registros.service';
import { Registro } from '../_models/registro';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  registros: Array<Registro> = new Array<Registro>();

  perfil: Perfil = new Perfil();
  registro: Registro = new Registro();
  agregando = false;

  constructor(
    public registrosServ: RegistrosService,
    public userServ: UserService
  ) { }

  ngOnInit() {
    this.getListaRegistros();
    setInterval(() => this.getListaRegistros(), 1500);
  }

  getListaRegistros() {
    this.registrosServ.getRegistros().subscribe(
      registros => {
        this.registros = registros;
        this.perfil = this.userServ.perfil;
      }
    );
  }

  openFormNuevo() {
    this.registro = new Registro();
    this.agregando = true;
  }

  closeFormNuevo() {
    this.agregando = false;
  }

  guardarNuevo() {
    this.registrosServ.postRegistro(this.registro).subscribe(
      ok => {
        console.log(ok);
        this.closeFormNuevo();
        this.getListaRegistros();
      },
      err => console.log(err);
    );
  }
}
