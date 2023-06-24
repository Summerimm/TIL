package com.springstudy.board.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter // getter setter 자동설정
@AllArgsConstructor // 기본 생성자 자동설정
public class UserDTO {
    private String userName;
    private String userId;
    private String userPw;



}
