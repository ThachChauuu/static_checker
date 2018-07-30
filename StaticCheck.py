
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
import functools

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    # global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]

    getInt = Symbol("getInt", MType([], IntType()))
    putInt = Symbol("putInt", MType([IntType()], VoidType()))
    putIntLn = Symbol("putIntLn", MType([IntType()], VoidType()))
    getFloat = Symbol("getFloat", MType([], FloatType()))
    putFloat = Symbol("putFloat", MType([FloatType()], VoidType()))
    putFloatLn = Symbol("putFloatLn", MType([FloatType()], VoidType()))
    putBool = Symbol("putBool", MType([BoolType()], VoidType()))
    putBoolLn = Symbol("putBoolLn", MType([BoolType()], VoidType()))
    putString = Symbol("putString", MType([StringType()], VoidType()))
    putStringLn = Symbol("putStringLn", MType([StringType()], VoidType()))
    putLn = Symbol("putLn", MType([], VoidType()))

    global_envi = [getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn]
            
    def __init__(self,ast):
        self.ast = ast

    def find_scope(self, lst):
        temp = lst[len(lst)-1]
        if all(isinstance(i, Symbol) for i in temp):
            return temp
        else:
            self.find_scope(temp)

    def lookup1(self, name, lst):
        for i in reversed(lst):
            if type(i) is list:
                pass

    def exitScope(self, lst):
        for i in lst:
            if type(i) is list:
                lst.remove(i)
        return lst

    def lookupId(self, id, lst):
        for i in lst:
            if type(i) is list:
                for x in i:
                    if id == x.name:
                        return x
            else:
                if id == i.name:
                    return i
        return None   

    def checkExpr(self, expr, lst):
        if type(expr) is Id:
            s = self.lookupId(expr.name, lst)
            if s:
                return s.mtype
            else:
                raise Undeclared(Identifier(), expr.name)
        elif type(expr) is IntLiteral:
            return IntType()
        elif type(expr) is StringLiteral:
            return StringType()
        elif type(expr) is FloatLiteral:
            return FloatType()
        elif type(expr) is BooleanLiteral:
            return BoolType()
        elif type(expr) is ArrayCell:
            arrtype = self.checkExpr(expr.arr, lst)
            idxtype = self.checkExpr(expr.idx, lst)
            if (arrtype == ArrayType() or arrtype == ArrayPointerType()) and idxtype == IntType():
                return ArrayType()
            else:
                raise TypeMismatchInExpression(expr)
        elif type(expr) is UnaryOp:
            rtype = self.checkExpr(expr.body, lst)
            if rtype == BoolType() and expr.op == "!":
                return BoolType()
            elif rtype == IntType() and expr.op == "-":
                return IntType()
            elif rtype == FLoatType() and expr.op == "-":
                return FloatType()
            else:
                raise TypeMismatchInExpression(expr)
        elif type(expr) is BinaryOp:
            ltype = self.checkExpr(expr.left, lst)
            rtype = self.checkExpr(expr.right, lst)
            if expr.op == "<" or expr.op == ">" or expr.op == "<=" or expr.op == ">=":
                if (ltype == IntType() and rtype == IntType()) or (ltype == FloatType() and rtype == IntType()) or (ltype == IntType() and rtype == FloatType()) or (ltype == FloatType() and rtype == FloatType()):
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "==" or expr.op == "!=":
                if ltype == rtype:
                    if ltype == VoidType() or ltype == ArrayPointerType() or ltype == ArrayType():
                        raise TypeMismatchInExpression(expr)
                    else:
                        return BoolType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "+" or expr.op == "-" or expr.op == "*" or expr.op == "/":
                if ltype == IntType() and rtype == IntType():
                    return IntType()
                elif (ltype == IntType() and rtype == FloatType()) or (ltype == FloatType() and rtype == IntType()) or (ltype == FloatType() and rtype == FloatType()):
                    return FloatType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "=":
                if ltype == rtype:
                    if ltype == VoidType() or ltype == ArrayType() or ltype == ArrayPointerType():
                        raise TypeMismatchInExpression(expr)
                    else:
                        return IntType()
            elif expr.op == "%":
                if ltype == IntType() and rtype == IntType():
                    return IntType()
                else:
                    raise TypeMismatchInExpression(expr)
            else:
                raise TypeMismatchInExpression(expr)
        elif type(expr) is CallExpr:
            ptypes = [self.checkExpr(x, lst) for x in expr.param]
            s = self.lookupId(expr.method.name, lst)
            if s is None or not type(s.mtype) is MType:
                raise Undeclared(Function(), expr.method.name)
            elif len(s.mtype.partype) != len(ptypes):
                raise TypeMismatchInStatement(expr)
            else:
                return s.mtype.rettype
        else:
            return IntType()
            
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        ins_glo_envi = c.copy()
        for d in ast.decl:
            if type(d) is VarDecl:
                self.visitVarDecl(d, ins_glo_envi)
            else:
                print(len(ins_glo_envi))
                self.visitFuncDecl(d, ins_glo_envi)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name, c, lambda x: x.name):
            raise Redeclared(Variable(), ast.variable.name)
        else:
            c.append(Symbol(ast.variable.name, ast.varType))

    def visitFuncDecl(self, ast, c):        # c is []
        if self.lookup(ast.name.name, c, lambda x: x.name):
            raise Redeclared(Function(), ast.name.name)
        else:
            c.append(Symbol(ast.name.name, MType([p.varType for p in ast.param] if ast.param else [], ast.returnType)))
        c.insert(len(c), [])
        for p in ast.param:
            if self.lookup(p.variable.name, c[len(c)-1], lambda x: x.name):
                raise Redeclared(Parameter(), p.variable.name)
            else:
                c[len(c)-1].append(Symbol(p.variable.name, p.varType))
        self.visitBlock(ast.body, c)
        c = self.exitScope(c)
        print(len(c))

    
    def visitBlock(self, ast, c):       # c is [...[..]]
        for x in ast.decl:
            temp = c[len(c) - 1]
            self.visitVarDecl(x, temp)
        for st in ast.stmt:
            if type(st) is If:
                self.visitIf(st, c)
            elif type(st) is For:
                self.visitFor(st, c)
            elif type(st) is Break:
                self.visitBreak(st, c)
            elif type(st) is Continue:
                self.visitContinue(st, c)
            elif type(st) is Dowhile:
                self.visitDowhile(st, c)
            elif type(st) is BinaryOp:
                self.visitBinaryOp(st, c)
            elif type(st) is UnaryOp:
                self.visitUnaryOp(st, c)
            elif type(st) is CallExpr:
                self.visitCallExpr(st, c)
            elif type(st) is Id:
                self.visitId(st, c)
            elif type(st) is ArrayCell:
                self.visitArrayCell(st, c)
            elif type(st) is Block:
                c.insert(len(c), [])     # c is [...[...[...]]]
                self.visitBlock(st, c)

    def visitIf(self, ast, c):          # c is [...[...]]
        etype = self.checkExpr(ast.expr, c)
        if etype != BoolType():
            raise TypeMismatchInStatement(ast)
        if type(ast.thenStmt) is Block:
            c.insert(len(c), [])        # c is [...[...[...]]]
            self.visitBlock(ast.thenStmt, c)
            del c[-1]                      # c is [...[...]]
        if type(ast.elseStmt) is Block:
            c.insert(len(c), [])
            self.visitBlock(ast.elseStmt, c)


    def visitFor(self, ast, c):
        e1type = self.checkExpr(ast.expr1, c)
        e2type = self.checkExpr(ast.expr2, c)
        e3type = self.checkExpr(ast.expr3, c)
        if e1type != IntType() or e3type != IntType() or e2type != BoolType():
            raise TypeMismatchInStatement(ast)

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitDowhile(self, ast, c):
        etype = self.checkExpr(ast.exp, c)
        if etype != BoolType():
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, c):
        self.checkExpr(ast, c)

    def visitUnaryOp(self, ast, c):
        self.checkExpr(ast, c)

    def visitCallExpr(self, ast, c):
        self.checkExpr(ast, c)

    def visitId(self, ast, c):
        self.checkExpr(ast, c)

    def visitArrayCel(self, ast, c):
        self.checkExpr(ast, c)

    

