
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

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
    putFloatLn = Symbol("putFloatLn", MType([FloatType], VoidType()))
    putBool = Symbol("putBool", MType([BoolType], VoidType()))
    putBoolLn = Symbol("putBoolLn", MType([BoolType], VoidType()))
    putString = Symbol("putString", MType([StringType()], VoidType()))
    putStringLn = Symbol("putStringLn", MType([StringType()], VoidType()))
    putLn = Symbol("putLn", MType([], VoidType()))

    global_envi = [getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn]
            
    def __init__(self,ast):
        self.ast = ast

    def lookupId(self, id, lst):
        si = self.lookup(id, lst[len(lst) - 1], lambda x: x.name)
        if si is None:
            so = self.lookup(id, lst[0:len(lst)-1], lambda x: x.name)
            if so:
                return so
            return None
        return si            

    def checkExpr(self, expr, lst):
        if type(expr) is Id:
            s = self.lookupId(expr, lst)
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
            elif rtype == Inttype() and expr.op == "-":
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
                pass
                # if stmt
                    # raise TypeMismatchInStatement(expr)
                # else:
                    # raise TypeMismatchInExpression(expr)
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
                self.visitFuncDecl(d, ins_glo_envi)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name, c, lambda x: x.name):
            raise Redeclared(Variable(), ast.variable.name)
        else:
            c.append(Symbol(ast.variable.name, ast.varType))
        # self.global_envi = c.copy()

    def visitFuncDecl(self, ast, c):        # c is []
        if self.lookup(ast.name.name, c, lambda x: x.name):
            raise Redeclared(Function(), ast.name.name)
        else:
            c.append(Symbol(ast.name.name, MType([p.varType for p in ast.param] if ast.param else [], ast.returnType)))
        # self.global_envi = c.copy()
        c.insert(len(c), [])
        for p in ast.param:
            if self.lookup(p.variable.name, c[len(c)-1], lambda x: x.name):
                raise Redeclared(Parameter(), p.variable.name)
            else:
                c[len(c)-1].append(Symbol(p.variable.name, p.varType))
        self.visitBlock(ast.body, c)
        # self.visitBlock(ast.body, c[len(c)-1])
        # exit scope
        del c[-1]

    
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
            elif type(st) is Block:
                c.insert(len(c), [])     # c is [...[...[...]]]
                self.visitBlock(st, c)  
        del c[-1]

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
        pass

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitDowhile(self, ast, c):
        pass             

    # def visitProgram(self,ast, c):    
    #     return [self.visit(x,c) for x in ast.decl]

    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    

