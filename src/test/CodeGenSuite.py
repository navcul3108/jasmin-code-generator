import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

#region Test simple progam
    def test_int(self):
        """Simple program: int main() {} """
        input = """ Var: x = 1, y = 1.2;
                    Function: foo
                    Parameter: a
                   Body: 
                        a = 1.2;
                        print(string_of_float(a));
                   EndBody.
                   Function: main
                   Body:
                        foo(1.2);
                   EndBody."""
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_502(self):
        input = """
            Function: foo
            Parameter: a[1][2]
            Body:
               a = {{2,3}};
               print(string_of_int(a[0][1]));
            EndBody.
            Function: main
            Body:
                foo({{1,2}});
            EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    
    def test_503(self):
        input = """
            Function: foo
            Body:
                Var: a = "Test foo";
                print(a);
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "Test foo"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    
    def test_504(self):
        input = """
            Function: foo
            Body:
                Var: a = True;
                print(string_of_bool(a));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test_505(self):
        input = """
            Function: foo
            Parameter: a,b
            Body:
                b = "123\\n";
                a = 1;
                print(b);
                print(string_of_int(a));
            EndBody.
            Function: main
            Body:
                foo(1, "abc");
            EndBody.
        """
        expect = "123\n1"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    
    def test_506(self):
        input = """
            Function: main
            Body:
                foo();
            EndBody.
            Function: foo
            Body:
                print("Function is called before decalration");                
            EndBody.
        """
        expect = "Function is called before decalration"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_507(self):
        input = """
            Var: a=1, b=1.2, c=True;
            Function: foo
            Parameter: a,b,c
            Body:
                print(string_of_int(a));
                print(string_of_float(b));
                print(string_of_bool(c));
            EndBody.
            Function: main
            Body:
                foo(a,b,c);
            EndBody.
        """
        expect = "11.2true"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    
    def test_508(self):
        input = """
            Function: foo
            Body:
                Var: float = 1000e-2;
                print(string_of_float(float));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_509(self):
        input = """
            Function: foo
            Body:
                Var: a[2][2] = {{1,2},{3,4}};
                a[0][0] = 3;
                a[0][1] = 4;
                a[1][0] = 1;
                a[1][1] = 2;
                print(string_of_int(a[0][0]));
                print("\\n");
                print(string_of_int(a[0][1]));
                print("\\n");
                print(string_of_int(a[1][0]));
                print("\\n");
                print(string_of_int(a[1][1]));
                print("\\n");
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "3\n4\n1\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))
#endregion

#region test everything
    def test_510(self):
        input = """
            Function: main
            Body:
                If True Then
                    print("True");
                EndIf.
            EndBody.
        """
        expect = "True"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_511(self):
        input = """
            Function: main
            Body:
                If False Then
                    print("False");
                ElseIf True Then
                    print("True");
                EndIf.
            EndBody.
        """
        expect = "True"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_512(self):
        input = """
            Function: main
            Body:
                If False Then
                    print("If");
                ElseIf False Then
                    print("Else If 1");
                ElseIf False Then
                    print("Else If 2");
                ElseIf False Then
                    print("Else If 3");
                Else
                    print("Else");
                EndIf.
            EndBody.
        """
        expect = "Else"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test_513(self):
        input = """
            Function: main
            Body:
                Var: i=0;
                For(i=1,i<10,2) Do
                    print(string_of_int(i));
                    print("\\n");
                EndFor.
            EndBody.
        """
        expect = "1\n3\n5\n7\n9\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_514(self):
        input = """
            Function: foo
            Body:
                Return 1;
            EndBody.
            Function: main
            Body:
                print(string_of_int(foo()));
            EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_515(self):
        input = """
            Function: main
            Body:
                Var: a=1;
                For(a=0, a<3, 1) Do
                    print("Before break");
                    Break;
                    print("After break");
                EndFor.
            EndBody.
        """
        expect = "Before break"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test_516(self):
        input = """
            Function: main
            Body:
                Var: a=1;
                For(a=0, a<3, 1) Do
                    print("Before break");
                    print("\\n");
                    Continue;
                    print("After break");
                EndFor.
            EndBody.
        """
        expect = "Before break\nBefore break\nBefore break\n"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    
    def test_517(self):
        input = """
            Function: main
            Body:
                Var: x=0;
                While x<5 Do
                    print(string_of_int(x));
                    x = x+1;
                EndWhile.
            EndBody.
        """
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_518(self):
        input = """
            Function: main
            Body:
                Var: x=1;
                Do
                    print(string_of_int(x));
                    x = x+1;
                    Break;
                    print("After break");
                While x<2
                EndDo.
            EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_519(self):
        input = """
            Function: main
            Body:
                Var: x=1;
                Do
                    print(string_of_int(x));
                    x = x+1;
                    Continue;
                    print("After break");
                While x<3
                EndDo.
            EndBody.        
            """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,519))
#endregion

#region unused 
    def test_520(self):
        input = """
            Function: main
            Body:
                If(1.0 <. 2.0) Then
                    print("Compare 2 float");
                EndIf.
            EndBody.
        """
        expect = "Compare 2 float"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_521(self):
        input = """
            Function: main
            Body:
                If(1.0 <=. 2.0) Then
                    print("Compare 2 float");
                EndIf.
            EndBody.
        """
        expect = "Compare 2 float"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    
    def test_522(self):
        input = """
            Function: main
            Body:
                If(2.0 >. 1.0) Then
                    print("Compare 2 float");
                EndIf.
            EndBody.        
            """
        expect = "Compare 2 float"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    
    def test_523(self):
        input = """
            Function: main
            Body:
                If(2.0 >=. 1.0) Then
                    print("Compare 2 float");
                EndIf.
            EndBody.        
        """
        expect = "Compare 2 float"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    def test_524(self):
        input = """
            Function: main
            Body:
                If(2.0 =/= 1.0) Then
                    print("Compare 2 float");
                EndIf.
            EndBody.        
        """
        expect = "Compare 2 float"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    
    def test_525(self):
        input = """
            Function: main
            Body:
                foo();
            EndBody.
            Function: foo
            Body:
                print("foo");
            EndBody.
        """
        expect = "foo"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    
    def test_526(self):
        input = """
            Function: foo
            Body:

            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,526))
    
    def test_527(self):
        input = """
            Function: foo
            Body:
                Var: a = "abc";
                print(a);
            EndBody.
            Function: main
            Parameter: a, b
            Body:
                foo();
            EndBody.
        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    
    def test_528(self):
        input = """
            Function: fact
            Parameter: n
            Body:
                If(n==1) Then
                    Return 1;
                Else
                    Return fact(n-1) * n;
                EndIf.
            EndBody.
            Function: main
            Body:
                print(string_of_int(fact(3)));
            EndBody.
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    
    def test_529(self):
        input = """
            Var: a = 10;
            Function: foo
            Body:
                If(a==1) Then
                    Return a;
                Else
                    a = a-1;
                    Return a + foo();
                EndIf.
            EndBody.
            Function: main
            Body:
                print(string_of_int(foo()));
            EndBody.
        """
        expect = "46"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    
    def test_530(self):
        input = """
            Function: foo
            Parameter: a, b
            Body:
                print(string_of_float(a+.float_to_int(b)));
            EndBody.
            Function: main
            Body:
                foo(1.2, 1);
            EndBody.
        """
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input,expect,530))
#endregion

#region Test with array
    def test_531(self):
        input = """
            Function: foo
            Parameter: a[2][2]
            Body:
                print(a[1][1]);
            EndBody.
            Function: main
            Body:
                foo({{"a", "b"}, {"c", "d"}});
            EndBody.
        """
        expect = "d"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    
    def test_532(self):
        input = """
            Function: foo
            Parameter: a[2][2]
            Body:
                If(a[1][0]) Then
                    print(string_of_bool(a[0][1]));
                Else
                    print(string_of_bool(a[0][0]));
                EndIf.
            EndBody.
            Function: main
            Body:
                foo({{True, False}, {False, True}});
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_533(self):
        input = """
            Function: foo
            Parameter: a[2][2][2]
            Body:
                print(string_of_float(a[1][0][1]));
            EndBody.
            Function: main
            Body:
                foo({ {{1.0, 2.0},{3.45, 1.56}}, {{100e-2, 2.0},{1.2e+10, 3.0}} });
            EndBody.
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_534(self):
        input = """
            Function: foo
            Body:
                Return {{"First element","Second"},{"Third", "Fourth"}};            
            EndBody.
            Function: main
            Body:
                print(foo()[0][0]);
            EndBody.
        """
        expect = "First element"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_535(self):
        input = """
            Function: foo
            Parameter: a[1][2], b
            Body:
                Return a[0][1]+.b;
            EndBody.
            Function: main
            Body:
                print(string_of_float(foo({{1.2e-2, 2.3}}, 1.5)));
            EndBody.
        """
        expect = "3.8"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    
    def test_536(self):
        input = """
            Function: foo
            Body:
                Return "abc";
            EndBody.
            Function: main
            Body:
                Var: a[1][2] = {{"a", "b"}};
                a[0][0] = foo();
                print(a[0][0]);
            EndBody.
        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    
    def test_537(self):
        input = """
            Function: foo
            Body:
                Return {{1,2},{3,4}};
            EndBody.
            Function: main
            Body:
                Var: a[2][2] = {{0,0},{0,0}};
                a = foo();
                print(string_of_int(a[0][0]));
            EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_538(self):
        input = """
            Function: foo
            Body:
                Return {{True, False}, {True, False}};
            EndBody.
            Function: main
            Body:
                Var: a[2][2] = {{False, False}, {False, False}};
                a = foo();
                print(string_of_bool(a[0][0]));
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    
    def test_539(self):
        input = """
            Function: foo
            Body:
                Return {{1.2, 120e-2},{1.2e3, 200e-5}};
            EndBody.
            Function: main
            Body:
                Var: a = {{1.0, 1.0}, {1.0, 1.0}};
                a = foo();
                print(string_of_float(a[1][1]));
            EndBody.
        """
        expect = "0.002"
        self.assertTrue(TestCodeGen.test(input,expect,539))
#endregion

#region test global variable
    def test_540(self):
        input = """
            Var: int=1000, b=1222.2e-2, c=True, d = "abc";
            Function: foo
            Body:
                print(string_of_int(int));
                print("\\n");
                print(string_of_float(b));
                print("\\n");
                print((string_of_bool(c)));
                print("\\n");
                print(d);
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "1000\n12.222\ntrue\nabc"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    def test_541(self):
        input = """
            Var: a = 1, b=1.2, c = True;
            Function: foo
            Parameter: x, y, z
            Body:
                print(string_of_int(x));
                print("\\n");
                print(string_of_float(y));
                print("\\n");
                print((string_of_bool(z)));
            EndBody.
            Function: main
            Body:
                foo(a,b,c);
            EndBody.
        """
        expect = "1\n1.2\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    
    def test_542(self):
        input = """
            Var: a=1, b=2.5;
            Function: foo
            Body:
                a = a-1;
            EndBody.
            Function: main
            Body:
                foo();
                foo();
                foo();
                foo();
                print(string_of_int(a));
            EndBody.
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    
    def test_543(self):
        input = """
            Var: a=1;
            Function: foo
            Parameter: a
            Body:
                a = a+1;
                print(string_of_int(a));
            EndBody.
            Function: main
            Body:
                foo(a);
                print("\\n");
                print(string_of_int(a));
            EndBody.
        """
        expect = "2\n1"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    
    def test_544(self):
        input = """
            Var: x = {{1, 2}};
            Function: foo
            Parameter: a, b
            Body:
                x[0][0] = a;
                x[0][1] = b;
            EndBody.
            Function: main
            Body:
                foo(2,4);
                print(string_of_int(x[0][0]));
                print(string_of_int(x[0][1]));
            EndBody.
        """
        expect = "24"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test_545(self):
        input = """
            Var: x = "123";
            Function: foo
            Body:
                x = "abc";
            EndBody.
            Function: main
            Body:
                foo();
                print(x);
            EndBody.
        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_546(self):
        input = """
            Var: x = True;
            Function: foo
            Body:
                x = !(5>3);
            EndBody.
            Function: main
            Body:
                foo();
                print(string_of_bool(x));
            EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    
    def test_547(self):
        input = """
            Var: x = 1.2;
            Function: foo
            Body:
                x = x *. 3.0;
            EndBody.
            Function: main
            Body:
                foo();
                foo();
                foo();
                print(string_of_float(x));
            EndBody.
        """
        expect = "32.4"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_548(self):
        input = """
            Var: x = 2;
            Function: foo
            Body:  
                x = x * x;
            EndBody.
            Function: main
            Body:
                foo();
                foo();
                foo();
                print(string_of_int(x));
            EndBody.
        """
        expect = "256"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test_549(self):
        input = """
            Var: x =1, y = 1.2, z = True, t = "abc", a[3] ={"a", "b", "c"};
            Function: foo
            Parameter: x, y, z, t, a[3] 
            Body:
                print(string_of_int(x));
                print("\\n");
                print(string_of_float(y));
                print("\\n");
                print(string_of_bool(z));
                print("\\n");
                print(t);
                print("\\n");
                print(a[0]);
                print("\\n");
                print(a[1]);
                print("\\n");
                print(a[2]);
            EndBody.
            Function: main
            Body:
                foo(x, y, z, t, a);
            EndBody.
        """
        expect = "1\n1.2\ntrue\nabc\na\nb\nc"
        self.assertTrue(TestCodeGen.test(input,expect,549))
#endregion

#region Test operator   
    def test_550(self):
        input = """
            Function: foo
            Body:
                Var: x =12, y =25;
                print(string_of_int(x+y));
                print("\\n");
                print(string_of_int(x-y));
                print("\\n");
                print(string_of_int(x\\y));
                print("\\n");
                print(string_of_int(x*y));
                print("\\n");
                print(string_of_int(x%y));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "37\n-13\n0\n300\n12"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    def test_551(self):
        input = """
            Function: foo
            Body:
                Var: x= 1.2, y=1.5;
                print(string_of_float(x+.y));
                print("\\n");
                print(string_of_float(x-.y));
                print("\\n");
                print(string_of_float(x\\.y));
                print("\\n");
                print(string_of_float(x*.y));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "2.7\n-0.29999995\n0.8\n1.8000001"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    
    def test_552(self):
        input = """
            Function: foo
            Body:
                Var: x=2, y=1;
                print(string_of_bool(x>y));
                print(string_of_bool(x>=y));
                print(string_of_bool(x<y));
                print(string_of_bool(x<=y));
                print(string_of_bool(x!=y));
                print(string_of_bool(x==y));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "truetruefalsefalsetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    
    def test_553(self):
        input = """
            Function: foo
            Body:
                Var: x= 1.0, y =1.2;
                print(string_of_bool(x>.y));
                print(string_of_bool(x>=.y));
                print(string_of_bool(x<=.y));
                print(string_of_bool(x<.y));
                print(string_of_bool(x=/=y));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "falsefalsetruetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    
    def test_554(self):
        input = """
            Function: foo
            Body:
                print(string_of_bool(True&&False));
                print(string_of_bool(True||False));
                print(string_of_bool(!False));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    
    def test_555(self):
        input = """
            Function: foo
            Body:
                print(string_of_int(-5));
                print(string_of_int(--5));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "-55"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    
    def test_556(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                print(string_of_int(x));
                print("\\n");
                print(string_of_float(y));                
            EndBody.
            Function: main
            Body:
                Var: x=100, y=1000.234e-2;
                foo(x*2, y\\.2.5);
            EndBody.
        """
        expect = "200\n4.0009203"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    
    def test_557(self):
        input = """
            Function: foo
            Parameter: x, y[5]
            Body:
                print(string_of_bool(x&&(y[2]>5)));
                print("\\n");
                print(string_of_int(y[3]));
            EndBody.
            Function: main
            Body:
                Var: x=1, y[5]={1,2,3,4,5};
                foo(x, y);
            EndBody.
        """
        expect = "false\n4"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    
    def test_558(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                print(string_of_int(--------------------x));
                print("\\n");
                print(string_of_bool(!!!!!!!!!!!!!!!!!!!y));
            EndBody.
            Function: main
            Body:
                foo(1, False);
            EndBody.
        """
        expect = "1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    
    def test_559(self):
        input = """
            Function: foo
            Body:
                Var: x=1, y=False;
                print(string_of_int(--------------------x));
                print("\\n");
                print(string_of_bool(!!!!!!!!!!!!!!!!!!!y));
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,559))
#endregion    

#region test loop
    def test_560(self):
        input = """
            Function: main
            Body:
                Var: x =1;
                For(x=1, x<10, 1)Do
                    print(string_of_int(x));
                    print("\\n");
                    If(x==5)Then
                        Break;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "1\n2\n3\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    
    def test_561(self):
        input = """
            Function: main
            Body:
                Var: x =1;
                For(x=1, x<10, 1)Do
                    If(x==5)Then
                        Continue;
                    EndIf.
                    print(string_of_int(x));
                    print("\\n");
                EndFor.
            EndBody.
        """
        expect = "1\n2\n3\n4\n6\n7\n8\n9\n"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    
    def test_562(self):
        input = """
            Function: main
            Body:
                Var:x=1;
                For(x=0,x<10,1)Do
                    If(x%2==0) Then
                        print(string_of_int(x));
                    Else
                        Continue;
                    EndIf.
                    print("End statement");
                EndFor
            EndBody.
        """
        expect = "0End statement2End statement4End statement6End statement8End statement"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    
    def test_563(self):
        input = """
            Function: main
            Body:
                Var: x=1;
                For(x=5, x>0, -1)Do
                    print(string_of_int(x));
                    print("\\n");
                EndFor.
            EndBody.
        """
        expect = "5\n4\n3\n2\n1\n"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    
    def test_564(self):
        input = """
            Function: main
            Body:
                Var: x=4;
                While x>1 Do
                    print(string_of_int(x));
                    print("\\n");
                    x = x-1;
                EndWhile.
            EndBody.
        """
        expect = "4\n3\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    
    def test_565(self):
        input = """
            Var: x=0;
            Function: main
            Body:
                While True Do
                    If(x==10) Then
                        Break;
                    EndIf.
                    print(string_of_int(x));
                    x = x+1;
                EndWhile.
            EndBody.
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_566(self):
        input = """
            Function: main
            Body:
                Var: x=2;
                Do
                    print(string_of_int(x));
                While x<1
                EndDo.
            EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    
    def test_567(self):
        input = """
            Function: isValid
            Parameter: x
            Body:
                Return x<10;
            EndBody.
        
            Function: main
            Body:
                Var: x=1;
                Do
                    print(string_of_int(x));
                    x = x+1;
                While isValid(x)
                EndDo.
            EndBody.
        """
        expect = "123456789"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    
    def test_568(self):
        input = """
            Function: isPrimeNumber
            Parameter: x
            Body:   
                If ((x==2) || (x==3)) Then
                    Return True;
                Else
                    Var: i=1, mid =0;
                    mid = x\\2+1;
                    For(i=2, i<mid, 1) Do
                        If(x%i==0) Then
                            Return False;
                        EndIf.
                    EndFor.
                    Return True;
                EndIf.
            EndBody.
            Function: main
            Body:  
                Var: x=0;
                For(x=2, x<20, 1)Do
                    If(isPrimeNumber(x)) Then
                        print(string_of_int(x));
                        print("\\n");
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "2\n3\n5\n7\n11\n13\n17\n19\n"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    
    def test_569(self):
        input = """
            Function: main
            Body:
                Var: x=1;
                For(x=0,x<5,1)Do
                    Var: y=0;
                    For(y=0,y<5,1)Do
                        print(string_of_int(x*y));
                        print("||");
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "0||0||0||0||0||0||1||2||3||4||0||2||4||6||8||0||3||6||9||12||0||4||8||12||16||"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    
    def test_570(self):
        input = """
            Function: main
            Body:
                Var: arr[4][4] = {{0,0,0,0},
                                {0,0,0,0},
                                {0,0,0,0},
                                {0,0,0,0}};
                Var: iW=0,iH=0;
                For(iH=0,iH<4,1)Do
                    For(iW=0,iW<4,1)Do
                        If(iW==iH) Then
                            arr[iH][iW] = 1;
                        EndIf.
                    EndFor.
                EndFor.

                For(iH=0,iH<4,1)Do
                    For(iW=0,iW<4,1)Do
                        print(string_of_int(arr[iH][iW]));
                    EndFor.
                    print("\\n");
                EndFor.
            EndBody.
        """
        expect = "1000\n0100\n0010\n0001\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_571(self):
        input = """
            Function: multiply
            Parameter: a[3][3], b[3][3]
            Body:
                Var: result[3][3] = {{0,0,0},
                                     {0,0,0},
                                     {0,0,0}};
                Var: iW = 0, iH = 0;
                For(iW=0,iW<3,1)Do
                    For(iH=0,iH<3,1)Do
                        result[iH][iW] = a[iH][iW] * b[iH][iW];
                    EndFor.
                EndFor.
                Return result;
            EndBody.
            Function: main
            Body:
                Var: a[3][3] = {{1,2,3},
                                {8,9,4},
                                {7,6,5}};
                Var: b[3][3] = {{1,8,7},
                                {2,9,6},
                                {3,4,5}};
                Var: result[3][3] = {{0,0,0},
                                     {0,0,0},
                                     {0,0,0}};
                Var: iW=0,iH=0;
                result = multiply(a,b);
                For(iW=0,iW<3,1)Do
                    For(iH=0,iH<3,1)Do
                        print(string_of_int(result[iH][iW]));
                        print("|");
                    EndFor.
                    print("\\n");
                EndFor.                
            EndBody.
        """
        expect = "1|16|21|\n16|81|24|\n21|24|25|\n"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    
#region test if
    def test_572(self):
        input = """
            Function: doWhile
            Body:
                Var: x=0;
                Do
                    Var: threshold = 0;
                    threshold = x+5;
                    Do
                        print(string_of_int(x));
                        print("|");
                        x = x+1;
                    While x<threshold
                    EndDo.
                    print("--");
                While x<20
                EndDo.
            EndBody.
            Function: main
            Body:
                doWhile();
            EndBody.
        """
        expect = "0|1|2|3|4|--5|6|7|8|9|--10|11|12|13|14|--15|16|17|18|19|--"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_573(self):
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                While x<.20.0 Do
                    Var: threshold = 0.0;
                    threshold = x+.5.0;
                    While x<.threshold Do
                        print(string_of_float(x));
                        print("|");
                        x = x+.1.0;
                    EndWhile.
                    print("--");
                EndWhile.
            EndBody.
        """
        expect = "1.0|2.0|3.0|4.0|5.0|--6.0|7.0|8.0|9.0|10.0|--11.0|12.0|13.0|14.0|15.0|--16.0|17.0|18.0|19.0|20.0|--"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_574(self):
        input = """
            Function: bar
            Body:
                print("Inside bar\\n");
            EndBody.

            Function: foo
            Body:
                bar();
                print("inside foo\\n");
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "Inside bar\ninside foo\n"
        self.assertTrue(TestCodeGen.test(input,expect,574))
    
    def test_575(self):
        input = """
            Function: foo
            Parameter: x
            Body:
                If(x==1) Then
                    Return 1;
                Else
                    Return x + foo(x-1);
                EndIf.
            EndBody.
            Function: main
            Body:
                print(string_of_int(foo(9)));
            EndBody.
        """
        expect = "45"
        self.assertTrue(TestCodeGen.test(input,expect,575))
    
    def test_576(self):
        input = """
            Function: foo
            Body:
                Var: x =False, y=0;
                While !x Do
                    print(string_of_int(y));
                    print("-");
                    print(string_of_bool(x));
                    x = x || (y==12);
                    y = y+1;
                    print("||");
                EndWhile.
            EndBody.
            Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "0-false||1-false||2-false||3-false||4-false||5-false||6-false||7-false||8-false||9-false||10-false||11-false||12-false||"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    
    def test_577(self):
        input = """
            Function: foo
            Parameter: x
            Body:
                print(string_of_int(-x));
            EndBody.
            Function: main
            Body:
                foo(5);
            EndBody.
        """
        expect = "-5"
        self.assertTrue(TestCodeGen.test(input,expect,577))
    
    def test_578(self):
        input = """
            Function: foo
            Parameter: y
            Body:
                If(y == 1)Then
                    print("foo finished at ");
                    print(string_of_int(y));
                Else
                    foo(y-1);
                EndIf.
            EndBody.

            Function: main
            Body:
                foo(10);
            EndBody.
        """
        expect = "foo finished at 1"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    
    def test_579(self):
        input = """
            Function: main
            Body:
                Var: x =0;
                While x<25 Do
                    If(x%2==0) Then
                        print("2-");
                        print(string_of_int(x));
                    ElseIf(x%3==0)Then
                        print("3-");
                        print(string_of_int(x));
                    EndIf.
                    x = x +1;
                    print("|");
                EndWhile.
            EndBody.
        """
        expect = "2-0||2-2|3-3|2-4||2-6||2-8|3-9|2-10||2-12||2-14|3-15|2-16||2-18||2-20|3-21|2-22||2-24|"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    
    def test_580(self):
        input = """
            Function: main
            Body:
                Var: x=0;
                print(string_of_int(x+3*4\\2));
            EndBody.
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    
    def test_581(self):
        input = """
            Function: main
            Body:
                Var: x=3;
                print(string_of_int((x+3)*4\\2));
            EndBody.
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    
    def test_582(self):
        input = """
            Function: main
            Body:
                Var: x=2;
                print(string_of_int(x+3*(4\\2)));                
            EndBody.
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    
    def test_583(self):
        input = """
            Function: main
            Body:
                Var: x = 2.0;
                print(string_of_float(x +. 3.0 *. 4.0 \\. 2.0));
            EndBody.
        """
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    
    def test_584(self):
        input = """
            Function: main
            Body:
                Var: x = 2.0;
                print(string_of_float((x +. 3.0) *. 4.0 \\. 2.0));
            EndBody.
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    
    def test_585(self):
        input = """
            Function: main
            Body:
                Var: x = 3.0;
                print(string_of_float(x +. 3.0 *. (4.0 \\. 2.0)));
            EndBody.
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    
    def test_586(self):
        input = """
            Function: main
            Body:
                print(string_of_bool((5>=3)&&(5.0>.3.0)));
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    
    def test_587(self):
        input = """
            Function: main
            Body:
                print(string_of_bool((5!=3)&&(5.0=/=3.0)));
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    
    def test_588(self):
        input = """
            Function: foo
            Body:
                Return 5;
            EndBody.
            Function: bar
            Parameter: x
            Body:
                Return x+5;
            EndBody.
            Function: main
            Body:
                print(string_of_bool(foo()==bar(foo())));
            EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    
    def test_589(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    
    def test_590(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    
    def test_591(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    
    def test_592(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_593(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    
    def test_594(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    
    def test_595(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_596(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,596))
    
    def test_597(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
    def test_598(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    
    def test_599(self):
        input = """
            Function: main
            Body:
                print("Copy and paste");
            EndBody.
        """
        expect = "Copy and paste"
        self.assertTrue(TestCodeGen.test(input,expect,599))
#endregion