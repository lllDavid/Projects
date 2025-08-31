package com.ehrblockchain.user.mapper;

import org.mapstruct.*;

import com.ehrblockchain.user.model.User;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;

@Mapper(
        componentModel = "spring",
        nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE
)
public interface UserMapper {

    User toEntity(UserCreateDTO dto);

    @Mapping(target = "roleName", source = "role.name")
    @Mapping(target = "patientId", source = "patient.id")
    UserDTO toDto(User user);

    void updateFromDto(UserUpdateDTO dto, @MappingTarget User user);

}