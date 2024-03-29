import { BasicInfo, StudyAbroad } from './../../account/account.model';
import { Inquiry, InquiryComment } from './../inquiry.model';
import { Component, OnInit } from '@angular/core';
import { AccountService } from '../../services/account.service';

@Component({
  selector: 'app-inquiry-detail',
  templateUrl: './inquiry-detail.component.html',
  styleUrls: ['./inquiry-detail.component.css'],
})
export class InquiryDetailComponent implements OnInit {
  inquiry: Inquiry;


  basicInfo: BasicInfo;
  profileImageUrl: string;
  logoUrl: string;
  studyAbroad: StudyAbroad;

  constructor(
    private accountService: AccountService,
  ) {}

  ngOnInit(): void {
    this.profileImageUrl = this.accountService.getProfileImageUrl(null);
    this.logoUrl = this.getLogoUrl();
    this.basicInfo = {
      user: {
        username: 'hkoketsu',
        email: 'hiroki@email.com',
        password: 'hiroki',
      },
      name: 'Hiroki Koketsu',
      status: {
        value: 'CU',
        displayName: 'Current Student',
      },
      homeCountry: {
        name: 'Japan',
      },
      studyAbroadCountry: {
        name: 'Canada',
      },
    };
    this.inquiry = {
      user: {
        username: 'hkoketsu',
        email: 'hiroki@email.com',
        password: 'hiroki',
      },
      title: 'title',
      body: 'description',
      created_at: new Date(),
    };
  }

  getLogoUrl(): string {
    if (!this.basicInfo) {
      return 'assets/img/brand/logo_future.png';
    }
    switch (this.basicInfo.status.value) {
      case 'FU':
        return 'assets/img/brand/logo_future.png';
      case 'CU':
        return 'assets/img/brand/logo_current.png';
      case 'AL':
        return 'assets/img/brand/logo_alumni.png';
      default:
        return 'assets/img/brand/logo_future.png';
    }
  }
}
