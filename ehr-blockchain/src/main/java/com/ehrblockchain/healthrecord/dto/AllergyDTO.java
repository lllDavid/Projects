package com.ehrblockchain.healthrecord.dto;

public class AllergyDTO {

    private Long id;
    private String allergen;
    private String reaction;
    private String severity;

    public AllergyDTO() {
    }

    public AllergyDTO(Long id, String allergen, String reaction, String severity) {
        this.id = id;
        this.allergen = allergen;
        this.reaction = reaction;
        this.severity = severity;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getAllergen() {
        return allergen;
    }

    public void setAllergen(String allergen) {
        this.allergen = allergen;
    }

    public String getReaction() {
        return reaction;
    }

    public void setReaction(String reaction) {
        this.reaction = reaction;
    }

    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
}