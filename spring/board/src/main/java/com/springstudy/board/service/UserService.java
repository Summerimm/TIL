package com.springstudy.board.service;

import com.springstudy.board.dto.UserDTO;
import com.springstudy.board.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    @Autowired
    UserRepository userRepository;

    // Create
    public UserDTO insertUser(UserDTO user) {
        return userRepository.insertUser(user);
    }

    // Read
    public List<UserDTO> getAllUsers() {
        return userRepository.getAllUsers();
    }

    public UserDTO getUserByUserId(String userId) {
        return userRepository.getUserByUserId(userId);
    }

    public void updateUserPw(String userId, UserDTO user) {
        userRepository.updateUserPw(userId, user);
    }

    public void deleteUser(String userId) {
        userRepository.deleteUser(userId);
    }

}
