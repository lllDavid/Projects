package com.ehrblockchain.patient.model;

import jakarta.persistence.Column;
import jakarta.persistence.Convert;
import jakarta.persistence.Embeddable;

import jakarta.validation.constraints.Size;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Embeddable
public class Address {
    @Size(max = 100)
    @Column(name = "street")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String street;

    @Size(max = 100)
    @Column(name = "city")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String city;

    @Size(max = 100)
    @Column(name = "state")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String state;

    // Implement regex pattern as needed
    @Column(name = "postal_code")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String postalCode;

    @Size(max = 100)
    @Column(name = "country")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String country;

    public Address() {
    }

    public Address(String street, String city, String state, String postalCode, String country) {
        this.street = street;
        this.city = city;
        this.state = state;
        this.postalCode = postalCode;
        this.country = country;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    @Override
    public String toString() {
        return "Address{" +
                "street='" + street + '\'' +
                ", city='" + city + '\'' +
                ", state='" + state + '\'' +
                ", postalCode='" + postalCode + '\'' +
                ", country='" + country + '\'' +
                '}';
    }
}