package com.study.toyproject.apitest;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@Controller
public class ApiController {

    @GetMapping("/api/test")
    @ResponseBody
    public String getApiTest() {

        return "{\"result\":\"ok\"}";
    }

    @PostMapping("/api/test2")
    @ResponseBody
    public String getApiTest2() {

        return "{\"result2\":\"ok\"}";
    }

    @GetMapping("/data")
    @ResponseBody
    public Map<String, Object> getData() {
        Map<String, Object> data = new HashMap<>();
        data.put("message", "Hello, World!");
        data.put("timestamp", new Date());
        return data;
    }
}
