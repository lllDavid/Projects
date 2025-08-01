package com.ehrblockchain.healthrecord.dto;

import java.time.LocalDate;

public class EncounterDTO {

    private Long id;
    private LocalDate encounterDate;
    private String provider;
    private String reason;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public LocalDate getEncounterDate() {
        return encounterDate;
    }

    public void setEncounterDate(LocalDate encounterDate) {
        this.encounterDate = encounterDate;
    }

    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }

    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
}
