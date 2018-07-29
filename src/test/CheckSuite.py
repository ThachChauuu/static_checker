import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_1(self):
        input = "int getInt;"
        output = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input, output, 401))

    def test_2(self):
        input = """int a, a;"""
        output = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, output, 402))

    def test_3(self):
        input = """
         int foo(int a, float a) {
             return 0;
         }
         int ax;"""
        output = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, output, 403))

    def test_4(self):
        input = """int a;
        int a(){
            return 0;
        }"""
        output = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, output, 404))

    def test_5(self):
        input = """int foo(){
            int a, a;
        }
        int foo1(int a){
            return 0;
        }"""
        output = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, output, 405))

    def test_6(self):
        input = """int foo(int b){
            int b;
            return 0;
        }"""
        output = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, output, 406))

    def test_7(self):
        input = """int foo(){
            int a, a;
            return 0;
        }"""
        output = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, output, 407))

    def test_8(self):
        input = """int foo(int a, int a){
            return 0;
        }"""
        output = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, output, 408))

    def test_9(self):
        input = """int foo(float a, boolean b) {
            boolean b;
            return 0;
        }"""
        output = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, output, 409))

    def test_10(self):
        input = """int a;
        boolean func1(){
            int index;
        }
        boolean func(){
            int ahihi;
        }
        int a;"""
        output = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, output, 410))