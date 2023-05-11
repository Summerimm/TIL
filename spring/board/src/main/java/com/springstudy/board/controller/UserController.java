package com.springstudy.board.controller;

import com.springstudy.board.dto.UserDTO;
import com.springstudy.board.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    UserService userService;

    // Create -> POST
    @PostMapping("")
    public UserDTO insertUser(@RequestBody UserDTO user) {
        return userService.insertUser(user);
    }

    @GetMapping("") // 같은 URL로 다른 메서드 이용해 다양한 서비스 만들 수 있음
    // Read -> GET
    public List<UserDTO> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{userId}")
    public UserDTO getUserByUserId(@PathVariable String userId) {
        return userService.getUserByUserId(userId);
    }

    // Update -> PUT
    @PutMapping("/{userId}")
    public void updateUserPw(@PathVariable String userId, @RequestBody UserDTO user) {
        userService.updateUserPw(userId, user);
    }

    // Delete -> DELETE
    @DeleteMapping("/{userId}")
    public void deleteUser(@PathVariable String userId) {
        userService.deleteUser(userId);
    }
}
