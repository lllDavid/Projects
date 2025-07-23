package com.ehrblockchain.healthrecord.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;

@Entity
@Table(name = "family_history")
public class FamilyHistory {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String relative;
    private String condition;

    @Column(name = "family_history_notes")
    private String notes;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public FamilyHistory() {
    }

    public FamilyHistory(String relative, String condition, String notes) {
        this.relative = relative;
        this.condition = condition;
        this.notes = notes;
    }

    public Long getId() {
        return id;
    }

    public String getRelative() {
        return relative;
    }

    public void setRelative(String relative) {
        this.relative = relative;
    }

    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "FamilyHistory{" +
                "id=" + id +
                ", relative='" + relative + '\'' +
                ", condition='" + condition + '\'' +
                ", notes='" + notes + '\'' +
                '}';
    }
}
