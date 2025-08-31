package com.ehrblockchain.security.encryption;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;

import com.google.crypto.tink.Aead;
import com.google.crypto.tink.KeysetHandle;
import com.google.crypto.tink.InsecureSecretKeyAccess;
import com.google.crypto.tink.TinkJsonProtoKeysetFormat;
import com.google.crypto.tink.aead.AeadConfig;
import com.google.crypto.tink.aead.AesGcmKeyManager;
import com.google.crypto.tink.RegistryConfiguration;

public final class AeadKeysetManager {

    private static final String KEYSET_FILENAME = "aead_keyset.json";
    private static final KeysetHandle KEYSET_HANDLE;
    private static final Aead AEAD;

    // Temporary, replace InsecureSecretKeyAccess with Key Management System
    static {
        try {
            AeadConfig.register();

            Path keyPath = Path.of(KEYSET_FILENAME);

            if (Files.exists(keyPath)) {
                String json = Files.readString(keyPath, StandardCharsets.UTF_8);
                KEYSET_HANDLE = TinkJsonProtoKeysetFormat.parseKeyset(
                        json, InsecureSecretKeyAccess.get()
                );
            } else {
                KeysetHandle generatedHandle = KeysetHandle.generateNew(
                        AesGcmKeyManager.aes256GcmTemplate()
                );
                String json = TinkJsonProtoKeysetFormat.serializeKeyset(
                        generatedHandle, InsecureSecretKeyAccess.get()
                );
                Files.writeString(keyPath, json, StandardCharsets.UTF_8);
                KEYSET_HANDLE = generatedHandle;
            }

            AEAD = KEYSET_HANDLE.getPrimitive(RegistryConfiguration.get(), Aead.class);

        } catch (Exception e) {
            throw new ExceptionInInitializerError(e);
        }
    }

    public static Aead getAead() {
        return AEAD;
    }
}