package com.example.appteoria04.models;

import com.example.appteoria04.app.MyApplication;

import java.util.Date;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;
import io.realm.annotations.Required;

public class Product extends RealmObject {

    @PrimaryKey
    private int id;
    @Required
    private String name;
    private int quantity;
    private double price;

    public Product() {
    }

    public Product(String name, int quantity, double price) {
        this.id = MyApplication.noteID.incrementAndGet();
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity){this.quantity = quantity;}

    public double getPrice() { return price; }

    public void setPrice(double price) { this.price = price; }

    public double total(){
        return quantity * price;
    }
}
