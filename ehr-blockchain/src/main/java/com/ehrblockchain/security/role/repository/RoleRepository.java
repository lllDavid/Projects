package com.ehrblockchain.security.role.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ehrblockchain.security.role.RoleEnum;
import com.ehrblockchain.security.role.model.Role;

public interface RoleRepository extends JpaRepository<Role, Integer> {
    Optional<Role> findByName(RoleEnum name);
}