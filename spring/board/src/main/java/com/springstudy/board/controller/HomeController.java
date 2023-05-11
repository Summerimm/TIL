package com.springstudy.board.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController // == @Controller + @ ResponseBody
@RequestMapping("/")
public class HomeController {

    @GetMapping("")
    public String test() {
        return "test!!!";
    }
}
