

class Client {

    public static void main (String args[]) {

        A a = new A();

        B b = new B();

        b.m();

    }}

class A { void m() {
    System.out.println('a');
} }

class B extends A {void m() {
    System.out.println('b');
} }