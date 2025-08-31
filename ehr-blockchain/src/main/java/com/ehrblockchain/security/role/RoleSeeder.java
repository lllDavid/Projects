package com.ehrblockchain.security.role;

import java.util.concurrent.atomic.AtomicBoolean;

import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.security.role.model.Role;
import com.ehrblockchain.security.role.repository.RoleRepository;

@Component
public class RoleSeeder implements ApplicationListener<ContextRefreshedEvent> {

    private final RoleRepository roleRepository;
    private final AtomicBoolean seeded = new AtomicBoolean(false);

    public RoleSeeder(RoleRepository roleRepository) {
        this.roleRepository = roleRepository;
    }

    @Override
    @Transactional
    public void onApplicationEvent(ContextRefreshedEvent event) {
        if (!seeded.compareAndSet(false, true)) {
            return;
        }

        for (RoleEnum roleEnum : RoleEnum.values()) {
            roleRepository.findByName(roleEnum)
                    .orElseGet(() -> {
                        Role role = new Role();
                        role.setName(roleEnum);
                        role.setDescription("Auto-generated role: " + roleEnum.name());
                        return roleRepository.save(role);
                    });
        }
    }
}