package com.company;

import java.math.BigInteger;

public class Puzzle {
    final static BigInteger M = new BigInteger("2021");

    private static BigInteger compute(long n) {

        String s = "";
        String a = new BigInteger(n+"").mod(M).toString();
        String b = new BigInteger(a).mod(M).toString();
        for (long i = 0; i < Integer.parseInt(a); i++) {
            s = s + a;
        }
        return new BigInteger(s.toString()).mod(M);
    }
    public static void main(String args[]) {

        for (long n : new long[] { 1L, 2L, 5L, 10L, 20L, 67489454811002199L }) {

            System.out.println("" + n + ": " + compute(n));
        }
    }
}
