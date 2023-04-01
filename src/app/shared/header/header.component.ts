import { Component, ElementRef, OnInit, Renderer2, ViewChild } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  @ViewChild('asOpen') asOpen! : ElementRef;
  icon: string = 'uil uil-moon';
  constructor(private renderer2: Renderer2) { }

  changeIcon(){
    this.icon = this.icon === 'uil uil-bright' ? 'uil uil-moon' : 'uil uil-bright'
    if (this.icon === 'uil uil-moon') {
      document.documentElement.classList.remove('dark');
    }else{
      document.documentElement.classList.add('dark');
    }
  }

  openNav(){
    this.renderer2.addClass(this.asOpen.nativeElement, 'openNav');
  }

  closeNav(){
    this.renderer2.removeClass(this.asOpen.nativeElement, 'openNav');
  }

  ngOnInit(): void {
  }

}
