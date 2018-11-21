import { Component, OnInit } from '@angular/core';
import { RegistrosService } from '../_services/registros.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  registros = [];
  constructor(
    public registrosServ: RegistrosService
  ) { }

  ngOnInit() {
    this.registrosServ.getRegistros().subscribe(
      registros => this.registros = registros
    );
  }

}
