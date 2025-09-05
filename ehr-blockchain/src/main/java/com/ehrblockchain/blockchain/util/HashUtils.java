package com.ehrblockchain.blockchain.util;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Output;

import com.ehrblockchain.healthrecord.dto.*;

public class HashUtils {

    private static final Kryo kryo = new Kryo();

    static {
        kryo.register(HealthRecordDTO.class);

        kryo.register(DiagnosisDTO.class);
        kryo.register(NoteDTO.class);
        kryo.register(TreatmentPlanDTO.class);
        kryo.register(PrescriptionDTO.class);
        kryo.register(VitalsDTO.class);
        kryo.register(CBCDTO.class);
        kryo.register(AllergyDTO.class);
        kryo.register(LabResultDTO.class);
        kryo.register(ImmunizationDTO.class);
        kryo.register(MedicalHistoryDTO.class);
        kryo.register(FamilyHistoryDTO.class);
        kryo.register(EncounterDTO.class);
        kryo.register(ProcedureDTO.class);

        kryo.register(java.time.LocalDate.class);
        kryo.register(java.time.LocalDateTime.class);
    }

    public static String hashData(Object... data) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");

            for (Object d : data) {
                byte[] bytes = kryoSerialize(d);
                md.update(bytes);
            }

            return toHex(md.digest());
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 not available", e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static byte[] kryoSerialize(Object obj) throws IOException {
        try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
             Output output = new Output(baos)) {
            kryo.writeClassAndObject(output, obj);
            output.flush();
            return baos.toByteArray();
        }
    }

    private static String toHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}