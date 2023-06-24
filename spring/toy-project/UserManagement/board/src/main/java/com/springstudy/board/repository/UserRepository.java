package com.springstudy.board.repository;

import com.springstudy.board.dto.UserDTO;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

@Repository
public class UserRepository {
    // 원래는 DB 연동하는 코드가 들어가야 함
    // JBA를 배우고 난 뒤 JBA를 이용해 DB 연동 가능
    // 여기서는 DB가 연동되었다는 가정을 함. static으로 만들어줌
    static public ArrayList<UserDTO> users;

    // DB
    static {
        users = new ArrayList<>();
        users.add(new UserDTO("Harim", "test1", "1234"));
        users.add(new UserDTO("Haneul", "test2", "1234"));
        users.add(new UserDTO("Hyunah", "test3", "1234"));
    }

    // Create
    public UserDTO insertUser(UserDTO user) {
        users.add(user);
        return user;
    }

    // Read - All
    public List<UserDTO> getAllUsers() {
        return users;
    }

    // Read - One of them
    public UserDTO getUserByUserId(String userId) {
        return users.stream()
                .filter(userDTO -> userDTO.getUserId().equals(userId))
                .findAny()
                .orElse(new UserDTO("", "", ""));
    }

    // Update
    public void updateUserPw(String userId, UserDTO user) {
        users.stream()
                .filter(userDTO -> userDTO.getUserId().equals(userId))
                .findAny()
                .orElse(new UserDTO("", "", ""))
                .setUserPw(user.getUserPw());
    }

    // Delete
    public void deleteUser(String userId) {
        users.removeIf(userDTO -> userDTO.getUserId().equals(userId));
    }
}
