package com.ehrblockchain.security.encryption;

import com.google.crypto.tink.Aead;

import java.nio.charset.StandardCharsets;
import java.util.Base64;

import jakarta.persistence.AttributeConverter;
import jakarta.persistence.Converter;

// TODO: support all types, currently string only
@Converter(autoApply = false)
public class ColumnEncryptionConverter implements AttributeConverter<String, String> {

    private static final Aead AEAD = AeadKeysetManager.getAead();
    private static final byte[] AAD = "field_encryption".getBytes(StandardCharsets.UTF_8);

    @Override
    public String convertToDatabaseColumn(String attribute) {
        if (attribute == null) return null;
        try {
            byte[] encrypted = AEAD.encrypt(attribute.getBytes(StandardCharsets.UTF_8), AAD);
            return Base64.getEncoder().encodeToString(encrypted);
        } catch (Exception e) {
            throw new IllegalStateException("Encrypt failure", e);
        }
    }

    @Override
    public String convertToEntityAttribute(String dbData) {
        if (dbData == null) return null;
        try {
            byte[] decoded = Base64.getDecoder().decode(dbData);
            byte[] decrypted = AEAD.decrypt(decoded, AAD);
            return new String(decrypted, StandardCharsets.UTF_8);
        } catch (Exception e) {
            throw new IllegalStateException("Decrypt failure", e);
        }
    }
}